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
 
lexer grammar XmlLexer;

/// [14] CharData ::= [^<&]* - ([^<&]* ']]>' [^<&]*)
CharData
  : ~[<&]+ -> skip
  ;

/// [15] Comment ::= '<!--' ((Char - '-') | ('-' (Char - '-')))* '-->'
Comment
 : '<!--' .*? '-->' -> skip
 ;

/// [23]    XMLDecl    ::=      '<?xml' VersionInfo EncodingDecl? SDDecl? S? '?>'

/// [39] element ::= EmptyElemTag
///                 | STag content ETag 
/// [44] EmptyElemTag ::= '<' Name (S Attribute)* S? '/>'
/// [40] STag ::= '<' Name (S Attribute)* S? '>'
/// [41] Attribute ::= Name Eq AttValue
/// [42] ETag ::= '</' Name S? '>'
 
LT :        '<'     -> pushMode(TAG);
LT_SLASH :  '</'    -> pushMode(TAG);
XML_DECL:   '<?xml' -> pushMode(TAG);

mode TAG;

GT :        '>'     -> popMode;
SLASH_GT :  '/>'    -> popMode;
QUESTION_GT:'?>'    -> popMode;



/// [25] Eq ::= S? '=' S?
Eq : S? '=' S?;

/// [3] S ::= (\u20 | \u9 | \uD | \uA)+
S
 : [\u0020\u0009\u000D\u000A]+
 ;


/// [10] AttValue ::= '"' ([^<&"] | Reference)* '"'
///                   |  "'" ([^<&'] | Reference)* "'"
AttValue
  : '"' (~[<&"] | Reference)* '"'
  | '\'' (~[<&'] | Reference)* '\''
  ;


fragment Reference
  : '&amp;'
  | '&lt;'
  | '&gt;'
  | '&apos;'
  | '&quot;'
  ;

/// [5] Name ::= NameStartChar (NameChar)*
Name
  : NameStartChar (NameChar)*
  ;

/// [4a] NameChar ::= NameStartChar | "-" | "." | [0-9] | \uB7 | ......
fragment NameChar
  : NameStartChar
  | '-'
  | '.'
  | [0-9]
//  | '\u00B7'
//  | [\u0300-\u036F]
//  | [\u203F-\u2040]
  ;

/// [4] NameStartChar ::= ":" | [A-Z] | "_" | [a-z] | .....
fragment NameStartChar
  : ':'
  | [A-Z]
  | '_'
  | [a-z]
//  | [\u00C0-\u00D6]
//  | [\u00D8-\u00F6]
//  | [\u00F8-\u02FF]
//  | [\u0370-\u037D]
//  | [\u037F-\u1FFF]
//  | [\u200C-\u200D]
//  | [\u2070-\u218F]
//  | [\u2C00-\u2FEF]
//  | [\u3001-\uD7FF]
//  | [\uF900-\uFDCF]
//  | [\uFDF0-\uFFFD]
//  | [\u10000-\uEFFFF]
  ;
