/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 by Bart Kiers
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */
grammar ECMAScript;

@parser::members {
}

@lexer::members {
}

/// Program :
///     SourceElements?
program
 : sourceElements? EOF
 ;

/// SourceElements :
///     SourceElement
///     SourceElements SourceElement
sourceElements
 : sourceElement+
 ;

/// SourceElement :
///     Statement
///     FunctionDeclaration
sourceElement
 : statement
// | functionDeclaration
 ;

/// Statement :
///     Block
///     VariableStatement
///     EmptyStatement
///     ExpressionStatement
///     IfStatement
///     IterationStatement
///     ContinueStatement
///     BreakStatement
///     ReturnStatement
///     WithStatement
///     LabelledStatement
///     SwitchStatement
///     ThrowStatement
///     TryStatement
///     DebuggerStatement
statement
 : block
 | variableStatement
 | emptyStatement
 | expressionStatement
 | ifStatement
 | iterationStatement
// | continueStatement
// | breakStatement
 | returnStatement
// | withStatement
// | labelledStatement
// | switchStatement
// | throwStatement
// | tryStatement
// | debuggerStatement
  | mcuSleepStatement
 ;

// mb: ad-hoc rule added for mcu_sleep function call
mcuSleepStatement
  : 'mcu_sleep' arguments eos
;


/// Block :
///     { StatementList? }
block
 : '{' statementList? '}'
 ;

/// StatementList :
///     Statement
///     StatementList Statement
statementList
 : statement+
 ;

/// VariableStatement :
///     var VariableDeclarationList ;
variableStatement
 : Var variableDeclarationList eos
 ;

/// VariableDeclarationList :
///     VariableDeclaration
///     VariableDeclarationList , VariableDeclaration
variableDeclarationList
 : variableDeclaration ( ',' variableDeclaration )*
 ;

/// VariableDeclaration :
///     Identifier Initialiser?
variableDeclaration
 : Identifier initialiser?
 ;

/// Initialiser :
///     = AssignmentExpression
initialiser
 : '=' singleExpression
 ;

/// EmptyStatement :
///     ;
emptyStatement
 : SemiColon
 ;

/// ExpressionStatement :
///     [lookahead ? {{, function}] Expression ;
expressionStatement
 : singleExpression SemiColon
 ;

/// IfStatement :
///     if ( Expression ) Statement else Statement
///     if ( Expression ) Statement
ifStatement
 : If '(' singleExpression ')' statement ( Else statement )?
 ;

/// IterationStatement :
///     do Statement while ( Expression );
///     while ( Expression ) Statement
///     for ( Expression? ; Expression? ; Expression? ) Statement
///     for ( var VariableDeclarationList ; Expression? ; Expression? ) Statement
///     for ( LeftHandSideExpression in Expression ) Statement
///     for ( var VariableDeclaration in Expression ) Statement
iterationStatement
 : Do statement While '(' singleExpression ')' eos                                                 # DoStatement
 | While '(' singleExpression ')' statement                                                        # WhileStatement
 | For '(' Var Identifier '=' singleExpression ';' Identifier '<'  singleExpression ';' 
 Identifier '++' ')' statement                                                                       # SimpleForStatement
 | For '(' singleExpression? ';' singleExpression? ';' singleExpression? ')' statement         # ForStatement
 | For '(' Var variableDeclarationList ';' singleExpression? ';' singleExpression? ')' statement # ForVarStatement
 | For '(' singleExpression In singleExpression ')' statement                                      # ForInStatement
 | For '(' Var variableDeclaration In singleExpression ')' statement                               # ForVarInStatement
 ;

/// ReturnStatement :
///     return ;
///     return [no LineTerminator here] Expression ;
returnStatement
 : Return singleExpression? eos
 ;

/// FunctionDeclaration :
///     function Identifier ( FormalParameterList? ) { FunctionBody }
functionDeclaration
 : Function Identifier '(' formalParameterList? ')' '{' functionBody '}'
 ;

/// FormalParameterList :
///     Identifier
///     FormalParameterList , Identifier
formalParameterList
 : Identifier ( ',' Identifier )*
 ;

/// FunctionBody :
///     SourceElements?
functionBody
 : sourceElements?
 ;
    
