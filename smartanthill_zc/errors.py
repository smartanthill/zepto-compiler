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


class CompilerError(Exception):

    '''
    Generic error raised when compilation problem occurs
    '''

    def __init__(self, value):
        '''
        Constructor
        '''
        super(CompilerError, self).__init__()
        self.value = value

    def __str__(self):
        '''
        String representation
        '''
        return '; '.join(self.value)


class ResolutionCycleError(Exception):

    '''
    Raised when a resolution cycle is detected
    '''
    pass


class UnresolvedError(Exception):

    '''
    Raised when accessing resolution info on
    an expression not resolved before
    '''


class PreviousResolutionError(Exception):

    '''
    Raised when accessing resolution info on
    an expression that raised a resolution error before
    '''
    pass


class ResolutionError(Exception):

    '''
    Raised when a resolution error occurs that needs to raise
    '''
    pass
