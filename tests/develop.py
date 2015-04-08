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

import sys

from smartanthill_zc import compiler
from smartanthill_zc import syntax
from smartanthill_zc import visitor


def main():
    #    tree = compiler.parse_js_string(u'return 2 + 3;')
    #    print compiler.tree_to_str(tree)

    #    parse_tree = compiler.parse_js_string(u'return Some.break(); return Some.Thing();')
    comp = compiler.Compiler()
    js_tree = compiler.parse_js_string(comp, u'for(var i = 0; i < 5; j++) ;')
    print '\n'.join(compiler.dump_antlr_tree(js_tree))
    root = syntax.js_tree_to_syntax_tree(comp, js_tree)
    visitor.check_all_nodes_reachables(comp, root)
    print '\n'.join(visitor.dump_tree(root))


# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