/// ArrayLiteral :
///     [ Elision? ]
///     [ ElementList ]
///     [ ElementList , Elision? ]
arrayLiteral
 : '[' elementList? /* ','? elision? */ ']'
 ;

/// ElementList :
///     Elision? AssignmentExpression
///     ElementList , Elision? AssignmentExpression
elementList
 : /* elision? */ singleExpression ( ',' /* elision? */ singleExpression )*
 ;

/// Arguments :
///     ( )
///     ( ArgumentList )
arguments
 : '(' argumentList? ')'
 ;
    
/// ArgumentList :
///     AssignmentExpression
///     ArgumentList , AssignmentExpression
argumentList
 : singleExpression ( ',' singleExpression )*
 ;
    
/// Expression :
///     AssignmentExpression
///     Expression , AssignmentExpression
///
/// AssignmentExpression :
///     ConditionalExpression
///     LeftHandSideExpression = AssignmentExpression
///     LeftHandSideExpression AssignmentOperator AssignmentExpression
///
/// ConditionalExpression :
///     LogicalORExpression
///     LogicalORExpression ? AssignmentExpression : AssignmentExpression
///
/// LogicalORExpression :
///     LogicalANDExpression
///     LogicalORExpression || LogicalANDExpression
///
/// LogicalANDExpression :
///     BitwiseORExpression
///     LogicalANDExpression && BitwiseORExpression
///
/// BitwiseORExpression :
///     BitwiseXORExpression
///     BitwiseORExpression | BitwiseXORExpression
///
/// BitwiseXORExpression :
///     BitwiseANDExpression
///     BitwiseXORExpression ^ BitwiseANDExpression
///
/// BitwiseANDExpression :
///     EqualityExpression
///     BitwiseANDExpression & EqualityExpression
///
/// EqualityExpression :
///     RelationalExpression
///     EqualityExpression == RelationalExpression
///     EqualityExpression != RelationalExpression
///     EqualityExpression === RelationalExpression
///     EqualityExpression !== RelationalExpression
///
/// RelationalExpression :
///     ShiftExpression
///     RelationalExpression < ShiftExpression
///     RelationalExpression > ShiftExpression
///     RelationalExpression <= ShiftExpression
///     RelationalExpression >= ShiftExpression
///     RelationalExpression instanceof ShiftExpression 
///     RelationalExpression in ShiftExpression
///
/// ShiftExpression :
///     AdditiveExpression
///     ShiftExpression << AdditiveExpression
///     ShiftExpression >> AdditiveExpression
///     ShiftExpression >>> AdditiveExpression
/// 
/// AdditiveExpression :
///     MultiplicativeExpression
///     AdditiveExpression + MultiplicativeExpression
///     AdditiveExpression - MultiplicativeExpression
///
/// MultiplicativeExpression :
///     UnaryExpression
///     MultiplicativeExpression * UnaryExpression
///     MultiplicativeExpression / UnaryExpression
///     MultiplicativeExpression % UnaryExpression
///
/// UnaryExpression :
///     PostfixExpression
///     delete UnaryExpression
///     void UnaryExpression
///     typeof UnaryExpression
///     ++ UnaryExpression
///     -- UnaryExpression
///     + UnaryExpression
///     - UnaryExpression
///     ~ UnaryExpression
///     ! UnaryExpression
///
/// PostfixExpression :
///     LeftHandSideExpression
///     LeftHandSideExpression [no LineTerminator here] ++
///     LeftHandSideExpression [no LineTerminator here] --
///
/// LeftHandSideExpression :
///     NewExpression
///     CallExpression
///
/// CallExpression :
///     MemberExpression Arguments
///     CallExpression Arguments
///     CallExpression [ Expression ]
///     CallExpression . IdentifierName
///
/// NewExpression :
///     MemberExpression
///     new NewExpression
///
/// MemberExpression :
///     PrimaryExpression
///     FunctionExpression
///     MemberExpression [ Expression ]
///     MemberExpression . IdentifierName
///     new MemberExpression Arguments
///
/// FunctionExpression :
///     function Identifier? ( FormalParameterList? ) { FunctionBody }
///
/// PrimaryExpression :
///     this
///     Identifier
///     Literal
///     ArrayLiteral
///     ObjectLiteral
///     ( Expression )
///

