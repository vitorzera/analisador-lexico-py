# analisador-lexico-py
Analisador Léxico desenvolvido em python para ler arquivos da linguagem C.

## Id dos Tokens
Palavra reservada (150): Representa palavras reservadas como "int" e "return".

Biblioteca (151+): Representa bibliotecas incluídas com #include <...>.

Delimitador de início (151): Indica o início de um bloco de código, como em int main() {.

Delimitador de fim (152): Indica o fim de um bloco de código, como em }.

Comando de atribuição (153): Representa o operador de atribuição "=".

Operador de adição (154): Representa o operador de adição "+".

Operador de multiplicação (155): Representa o operador de multiplicação "*".

Finalizador de linha (156): Representa o ponto e vírgula que termina uma instrução.

Constante numérica (157): Representa números inteiros.

Nome de variável (identificador_count): Representa nomes de variáveis, sendo atribuído um número único a cada identificador.

Separador (158): Representa a vírgula utilizada como separador em listas ou declarações.

