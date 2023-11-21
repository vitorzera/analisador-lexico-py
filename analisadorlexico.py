import re

def analiseLexica():
    f = open("calculadoraBasica.c", "r")  # Abre o arquivo para leitura
    lines = f.readlines()

    tokens = {}
    qtdLines = 1
    identificador_count = 150

    for line in lines:
        line = re.sub("{", " {", line)
        line = re.sub(";", " ;", line)
        line = re.sub(",", " ,", line)
        line = re.sub("=", " = ", line)
        line = re.sub("[ ]{2,}", " ", line)
        if line.strip() != '':
            line = line.strip()

            if re.search("^#include <.*[.]h>$", line):
                line = line.split()
                tokens[(line[0], qtdLines)] = 150  # Palavra reservada
                biblioteca = re.sub("(<|>)", "", line[1])
                tokens[(biblioteca, qtdLines)] = identificador_count
                identificador_count += 1  # Biblioteca
            elif re.search("^int main\\(\\)( {|)$", line):
                line = line.split()
                tokens[(line[0], qtdLines)] = 150  # Palavra reservada
                tokens[(line[1], qtdLines)] = 150  # Palavra reservada
                if len(line) == 3:
                    tokens[(line[2], qtdLines)] = 151  # Delimitador de início
            elif line == "{":
                tokens[(line, qtdLines)] = 151  # Delimitador de início
            elif line == "}":
                tokens[(line, qtdLines)] = 152  # Delimitador de fim
            else:
                aux = line
                line = line.split()
                for i in line:
                    if i == "int" or i == "return":
                        tokens[(i, qtdLines)] = 150  # Palavra reservada
                    elif i == "=":
                        tokens[(i, qtdLines)] = 153  # Comando de atribuição
                    elif i == "+":
                        tokens[(i, qtdLines)] = 154  # Operador de adição
                    elif i == "*":
                        tokens[(i, qtdLines)] = 155  # Operador de multiplicação
                    elif i == ";":
                        tokens[(i, qtdLines)] = 156  # Finalizador de linha
                    elif re.search("^[a-zA-Z]{1,}[0-9]*$", i):
                        tokens[(i, qtdLines)] = identificador_count
                        identificador_count += 1  # Nome de variável
                    elif re.search("^[0-9]{1,}$", i):
                        tokens[(i, qtdLines)] = 157  # Constante numérica
                    elif i == ",":
                        tokens[(i, qtdLines)] = 158  # Separador
                    else:
                        if i == "#include":
                            i = aux
                        print("O token '" + i + "' na linha " + str(qtdLines) + " é inválido")
                        return
        qtdLines += 1

    with open("output.txt", "w") as output_file:
        for key in tokens:
            output_file.write(str(key[1]) + ": " + str(tokens[key]) + " - " + str(key[0]) + "\n")

def main():
    analiseLexica()

main()
