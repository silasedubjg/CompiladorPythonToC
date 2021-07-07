from lexema import *

frase = input("digite uma frase para compilar :")
vetor = frase.split(' ')

reservadas = ["sinh","sqrt","fabs","log10","pow","log",
           "ceil","tanh","atam","tan","asm","auto",
           "break","case","char","const","continue",
           "default","do","double","else","enum","extern",
           "float","for","goto","if","int","long","register",
           "return","short","sizeof","static","struct","switch",
           "typedef","union","void","while","for"]

operadores =["::", "(tipo)",".*","throw", "c?t:f"]

atribuidor = ["|=", "^=","*=","/=", "%=","+=","-=","=","<<=" ,">>=","&="]

relacionais = [">", "<", ">="," <="," ==", "!="]

aritmetico = ["++","--","+", "-","*", "/", "%"]

logico = ["&&", "||","!"]

Bitabit = ["&", "|", "^", "~", ">>", "<<"]

separadores = [",",";","(",")","[","]"]

agrupamento = ["()", "[]" ,"->" ,"." ]

analisador = []

cont = 0

for palavra in vetor:
    for expressao in relacionais:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador relacional")
            analisador.append(expressao)
            cont = 1
        
    for expressao in agrupamento:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador de agrupamento")
            analisador.append(expressao)
            cont = 1
    for expressao in separadores:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador de separação")
            analisador.append(expressao)
            cont = 1
    for expressao in Bitabit:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador Bit a bit")
            analisador.append(expressao)
            cont = 1
    for expressao in logico:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador lógico")
            analisador.append(expressao)
            cont = 1
    for expressao in reservadas:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," palavra reservada")
            analisador.append(expressao)
            cont = 1
    for expressao in operadores:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador")
            analisador.append(expressao)
            cont = 1
    for expressao in atribuidor:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador de atribuição")
            analisador.append(expressao)
            cont = 1
    for expressao in aritmetico:
        if palavra == expressao:
            expressao = lexema()
            expressao.criar(palavra," operador aritmético")
            analisador.append(expressao)
            cont = 1
    if palavra.isdigit():
            inteiro = lexema()
            inteiro.criar(palavra," número inteiro")
            analisador.append(inteiro)
            cont = 1
    else:
        try:
            float(palavra)
            decimal = lexema()
            decimal.criar(palavra," número decimal")
            analisador.append(decimal)
            cont = 1
        except :
            pass   
    if cont == 0:
        teste = list(palavra)
        primeiraletra= teste[0]
        if primeiraletra.isalpha():
            ndef = lexema()
            ndef.criar(palavra," identificador")
            analisador.append(ndef)
            cont = 1
     
        else:
            ndef = lexema()
            ndef.criar(palavra," Não é uma expressão conhecida")
            analisador.append(ndef)
            cont = 1
    cont = 0
string = 'ola'
string.isdecimal

for palavra in analisador:
    print('Lexema: '+"'"+palavra.lex+"'"+' Tipo: '+palavra.tipo)