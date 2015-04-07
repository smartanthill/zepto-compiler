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
import antlr4.error.ErrorListener
from ECMAScript.ECMAScriptLexer import ECMAScriptLexer
from ECMAScript.ECMAScriptParser import ECMAScriptParser
from ECMAScript.ECMAScriptVisitor import ECMAScriptVisitor

class CompilerError(Exception):
    pass


class Compiler:
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.next_node_id = 0
        self.removed_nodes = []
        self.error_flag = False
        
    def init_node(self, node):
        node.node_id = self.next_node_id
        self.next_node_id += 1
        return node
        
    def remove_node(self, node):
        self.removed_nodes.append(node.node_id)
        

    def reportError(self, fmt, args):
        self.error_flag = True
        print fmt % args
        
    def raiseError(self, fmt, args):
        self.error_flag = True
        print fmt % args
        raise CompilerError()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #print("line " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)
        self.error_flag = True

    def checkStage(self, name):
        if self.error_flag:
            print "Stage %s giving up because of previous errors" % name
            raise CompilerError()


class ProxyAntlrErrorListener(antlr4.error.ErrorListener.ErrorListener):
    '''
    Proxy class that implements antl4 ErrorListener
    
    '''
    def __init__(self, compiler):
        self.compiler = compiler
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        '''
        Implements ErrorListener from antlr4
        '''
        self.compiler.syntaxError(recognizer, offendingSymbol, line, column, msg, e)
    

def parse_js_string(compiler, data):

    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = ECMAScriptLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(ProxyAntlrErrorListener(compiler))
    tree = parser.program()
    
    compiler.checkStage('parse_js')

    return tree

def dump_antlr_tree(tree):
    antlr_visitor = DumpAntlrTreeVisitor()
    antlr_visitor.visit(tree)
    return antlr_visitor.result

class DumpAntlrTreeVisitor(antlr4.ParseTreeVisitor):
    '''
    AntLr visitor class that will dump every node in the tree
    Used for testing mostly
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.result = []
        self.stack = []

    def visitChildren(self, node):

        s = '+-' * len(self.stack) + type(node).__name__
        self.stack.append(len(self.result))
        self.result.append(s)

        for i in range(node.getChildCount()):
            node.getChild(i).accept(self)

        self.stack.pop()

    def visitTerminal(self, node):
        self.result[self.stack[-1]] += " '" + node.getText() + "'"