singleExpression // mb: oversimplified to begin with
 : Identifier '.' Identifier arguments                              # MethodExpression
 | Identifier arguments                                                 # FunctionExpression
// : Function Identifier? '(' formalParameterList? ')' '{' functionBody '}' # FunctionExpression
// | singleExpression '[' expressionSequence ']'                            # MemberIndexExpression
 | singleExpression '.' Identifier                                    # MemberDotExpression
// | singleExpression arguments                                             # ArgumentsExpression
// | New singleExpression arguments?                                        # NewExpression
// | singleExpression /* {!here(LineTerminator)}? */ '++'                   # PostIncrementExpression
// | singleExpression /* {!here(LineTerminator)}? */ '--'                   # PostDecreaseExpression
// | Delete singleExpression                                                # DeleteExpression
// | Void singleExpression                                                  # VoidExpression
// | Typeof singleExpression                                                # TypeofExpression
// | '++' singleExpression                                                  # PreIncrementExpression
// | '--' singleExpression                                                  # PreDecreaseExpression
// | '+' singleExpression                                                   # UnaryPlusExpression
// | '-' singleExpression                                                   # UnaryMinusExpression
// | '~' singleExpression                                                   # BitNotExpression
 | '!' singleExpression                                                   # NotExpression
 | singleExpression ( '*' | '/' | '%' ) singleExpression                  # MultiplicativeExpression
 | singleExpression ( '+' | '-' ) singleExpression                        # AdditiveExpression
// | singleExpression ( '<<' | '>>' | '>>>' ) singleExpression              # BitShiftExpression
 | singleExpression ( '<' | '>' | '<=' | '>=' ) singleExpression          # RelationalExpression
// | singleExpression Instanceof singleExpression                           # InstanceofExpression
// | singleExpression In singleExpression                                   # InExpression
 | singleExpression ( '==' | '!=' | '===' | '!==' ) singleExpression      # EqualityExpression
// | singleExpression '&' singleExpression                                  # BitAndExpression
// | singleExpression '^' singleExpression                                  # BitXOrExpression
// | singleExpression '|' singleExpression                                  # BitOrExpression
 | singleExpression '&&' singleExpression                                 # LogicalAndExpression
 | singleExpression '||' singleExpression                                 # LogicalOrExpression
// | singleExpression '?' singleExpression ':' singleExpression             # TernaryExpression
// | singleExpression '=' expressionSequence                                # AssignmentExpression
 | Identifier '=' singleExpression                                        # AssignmentExpression
// | singleExpression assignmentOperator expressionSequence                 # AssignmentOperatorExpression
// | This                                                                   # ThisExpression
 | Identifier                                                             # IdentifierExpression
 | literal                                                                # LiteralExpression
 | arrayLiteral                                                           # ArrayLiteralExpression
// | objectLiteral                                                          # ObjectLiteralExpression
 | '(' singleExpression ')'                                             # ParenthesizedExpression
 ;

/// AssignmentOperator : one of
///     *=	/=	%=	+=	-=	<<=	>>=	>>>=	&=	^=	|=
assignmentOperator
 : '*=' 
 | '/=' 
 | '%=' 
 | '+=' 
 | '-=' 
 | '<<=' 
 | '>>=' 
 | '>>>=' 
 | '&=' 
 | '^=' 
 | '|='
 ;

literal // mb: no strings and no regex
// :  NullLiteral 
 : BooleanLiteral
// | StringLiteral
// | RegularExpressionLiteral
 | numericLiteral
 ;

numericLiteral // mb: only decimal literals
 : DecimalLiteral
// | HexIntegerLiteral
// | OctalIntegerLiteral
 ;


eos
 : SemiColon
 | EOF
 ;

/// 7.3 Line Terminators
LineTerminator
 : [\r\n] -> channel(HIDDEN)
 ;

