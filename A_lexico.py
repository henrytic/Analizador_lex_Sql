import ply.lex as lex

tokens = [
    "TOK_SELECT",
    "TOK_FROM",
    "TOK_WHERE",
    "TOK_AND",
    "TOK_OR",
    "TOK_NOT",
    "TOK_IN",
    "TOK_BETWEEN",
    "TOK_LIKE",
    "TOK_DISTINCT",
    "TOK_AS",
    "TOK_JOIN",
    "TOK_ON",
    "TOK_INNER",
    "TOK_OUTER",
    "TOK_LEFT",
    "TOK_RIGHT",
    "TOK_FULL",
    "TOK_ORDER",
    "TOK_BY",
    "TOK_ASC",
    "TOK_DESC",
    "TOK_LIMIT",
    "TOK_OFFSET",
    "TOK_COMMA",
    "TOK_DOT",
    "TOK_EQ",
    "TOK_NEQ",
    "TOK_GT",
    "TOK_LT",
    "TOK_GE",
    "TOK_LE",
    "TOK_PLUS",
    "TOK_MINUS",
    "TOK_MUL",
    "TOK_DIV",
    "TOK_MOD",
    "TOK_ID",
    "TOK_NUM",
    "TOK_STRING",
    "TOK_NULL",
    "TOK_SIGNO"
]

t_ignore = " \t"

def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'
    t.type = "TOK_SELECT"
    return t

def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'
    t.type = "TOK_FROM"
    return t
def t_SIGNO(t):
    r',|<'
    t.type="TOK_SIGNO"
    return t
def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    t.type = "TOK_WHERE"
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = "TOK_ID"
    return t
def t_NUM(t):
    r'[0-9]+'
    t.type = "TOK_NUM"
    return t
def t_EQ(t):
    r'='
    t.type = "TOK_EQ"
    return t
def t_error(t):
    print("no te conozco '%s'" % t.value[0])
    t.lexer.skip(1)
def print_token(tok):
    if tok.type == "TOK_SELECT":
        print("Palabra Clave:", tok.value)
    elif tok.type == "TOK_FROM":
        print("Palabra Clave:", tok.value)
    elif tok.type == "TOK_WHERE":
        print("Palabra Clave:", tok.value)
    elif tok.type == "TOK_ID":
        print("Identificador:", tok.value)
    elif tok.type == "TOK_NUM":
        print("Numero:", tok.value)
    elif tok.type == "TOK_EQ":
        print("OPREL:", tok.value)
    elif tok.type == "TOK_SIGNO":
        print("SIGNO:", tok.value)
    else:
        print("Token desconocido:", tok.type, tok.value)

lexer = lex.lex()

def main():
    data = "SELEcT name FroM table2 WHEre a2 = 15 ;"
    #data = "SELECT col1, col2 from mi_Tabla wHERE col1 < 20"
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print_token(tok)

if __name__ == "__main__":
    main()
