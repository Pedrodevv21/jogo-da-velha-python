# Jogo da Velha em Python

Projeto de **Jogo da Velha (Tic-Tac-Toe)** desenvolvido em **Python**, executado no terminal.

O projeto foi criado com o objetivo de praticar lógica de programação, organização de código e evolução incremental, incluindo posteriormente integração com banco de dados.

---

## Como funciona

* Tabuleiro **3x3**
* Jogadores alternam entre **X** e **O**
* Escolha de jogadas via terminal (linha e coluna)
* Validações implementadas:

  * posição ocupada
  * entrada inválida
  * opção de sair do jogo
* Verificação automática de:

  * vitória (linhas, colunas e diagonais)
  * empate (velha)
* Modos disponíveis:

  * jogador vs jogador
  * jogador vs computador

---

## Como executar o projeto (modo rápido)

Você pode rodar o jogo normalmente sem configurar banco de dados.

### 1. Clonar o repositório

```bash
git clone
cd jogo-da-velha
```

---

### 2. Executar o projeto

```bash
python main.py
```

> O jogo roda diretamente no terminal e não requer instalação adicional.

---

## Sobre o banco de dados

O projeto também possui integração com **PostgreSQL**, onde é possível:

* salvar o resultado das partidas
* registrar histórico de jogos
* armazenar data e horário

Essa funcionalidade foi implementada para praticar integração com banco de dados utilizando **psycopg2**.

> A configuração do banco é opcional e não é necessária para testar o jogo.

---

## Conceitos praticados

* Estruturas condicionais (`if`)
* Laços de repetição (`while`)
* Manipulação de listas (matrizes)
* Entrada de dados com `input`
* Tratamento de erros (`try/except`)
* Organização de código em múltiplos arquivos
* Integração com banco de dados (SQL)

---

## Estrutura do projeto

```
main.py          # fluxo principal do jogo
Banco_jogo_velha # conexão e operações com o banco de dados

jogo/
  tabuleiro.py   # regras e exibição do tabuleiro
  jogador.py     # entrada do jogador e lógica da CPU
  jogo.py        # controle de modo e fluxo auxiliar
```

---

## Evolução do projeto

### Versão 1

* lógica básica do jogo

### Versão 2

* validação de jogadas
* melhoria de mensagens

### Versão 3

* opção de sair no meio da partida
* contador de partidas
* jogar novamente

### Versão 4

* placar de vitórias
* modo contra computador

### Versão 5

* refatoração e separação em arquivos

### Versão 6

* integração com banco de dados (PostgreSQL)
* persistência de histórico

---

## 🔧 Tecnologias utilizadas

* Python
* Terminal (CLI)
* Git
* PostgreSQL (opcional)
* psycopg2 (opcional)

---

## Objetivo do projeto

Este projeto faz parte do meu processo de aprendizado em programação, com foco em:

* prática constante
* construção de projetos reais
* evolução incremental
* aplicação de conceitos de backend


