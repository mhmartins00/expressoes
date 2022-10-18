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

# REGEX PARA VALIDACOES
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
    r'^(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|printf)$'
    return t

def t_PALAVRA( t ) :
    r'^[a-zA-ZÀ-ÿ]+$'
    return t

def t_NUMERO_REAL( t ) :
    r'^[0-9]+[.][0-9]+$'
    return t

def t_TAG_HTML( t ) :
    r'^<[a-zA-Z0-9 -_./:=&"%+?@\$! \s]+>?$'
    return t

def t_error( t ):
  print("Invalid Token:",t.value)
  t.lexer.skip( 1 )

lexer = lex.lex()

def p_celular( p ):
    'expr : CELULAR'
    p[0] = f'CELULAR VÁLIDO'

def p_cpf( p ):
    'expr : CPF'
    p[0] = f'CPF VÁLIDO'

def p_placa( p ):
    'expr : PLACA'
    p[0] = f'PLACA VÁLIDA'

def p_url( p ):
    'expr : URL'
    p[0] = f'URL VÁLIDA'

def p_cnpj( p ):
    'expr : CNPJ'
    p[0] = f'CNPJ VÁLIDO'

def p_palavra_reservada_c( p ):
    'expr : PALAVRA_RESERVADA_C'
    p[0] = f'PALAVRA RESERVADA DA LINGUAGEM C'

def p_palavra( p ):
    'expr : PALAVRA'
    p[0] = f'PALAVRA VÁLIDA'

def p_numero_real( p ):
    'expr : NUMERO_REAL'
    p[0] = f'NUMERO REAL VÁLIDO'

def p_tag_html( p ):
    'expr : TAG_HTML'
    p[0] = f'TAG HTML VÁLIDA'

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

print("#---------------------------#")
print("|     Testes de tokens      |")
print("#---------------------------#\n\n")
resTelefoneCelular = parser.parse("51993005511")
print(f"TelefoneCelular = {resTelefoneCelular}")
print("\n")
resPlaca = parser.parse("ILP5577")
print(f"Placa = {resPlaca}")
print("\n")
resCpf = parser.parse("031.789.780-24")
print(f"CPF = {resCpf}")
print("\n")
resNumerosReais = parser.parse("456.33333")
print(f"NumerosReais = {resNumerosReais}")
print("\n")
resTagsHtml = parser.parse("<p>")
print(f"TagsHTML = {resTagsHtml}")
print("\n")
resUrl = parser.parse("https://abc.com")
print(f"URL = {resUrl}")
print("\n")
resPalavras = parser.parse("éDeCasa")
print(f"Palavras = {resPalavras}")
print("\n")
resCnpj = parser.parse("01234567890123")
print(f"CNPJ = {resCnpj}")
print("\n")
resIdC = parser.parse("int")
print(f"IdC = {resIdC}")
print("\n")
