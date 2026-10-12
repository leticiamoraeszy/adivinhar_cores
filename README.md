# 🎨 Jogo de Adivinhar a Cor

Jogo de terminal em Python no qual o computador escolhe uma cor aleatória e o jogador tenta adivinhá-la. O placar é acumulado ao longo das rodadas, e o vencedor é anunciado quando o jogador decide parar.

Projeto desenvolvido para praticar **Programação Orientada a Objetos (POO)** em Python.

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Conceitos praticados](#-conceitos-praticados)
- [Requisitos](#-requisitos)
- [Como executar](#-como-executar)
- [Como jogar](#-como-jogar)
- [Exemplo de execução](#-exemplo-de-execução)
- [Estrutura do código](#-estrutura-do-código)
- [Melhorias futuras](#-melhorias-futuras)

---

## ✨ Funcionalidades

- O computador sorteia uma cor entre **azul**, **vermelho** e **verde**
- O jogador digita o palpite (aceita maiúsculas/minúsculas e espaços extras)
- Placar separado para o jogador e para o computador
- Opção de continuar ou encerrar após cada palpite
- Exibição da pontuação final e do vencedor

---

## 🧠 Conceitos praticados

- Classes e objetos
- Herança (`Rodada` herda de `Advinhar`)
- Classe base abstrata (`ABC`)
- Atributos de instância e método construtor (`__init__`)
- Módulo `random` (`random.choice`)
- Módulo `time` (`sleep`)
- Laço `while`, condicionais e tratamento de entrada do usuário
- Formatação de strings com f-strings

---

## 🔧 Requisitos

- [Python 3.8+](https://www.python.org/downloads/)

Não há dependências externas: o projeto usa apenas a biblioteca padrão do Python.

---

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

2. Entre na pasta do projeto:

```bash
cd NOME-DO-REPOSITORIO
```

3. Execute o jogo:

```bash
python main.py
```

> Substitua `main.py` pelo nome do seu arquivo, caso seja diferente.

---

## 🎮 Como jogar

1. O programa pede que você escolha uma das cores disponíveis.
2. Digite a cor que acha que o computador escolheu.
3. O jogo informa se você **acertou** ou **errou** e atualiza o placar.
4. Responda `S` para continuar ou `N` para encerrar.
5. Ao encerrar, a pontuação total é exibida junto com o vencedor.

---

## 💻 Exemplo de execução

```text
Escreva uma dessas cores: ('azul', 'vermelho', 'verde'). Tente adivinhar a cor que eu escolhi! azul
ERROU!. Eu escolhi verde e você azul
Deseja continuar?[S/N] s
continunando o jogo...
Escreva uma dessas cores: ('azul', 'vermelho', 'verde'). Tente adivinhar a cor que eu escolhi! verde
ACERTOU! Eu escolhi a cor verde e você verde
Deseja continuar?[S/N] n

---PONTUAÇÃO---
computador: 1
jogador Lucia: 1
Jogador Lucia venceu!
```

---

## 🗂️ Estrutura do código

| Classe / Método | Descrição |
|---|---|
| `Advinhar` (classe abstrata) | Define o estado base do jogo: cores disponíveis, nome do jogador e contadores de pontos |
| `Rodada` (herda de `Advinhar`) | Contém a lógica do jogo |
| `Rodada.jogar()` | Executa as rodadas: sorteia a cor, lê o palpite, atualiza a pontuação e pergunta se o jogador quer continuar |
| `Rodada.vencedor()` | Exibe o placar final e anuncia quem venceu |

### Atributos principais

| Atributo | Função |
|---|---|
| `cores` | Tupla com as cores possíveis |
| `nome` | Nome do jogador |
| `pontos_jogador` / `pontos_computador` | Pontuação da sessão atual |
| `tot_player` / `tot_pc` | Pontuação total acumulada |

---

## 🔮 Melhorias futuras

- [ ] Em vez de encerrar o programa com `ValueError` quando a cor é inválida, pedir o palpite novamente
- [ ] Tratar entrada vazia na pergunta "Deseja continuar?" (hoje gera `IndexError`)
- [ ] Tratar o caso de **empate** no placar final
- [ ] Sortear uma nova cor a cada palpite
- [ ] Pedir o nome do jogador via `input()`
- [ ] Adicionar mais cores e níveis de dificuldade
- [ ] Criar uma versão com interface gráfica (Tkinter)

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo.
