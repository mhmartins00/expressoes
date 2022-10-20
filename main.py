#  README
#  Para executar basta estar no mesmo diretório do arquivo main.py e digitar > python main.py.
# 1) número de telefone celular = 00900000000 [obrigatorio o comeco com o 9]
# 2) placas de carro = xxx0000 | XXX000 [3 letras seguidas por 4 numeros]
# 3) cpf = 123.456.789-01 [qualquer numero 11 digitos mas com mascara] 
# 4) números reais = 123.5555555 [de qualquer tamanho]
# 5) tags html = <qualquer_coisa INCLUSIVE com espaço = @>
# 6) URL de páginas = HTTP:// | http:// | HTTPS:// | https:// [qualquer coisa seguida]
# 7) palavras = aass ou AAAS ou asAD [sem numeros e simbolos mas com acentos]
# 8) cnpj = 12345678901234 [qualquer numero 14 digitos sem mascara]
# 9) identificadores ling. C = [ids do C int, float, etc...]

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

# Definicao das funcoes com as expressoes regulares
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
    r'^(alignas|alignof|and|and_eq|asm|auto|bitand|bitor|bool|break|case|catch|char|chr8_t|char16_t|char32_t|class|compl|concept|const|const_cast|consteval|constexpr|constinit|continue|co_await|co_return|co_yield|decltype|default|delete|do|doube|dynamic_cast|else|enum|explicit|export|extern|false|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|noexcept|not|not_eq|nullptr|operator|or|or_eq|private|protected|public|register reinterpret_cast|requires|return|short|signed|sizeof|static|static_assert|statc_cast|struct|switch|template|this|thread_local|throw|true|try|typedef|typeid|tpename|union|unsigned|using|virtual|void|volatile|wchar_t|while|xor|xor_eq|printf)$'
    return t

def t_PALAVRA( t ) :
    r'^[a-zA-ZÀ-ÿ]+$'
    return t

def t_NUMERO_REAL( t ) :
    r'^[0-9]+[.][0-9]+$'
    return t

def t_TAG_HTML( t ) :
    r'^[<]+(.*?)+[>]$'
    return t

def t_error( t ):
  t.lexer.skip( 1 )

lexer = lex.lex()

# Definição das funcoes para validacao de tokens
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
    print("Token inválido")

parser = yacc.yacc()

# Digitar tokens para validar no console
escape = ""
print("#---------------------------#")
print("|     Testes de tokens      |")
print("|                           |")
print("| *Para sair digite 's'     |")
print("#---------------------------#\n")
while escape != "s":
    token = input("Digite o token: ")
    res = parser.parse(token)
    print(f"Token = {res}")
    print("_________________________________________\n")
    escape = input("Parar? [s / n]: ")
    print("_________________________________________\n")


# Inicio dos testes de desenvolvimento

# print("#---------------------------#")
# print("|     Testes de tokens      |")
# print("#---------------------------#\n\n")
# resTelefoneCelular = parser.parse("51993005511")
# print(f"TelefoneCelular = {resTelefoneCelular}")
# resTelefoneCelular = parser.parse("51787535135")
# print(f"Invalid TelefoneCelular = {resTelefoneCelular}")
# print("_________________________________________\n")
# resPlaca = parser.parse("ILP5577")
# print(f"Placa = {resPlaca}")
# resPlaca = parser.parse("I5P6987")
# print(f"Invalid Placa = {resPlaca}")
# print("_________________________________________\n")
# resCpf = parser.parse("031.789.780-24")
# print(f"CPF = {resCpf}")
# resCpf = parser.parse("03178978024")
# print(f"Invalid CPF = {resCpf}")
# print("_________________________________________\n")
# resNumerosReais = parser.parse("456.33333")
# print(f"NumerosReais = {resNumerosReais}")
# resNumerosReais = parser.parse("45633333")
# print(f"Invalid NumerosReais = {resNumerosReais}")
# print("_________________________________________\n")
# resTagsHtml = parser.parse("<p>")
# print(f"TagsHTML = {resTagsHtml}")
# resTagsHtml = parser.parse("<p")
# print(f"Invalid TagsHTML = {resTagsHtml}")
# print("_________________________________________\n")
# resUrl = parser.parse("https://abc.com")
# print(f"URL = {resUrl}")
# resUrl = parser.parse("htts://as.com.br")
# print(f"Invalid URL = {resUrl}")
# print("_________________________________________\n")
# resPalavras = parser.parse("éDeCasa")
# print(f"Palavras = {resPalavras}")
# resPalavras = parser.parse("é de casa")
# print(f"Invalid Palavras = {resPalavras}")
# print("_________________________________________\n")
# resCnpj = parser.parse("01234567890123")
# print(f"CNPJ = {resCnpj}")
# resCnpj = parser.parse("0123456789012")
# print(f"Invalid CNPJ = {resCnpj}")
# print("_________________________________________\n")
# resIdC = parser.parse("int")
# print(f"IdC = {resIdC}")
# #nao reconhece como identificador do C, mas como uma palavra valida
# resIdC = parser.parse("inteiro")
# print(f"Invalid IdC = {resIdC}")
# print("_________________________________________\n")
