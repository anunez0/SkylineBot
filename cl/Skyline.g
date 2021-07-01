grammar Skyline;

root : start EOF ;

start : (identifier ':=')? skyline ;

identifier : IDENTIFIER ;

skyline : priority1 ;

priority1 : priority2 ('+' priority2 | ('+' | '-') NUMBER)* ;

priority2 : priority3 ('*' (priority3 | NUMBER))* ;

priority3 : '-'? priority4 ;

priority4 : '(' skyline ')' | identifier | building | composed | random ;

building : '(' NUMBER ',' NUMBER ',' NUMBER ')' ;

composed : '[' building (',' building)* ']' ;

random : '{' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER '}' ;

IDENTIFIER : LETTER (LETTER | DIGIT)* ;
NUMBER : '-'? DIGIT+ ;
LETTER : [a-zA-Z] ;
DIGIT : [0-9] ;
WS : [ \n]+ -> skip ;
