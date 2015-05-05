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

from smartanthill_zc.node import Node


def visit_node(visitor, node):
    '''
    Dynamic version of node visitor using reflection
    Trivial implementation
    '''
    assert isinstance(node, Node)
    name = 'visit_' + type(node).__name__
    attr = getattr(visitor, name, None)
    if attr:
        attr(node)
    else:
        getattr(visitor, 'default_visit')(node)


def walk_node_childs(walker, node):
    '''
    Dynamic version of node walker using reflection
    Trivial implementation
    '''
    assert isinstance(node, Node)
    names = dir(node)
    for current in names:
        if current.startswith('child_'):
            ch = getattr(node, current)
            if ch:
                walker.walk_node(ch)
        elif current.startswith('childs_'):
            chs = getattr(node, current)
            for ch in chs:
                walker.walk_node(ch)


class NodeWalker(object):

    '''
    Base class for walker
    '''
    pass


class NodeVisitor(object):

    '''
    Base class for visitor
    '''
    pass


def check_all_nodes_reachables(compiler, root):
    '''
    Checks a syntax tree walking it down and verifying that all node id are
    reachable and verifying parenthood relationship
    Is used as a self check to verify on common issues of the tree structure
    '''
    walker = _CheckReachableWalker(
        compiler.removed_nodes, compiler.next_node_id)
    walker.walk_node(root)
    walker.finish()


class _CheckReachableWalker(NodeWalker):

    '''
    Walker class used by check_all_nodes_reachables function
    '''

    def __init__(self, removed_nodes, next_node_id):
        self.dones = []
        self.parents = []
        self.removed_nodes = removed_nodes
        self.next_node_id = next_node_id

    def walk_node(self, node):
        assert node
        if len(self.parents) != 0:
            assert self.parents[-1] == node.get_parent()

        self.dones.append(node.node_id)

        self.parents.append(node)
        walk_node_childs(self, node)
        self.parents.pop()

    def finish(self):
        self.dones += self.removed_nodes
        self.dones.sort()
        expected = 0
        for current in self.dones:
            if current == expected:
                expected += 1
            elif current == expected - 1:
                print 'Node %i has been reached again' % current
            elif current > expected:
                print ('Node range %i to %i has not been reached' %
                       (expected, current + 1))
            else:
                assert False

        if expected < self.next_node_id:
            print ('Node range %i to %i has not been reached' %
                   (expected, self.next_node_id - 1))
        elif expected > self.next_node_id:
            assert False


def dump_tree(node):
    '''
    Dump a syntax tree to a human readable text format
    Used for debugging and testing
    '''
    walker = _DumpTreeWalker()
    walker.walk_node(node)
    return walker.result


class _DumpTreeWalker(NodeWalker):

    '''
    Walker class used by dump_tree function
    '''

    def __init__(self):
        self.result = []
        self.index = 0

    def walk_node(self, node):
        ctx_attrs = ''
        names = dir(node)
        for current in names:
            if current.startswith('tk_'):
                assert False
            elif current.startswith('str_'):
                assert False
            elif current.startswith('txt_'):
                ctx_attrs += " %s='%s'" % (current[4:],
                                           getattr(node, current))

        s = '+-' * self.index + type(node).__name__ + ctx_attrs
        self.result.append(s)
        self.index += 1
        walk_node_childs(self, node)
        self.index -= 1
