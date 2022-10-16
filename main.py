import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'CPF',
    'MINUS',
    'NUMBER',
    'POINT',
)

t_ignore = ' \t'

t_MINUS   = r'-'
t_POINT   = r'\.'

# def t_NUMBER( t ) :
#     r'[0-9]{3}'
#     # t.value = int( t.value )
#     print("t_NUMBER")
#     print(f"valor de t = {t} t.value = {t.value} t.lineno = {t.lineno}")
#     return t

def t_CPF( t ) :
    r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'
    if t.value == 0:
        t.value = 0
    print(f"valor de t_CPF = {t} t.value = {t.value}")
    return t


def t_newline( t ):
  r'\n+'
  print("t_newline")
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  print("t_error")
  t.lexer.skip( 1 )

lexer = lex.lex()

# precedence = (
#     ( 'left', 'PLUS', 'MINUS' ),
#     ( 'left', 'TIMES', 'DIV' ),
# )

def p_cpf( p ):
    'expr : CPF'
    p[0] = f'{p[1]}'
    print(f"CPF = {p}")


def p_error( p ):
    print("Syntax error in input!")
    # print("p_error")


parser = yacc.yacc()

res = parser.parse("133.263.80110-61")
print(f"RES = {res}")