OpenBracket                : '[';
CloseBracket               : ']';
OpenParen                  : '(';
CloseParen                 : ')';
OpenBrace                  : '{';
CloseBrace                 : '}';
SemiColon                  : ';';
Comma                      : ',';
Assign                     : '=';
QuestionMark               : '?';
Colon                      : ':';
Dot                        : '.';
PlusPlus                   : '++';
MinusMinus                 : '--';
Plus                       : '+';
Minus                      : '-';
BitNot                     : '~';
Not                        : '!';
Multiply                   : '*';
Divide                     : '/';
Modulus                    : '%';
RightShiftArithmetic       : '>>';
LeftShiftArithmetic        : '<<';
RightShiftLogical          : '>>>';
LessThan                   : '<';
MoreThan                   : '>';
LessThanEquals             : '<=';
GreaterThanEquals          : '>=';
Equals                     : '==';
NotEquals                  : '!=';
IdentityEquals             : '===';
IdentityNotEquals          : '!==';
BitAnd                     : '&';
BitXOr                     : '^';
BitOr                      : '|';
And                        : '&&';
Or                         : '||';
MultiplyAssign             : '*=';
DivideAssign               : '/='; 
ModulusAssign              : '%='; 
PlusAssign                 : '+='; 
MinusAssign                : '-='; 
LeftShiftArithmeticAssign  : '<<='; 
RightShiftArithmeticAssign : '>>='; 
RightShiftLogicalAssign    : '>>>='; 
BitAndAssign               : '&='; 
BitXorAssign               : '^='; 
BitOrAssign                : '|=';

/// 7.8.1 Null Literals
NullLiteral
 : 'null'
 ;

/// 7.8.2 Boolean Literals
BooleanLiteral
 : 'true'
 | 'false'
 ;

/// 7.8.3 Numeric Literals
DecimalLiteral
 : DecimalIntegerLiteral '.' DecimalDigit* ExponentPart?
 | '.' DecimalDigit+ ExponentPart?
 | DecimalIntegerLiteral ExponentPart?
 ;

/// 7.8.3 Numeric Literals
HexIntegerLiteral
 : '0' [xX] HexDigit+
 ;

/// 7.6.1.1 Keywords
Break      : 'break';
Do         : 'do';
Instanceof : 'instanceof';
Typeof     : 'typeof';
Case       : 'case';
Else       : 'else';
New        : 'new';
Var        : 'var';
Catch      : 'catch';
Finally    : 'finally';
Return     : 'return';
Void       : 'void';
Continue   : 'continue';
For        : 'for';
Switch     : 'switch';
While      : 'while';
Debugger   : 'debugger';
Function   : 'function';
This       : 'this';
With       : 'with';
Default    : 'default';
If         : 'if';
Throw      : 'throw';
Delete     : 'delete';
In         : 'in';
Try        : 'try';

/// 7.6.1.2 Future Reserved Words
Class   : 'class';
Enum    : 'enum';
Extends : 'extends';
Super   : 'super';
Const   : 'const';
Export  : 'export';
Import  : 'import';

/// The following tokens are also considered to be FutureReservedWords 
/// when parsing strict mode  
Implements : /* {strictMode}? */ 'implements';
Let        : /* {strictMode}? */ 'let';
Private    : /* {strictMode}? */ 'private';
Public     : /* {strictMode}? */ 'public';
Interface  : /* {strictMode}? */ 'interface';
Package    : /* {strictMode}? */ 'package';
Protected  : /* {strictMode}? */ 'protected';
Static     : /* {strictMode}? */ 'static';
Yield      : /* {strictMode}? */ 'yield';

/// 7.6 Identifier Names and Identifiers
Identifier
 : IdentifierStart IdentifierPart*
 ;

WhiteSpaces
 : [\t\ ]+ -> channel(HIDDEN)
 ;

/// 7.4 Comments
MultiLineComment
 : '/*' .*? '*/' -> channel(HIDDEN)
 ;

SingleLineComment
 : '//' ~[\r\n]* -> channel(HIDDEN)
 ;

UnexpectedCharacter
 : .
 ;

fragment DecimalDigit
 : [0-9]
 ;
fragment HexDigit
 : [0-9a-fA-F]
 ;
fragment OctalDigit
 : [0-7]
 ;
fragment DecimalIntegerLiteral
 : '0'
 | [1-9] DecimalDigit*
 ;
fragment ExponentPart
 : [eE] [+-]? DecimalDigit+
 ;
fragment IdentifierStart
 : [$_a-zA-Z]
 ;
fragment IdentifierPart
 : IdentifierStart
 | DecimalDigit
 ;
