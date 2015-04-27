
java -cp ..\..\..\antlr-4.5\antlr-4.5-complete.jar;%CLASSPATH% org.antlr.v4.Tool -Dlanguage=Python2 -listener -visitor XmlLexer.g4 XmlParser.g4