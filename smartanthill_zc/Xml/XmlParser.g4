/*
 * Copyright (C) 2015 OLogN Technologies AG
 *
 * This source file is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License version 2
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */
 
parser grammar XmlParser;
options {tokenVocab=XmlLexer;}
 
/// [1] document ::= ( prolog element Misc* ) - ( Char* RestrictedChar Char* )
document
 : prolog? element EOF
 ;

/// [22] prolog ::= XMLDecl Misc* (doctypedecl Misc*)?
prolog
 : xmlDecl
 ;

/// [23] XMLDecl ::= '<?xml' VersionInfo EncodingDecl? SDDecl? S? '?>'
xmlDecl
 : '<?xml' (S attribute)* S? '?>'
 ;

/// [39] element ::= EmptyElemTag
///                  | STag content ETag
element
  : emptyElemTag        #emptyTagRule
  | sTag content eTag   #seTagRule
  ;

/// [44] EmptyElemTag ::= '<' Name (S Attribute)* S? '/>'
emptyElemTag
  : '<' Name (S attribute)* S? '/>'
  ;

/// [40] sTag ::= '<' Name (S Attribute)* S? '>'
sTag
  : '<' Name (S attribute)* S? '>'
  ;

/// [41] Attribute ::= Name Eq AttValue
attribute
  : Name Eq AttValue
  ;

/// [42] ETag ::= '</' Name S? '>'
eTag
  : S? '</' Name S? '>'
  ;

/// [43] content ::= CharData? ((element | Reference | CDSect | PI | Comment) CharData?)*
content
  : element*
  ;


