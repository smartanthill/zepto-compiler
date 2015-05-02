# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import antlr4

from smartanthill_zc.antlr_helper import (_ProxyAntlrErrorListener,
                                          check_reserved_name)
from smartanthill_zc.bodypart import (BodyPartDeclNode, BodyPartListNode,
                                      Encoding, FieldTypeDeclNode,
                                      MemberDeclNode, MessageTypeDeclNode)
from smartanthill_zc.builtin import ParameterListNode
from smartanthill_zc.Xml import XmlParserVisitor
from smartanthill_zc.Xml.XmlLexer import XmlLexer
from smartanthill_zc.Xml.XmlParser import XmlParser


def parse_xml_string(compiler, data):
    '''
    Parse unicode string containing xml plug-in manifest
    Returns an antlr parse tree
    '''
    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = XmlLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = XmlParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(_ProxyAntlrErrorListener(compiler))
    tree = parser.document()

    compiler.check_stage('parse_xml')

    return tree


def xml_parse_tree_process(compiler, xml_tree):
    '''
    Translates an xml parse tree as returned by antlr4 into a
    colection of body parts declarations, and extra meta data.
    '''

    bodyparts = create_body_parts_manager(compiler, compiler.BUILTIN)
    visitor = _XmlTreeVisitor(compiler, bodyparts)
    visitor.visit(xml_tree)

    compiler.check_stage('xml_bodyparts')

    return bodyparts


def match_tag_names(compiler, sTag, eTag):
    '''
    Verifies that open and close tag have the same name
    If this is not the case, reports error and raises
    '''

    if sTag.Name().getText() != eTag.Name().getText():
        compiler.report_error(eTag, "Close tag '%s' does not match the"
                                    " opening tag" % eTag.Name().getText())
        compiler.report_error(sTag, "Open tag here")

        # We raise, since xml structure is probably messed up
        compiler.raise_error()


def _get_name(compiler, value):
    '''
    Helper function, returns a tag or attribute name
    '''
    return get_token_text(compiler, value.Name())


def _get_att_value(compiler, att):
    '''
    Helper function, returns a tag attribute value
    '''
    # TODO, escape sequencce replace
    # TODO remove first and last
    del compiler

    txt = att.AttValue().getText()
    assert len(txt) >= 2
    return str(txt[1:-1])


def _get_ctx_childs(compiler, current):
    '''
    Helper function, returns a tuple with tag and content
    '''

    if isinstance(current, XmlParser.EmptyTagRuleContext):
        return (current.emptyElemTag(), [])
    elif isinstance(current, XmlParser.SeTagRuleContext):
        match_tag_names(compiler, current.sTag(), current.eTag())
        return (current.sTag(), current.content().element())
    else:
        assert False


def _get_attributes(compiler, ctx, req_names, opt_names):
    '''
    Returns a dictionary from xml attributes,
    it checks that all names in req_names are found,
    that no duplicate name is found,
    and that no unexpected name is found
    '''

    result = {}
    for current in ctx.attribute():
        name = _get_name(compiler, current)
        if name in result:
            compiler.report_error(current, "Duplicated attribute '%s'" % name)
        elif name not in req_names and name not in opt_names:
            compiler.report_error(current, "Unexpected attribute '%s'" % name)
        else:
            result[name] = _get_att_value(compiler, current)

    ok = True
    for current in req_names:
        if current not in result:
            compiler.report_error(current, "Missing attribute '%s'" % current)
            ok = False

    if not ok:
        compiler.raise_error()

    return result


def _get_tags(compiler, content, req_names, opt_names):
    '''
    Returns a dictionary from xml tags,
    it checks that all names in req_names are found,
    that no duplicate name is found,
    and that no unexpected name is found
    '''
    result = {}

    for current in content:

        ctx, childs = _get_ctx_childs(compiler, current)
        name = _get_name(compiler, ctx)

        if name in result:
            compiler.report_error(current, "Duplicated child tag '%s'" % name)
        elif name not in req_names and name not in opt_names:
            compiler.report_error(current, "Unexpected child tag '%s'" % name)
        else:
            result[name] = (ctx, childs)

    ok = True
    for current in req_names:
        if current not in result:
            compiler.report_error(current, "Missing child tag '%s'" % current)
            ok = False

    if not ok:
        compiler.raise_error()

    return result


