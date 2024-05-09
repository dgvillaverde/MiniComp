import ply.lex as lex
import ply.yacc as yacc

#Tokens
tokens = [
    'PLUS','MINUS','TIMES','DIVIDE',
    'ID','EQUAL','GREATER_THAN','LESS_THAN',
    'NOTEQUAL','LPARENT','RPARENT','LBRACE','RBRACE',
    'CTEI','CTEF', 'CTES', 'COMMA','SEMICOLON','COLON', 'STRING',
    'PROGRAM', 'PRINT', 'IF', 'ELSE', 'VAR', 'INT', 'FLOAT', 'VOID',
    'WHILE', 'DO'
]

#Expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_EQUAL = r'\='
t_NOTEQUAL = r'\<>'
t_GREATER_THAN = r'>'
t_SMALLER_THAN = r'<'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r':'
t_CTESTRING = r'\".*\"'

#ID
def t_ID(t):
    r'[a-zA-Z]([a-zA-Z]|[0-9])*'
    t.type = keywords.get(t.value, 'ID')
    return t

#Expresion regular para constante float
def t_CTEF(t):
    r'[0-9]*\.[0-9]+[0-9]+'
    t.value = float(t.value)
    return t

#Expresion regular para constante int
def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

keywords = {
    'program': 'PROGRAM',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'void': 'VOID',
    'while': 'WHILE',
    'do': 'DO',
}

#Gramatica 

def p_program(p):
    '''
    Programa: PROGRAM ID SEMICOLON Dev_V Dec_F MAIN Body END
    '''

def p_dev_v_epsilon(p):
    '''
    Dev_V : EPSILON
    '''

    pass