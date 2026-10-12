import random
from abc import ABC
from time import sleep
class Advinhar(ABC):
    def __init__(self, nome):
        self.cores = 'azul', 'vermelho', 'verde'
        self.nome = nome
        # pontuação da rodada atual
        self.pontos_computador = 0
        self.pontos_jogador = 0
        self.tot_player = 0
        self.tot_pc = 0

class Rodada(Advinhar):
    def jogar(self):
        self.pontos_computador = 0
        self.pontos_jogador = 0
        computador = random.choice(self.cores)
        while True:
                jogador = str(input(f'Escreva uma dessas cores: {self.cores}. Tente adivinhar a cor que eu escolhi!')).lower().strip()
                if jogador not in self.cores:
                    raise ValueError('VALOR INVÁLIDO, TENTE NOVAMENTE')
                    continue
                if jogador == computador:
                    self.pontos_jogador += 1
                    print(f'ACERTOU! Eu escolhi a cor {computador} e você {jogador}')
                elif jogador != computador:
                    self.pontos_computador += 1
                    print(f'ERROU!. Eu escolhi {computador} e você {jogador}')
                opção = input('Deseja continuar?[S/N]').strip().upper()[0]
                if opção in 'N':
                         self.tot_player += self.pontos_jogador
                         self.tot_pc += self.pontos_computador
                         break
                print('continunando o jogo...')
                sleep(1)

    def vencedor(self):
        print('\n---PONTUAÇÃO---')
        print(f'computador: {self.tot_pc}')
        print(f'jogador {self.nome}: {self.tot_player}')
        if self.tot_pc > self.tot_player:
            print('Computador venceu!')
        else:
            print(f'Jogador {self.nome} venceu!')

jogo = Rodada('Lucia')

jogo.jogar()
jogo.vencedor()

