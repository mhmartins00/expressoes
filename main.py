import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'CPF',
    'CELULAR',
    'PLACA',
    'URL',
    'CNPJ',
    'PALAVRA_RESERVADA_C',
    'PALAVRA',
    'NUMERO_REAL',
    'TAG_HTML'
)

# t_CELULAR = r'^[0-9]{2}9[0-9]{8}$'
# t_CPF = r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'
# t_PLACA = r'^[a-zA-Z]{3}[0-9]{4}$'
# t_URL = r'^([hH][tT][tT][pP][sS]?[:][\\/]{2})+([a-zA-Z0-9 -_./:=&"%+?@\$!])+$'
# t_CNPJ = r'^[0-9]{14}$'
# t_PALAVRA_RESERVADA_C = r'^(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|printf)$'
# t_PALAVRA = r'^[a-zA-ZÀ-ÿ \s]+$'
# t_NUMERO_REAL = r'^[0-9]+.[0-9]+$'
# t_TAG_HTML =r'^<[a-zA-Z0-9 -_./:=&"%+?@\$! \s]+>$'

t_ignore = ' \t'

def t_CELULAR( t ) :
    r'^[0-9]{2}9[0-9]{8}$'
    return t

def t_CPF( t ) :
    r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'
    # print(f"valor de t_CPF = {t} t.value = {t.value}")
    return t

def t_PLACA( t ) :
    r'^[a-zA-Z]{3}[0-9]{4}$'
    return t

def t_URL( t ) :
    r'^([hH][tT][tT][pP][sS]?[:][\\/]{2})+([a-zA-Z0-9 -_./:=&"%+?@\$!])+$'
    return t

def t_CNPJ( t ) :
    r'^[0-9]{14}$'
    return t

def t_PALAVRA_RESERVADA_C( t ) :
    r'^(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|printf)$' #Validar necessidade do \s que corresponde ao whitespace
    return t

def t_PALAVRA( t ) :
    r'^[a-zA-ZÀ-ÿ \s]+$' #Validar necessidade do \s que corresponde ao whitespace
    return t

def t_NUMERO_REAL( t ) :
    r'^[0-9]+.[0-9]+$' #Validar necessidade do \s que corresponde ao whitespace
    return t

def t_TAG_HTML( t ) :
    r'^<[a-zA-Z0-9 -_./:=&"%+?@\$! \s]+>$' #Validar necessidade do \s que corresponde ao whitespace
    return t

# def t_newline( t ):
#   r'\n+'
#   print("t_newline")
#   t.lexer.lineno += len( t.value 

def t_error( t ):
  print("Invalid Token:",t.value)
  t.lexer.skip( 1 )

lexer = lex.lex()

def p_celular( p ):
    'expr : CELULAR'
    p[0] = f'CELULAR VÁLIDO'
    # print(f"CPF = {p}")

def p_cpf( p ):
    'expr : CPF'
    p[0] = f'CPF VÁLIDO'
    # print(f"CPF = {p}")

def p_placa( p ):
    'expr : PLACA'
    p[0] = f'PLACA VÁLIDA'
    # print(f"CPF = {p}")

def p_cnpj( p ):
    'expr : CNPJ'
    p[0] = f'CNPJ VÁLIDO'
    # print(f"CPF = {p}")

def p_palavra_reservada_c( p ):
    'expr : PALAVRA_RESERVADA_C'
    p[0] = f'PALAVRA RESERVADA DA LINGUAGEM C'
    # print(f"CPF = {p}")

def p_palavra( p ):
    'expr : PALAVRA'
    p[0] = f'PALAVRA VÁLIDA'
    # print(f"CPF = {p}")

def p_numero_real( p ):
    'expr : NUMERO_REAL'
    p[0] = f'NUMERO REAL VÁLIDO'
    # print(f"CPF = {p}")

def p_tag_html( p ):
    'expr : TAG_HTML'
    p[0] = f'TAG HTML VÁLIDA'
    # print(f"CPF = {p}")

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

res = parser.parse("ASD6676")
print(f"RES = {res}")
