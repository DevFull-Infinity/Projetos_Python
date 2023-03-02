# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system,name

# Board (tabuleiro)


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:
    # Cria os constructos que serão usados pelos metodos da classe.
    def __init__(self, palavra):
        self.word = palavra
        self.Plc = []
        self.Plw = []

    # Se a letra digitada pelo usuário na forma maiscula ou minuscula estiver na palavra e não estiver na lista Plc(construct) append.
    # Se a letra digitada pelo usuário na forma maiscula ou minuscula NÃO estiver na palavra e NÃO estiver na lista Plw(construct) append.
    def parameters_c_w(self, letrax):
        if (letrax.lower() in self.word or letrax.upper() in self.word) and letrax not in self.Plc:
            self.Plc.append(letrax)
        elif (letrax.lower() not in self.word or letrax.upper() not in self.word) and letrax not in self.Plw:
            self.Plw.append(letrax)
        else:
            return False
        return True

    # Verefica se o game terminou estabelecendo as condições(ganhar,perder) e retorna se alguma das condições for verdadeira.
    def endgame(self):
        return self.won_game() or len(self.Plw) == 6

    # Verifica se o usuário ganhou o game através da condição de que haja a ausência do char '_' no retorno da função word.correct().
    def won_game(self):
        if '_' not in self.word_correct():
            return True
        return False

    # Se a letra em forma maiscula e minuscula não estiver na palavra a função vai retornar '_'.
    # No caso de a letra maiscula ou minuscula estiver na palavra a função vai retornar 'letra'.
    def word_correct(self):
        game = ['_' if letra.lower() not in self.Plc and letra.upper() not in self.Plc else letra for letra in
                self.word]
        return game

    # Printa o item da lista board relacionando o indice do item que vai ser printado com o número de itens no construtor PLw.
    # Printa o retorno da função word_correct().
    # Printa os itens na lista(constructor) Plc.
    # Printa os itens na lista(constructor) Plw.
    def status(self):
        print(board[len(self.Plw)])
        print('\nPalavra:', self.word_correct())
        print('\nLetras corretas:', [letra for letra in self.Plc])
        print('\nLetras incorretas:', [letra for letra in self.Plw])


# Abre o arquivo words para leitura.
# Com o arquivo aberto grava cada linha na variavel words.
# Retorna um item da variavel words através de um sorteio do indice.
def doc_word():
    with open("words", "rt") as wordy:
        words = wordy.readlines()
    return words[random.randint(0, len(words))].strip()


# Chama a class hangman atribuindo o retorno da função doc_word() e grava isso na variavel execution.
# Chama o status da class, pede para o usuário digitar uma letra, faz o tratamento de erro e passa essa letra para função;
# parameters_c_w enquanto o metodo endgame da class hangman não retorna True.
# Depois que loop while terminar chama uma ultima vez o metodo status
# Verifica através do metodo won_game() se o usuário ganhou
def main():
    execution = Hangman(doc_word())

    while not execution.endgame():
        execution.status()
        try:
            letra = input('\nDigite uma letra:')
        except IOError:
            print('Você não digitou uma letra!')
            continue
        else:
            pass
        execution.parameters_c_w(letra)

    execution.status()

    if execution.won_game():
        print('\nVocê venceu!!')
    else:
        print('\nVocê perdeu!!')


# Chama a função main()
if __name__ == '__main__':
    main()