def _make_bodypart(compiler, manager, ctx, content):
    '''
    Creates a BodyPartDeclNode from an xml <smartanthill.plugin>
    '''

    name = _get_name(compiler, ctx)
    assert name == 'smartanthill.plugin'

    bodypart = compiler.init_node(BodyPartDeclNode(), ctx)
    att = _get_attributes(compiler, ctx,
                          ['name', 'id', 'version'], [])

    if att['version'] != '1.0':
        compiler.report_error(ctx, "Unidentified version number '%s'" %
                              att['version'])

    bodypart.txt_name = att['name']
    try:
        bodypart.bodypart_id = long(att['id'])
    except:
        compiler.report_error(ctx, "Bad id '%s'" % att['id'])

    tags = _get_tags(compiler, content,
                     ['command', 'reply'],
                     ['description', 'peripheral'])

    # build parameter list from <command>
    pl = compiler.init_node(ParameterListNode(), ctx)
    bodypart.set_parameter_list(pl)

    # build reply type <reply>
    if len(tags['reply'][1]) == 0:
        compiler.report_error(tags['reply'][0], "Empty 'reply' not allowed")
        compiler.raise_error()

    reply_name = '_zc_reply_type_' + att['name']
    reply = compiler.init_node(
        MessageTypeDeclNode(reply_name), tags['reply'][0])

    for current in tags['reply'][1]:

        ctx, ch = _get_ctx_childs(compiler, current)
        name = _get_name(compiler, ctx)

        if name != 'field':
            compiler.report_error(ctx, "Unexpected child tag '%s'" % name)
            compiler.raise_error()

        field = _make_field(compiler, manager, ctx, ch)

        reply.add_element(field)

    bodypart.set_reply_type(reply)

    manager.child_body_part_list.add_declaration(bodypart)


def _make_field(compiler, manager, ctx, content):
    '''
    Creates a MemberDeclNode from an xml <field>
    '''
    name = _get_name(compiler, ctx)
    assert name == 'field'
    att = _get_attributes(compiler, ctx,
                          ['name', 'type'], ['min', 'max'])

    field = manager.child_field_type_factory.create_field_type(
        compiler, ctx, att)

    member = compiler.init_node(MemberDeclNode(att['name']), ctx)
    member.ref_field_type = field

    # TODO handle <meaning>
    del content

    return member


class _XmlTreeVisitor(XmlParserVisitor.XmlParserVisitor):

    '''
    Visitor class that implements xml_parse_tree_process function

    The template for the visitor is copy&paste from super class interface
    XmlParserVisitor.XmlParserVisitor
    '''

    def __init__(self, compiler, manager):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._manager = manager

    def _try_bodypart(self, ctx, content):
        '''
        If current tag corresponds to a body-part, it creates the body-part
        and returns True, returns False otherwise
        '''
        name = _get_name(self._compiler, ctx)
        if name == 'smartanthill.plugin':
            _make_bodypart(self._compiler, self._manager, ctx, content)
            return True
        else:
            return False

    # Visit a parse tree produced by XmlParser#emptyTagRule.
    def visitEmptyTagRule(self, ctx):

        self._try_bodypart(ctx.emptyElemTag(), [])

    # Visit a parse tree produced by XmlParser#seTagRule.
    def visitSeTagRule(self, ctx):

        match_tag_names(self._compiler, ctx.sTag(), ctx.eTag())

        if self._try_bodypart(ctx.sTag(), ctx.content().element()):
            pass
        else:
            self.visitChildren(ctx.content())
