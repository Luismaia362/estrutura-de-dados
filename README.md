# Sistema de Mecânica de Ônibus

Projeto desenvolvido em Python utilizando Flask e SQLite para gerenciamento de ônibus em uma mecânica.

## Objetivo

O sistema foi criado para simular o gerenciamento de atendimento de ônibus em uma mecânica, utilizando conceitos de estruturas de dados como fila e pilha.

---

# Tecnologias Utilizadas

- Python
- Flask
- Flask-CORS
- SQLite

---

# Funcionalidades

## Cadastro de ônibus
Permite cadastrar ônibus informando:
- Nome
- Prioridade
- Facilidade de manutenção

Todos os dados são armazenados no banco de dados SQLite.

---

## Listagem de ônibus
Exibe todos os ônibus cadastrados no sistema.

---

## Remoção de ônibus
Permite remover ônibus através do ID.

---

## Histórico de atendimentos
O sistema possui uma pilha de histórico para armazenar atendimentos realizados.

---

## Desfazer atendimento
Permite desfazer o último atendimento realizado utilizando o conceito de pilha (LIFO).

---

# Estruturas de Dados Utilizadas

## Fila
Utilizada para armazenar ônibus aguardando atendimento.

```python
fila = []
