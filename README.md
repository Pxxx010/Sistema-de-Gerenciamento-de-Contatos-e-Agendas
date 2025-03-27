# Sistema de Gerenciamento de Contatos e Agendas

Um sistema simples para gerenciar contatos e agendas usando Python e MongoDB.

## Requisitos

- Python 3.x
- MongoDB instalado e rodando
- Pacote mongoengine

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install mongoengine
```

## Como Usar

1. Certifique-se de que o MongoDB está rodando
2. Execute o programa:
```bash
python main.py
```

## Funcionalidades

### 1. Adicionar Contato
- Adicione um novo contato com nome e telefone
- Opção para adicionar o contato diretamente a uma agenda

### 2. Listar Contatos
- Visualize todos os contatos cadastrados no sistema

### 3. Criar Agenda
- Crie uma nova agenda para organizar seus contatos

### 4. Listar Agendas
- Visualize todas as agendas e seus contatos

### 5. Adicionar Contato à Agenda
- Adicione um contato existente a uma agenda específica

### 6. Sair
- Encerra o programa

## Estrutura do Projeto

- `main.py`: Arquivo principal com toda a lógica do sistema
- `contact_db`: Banco de dados MongoDB criado automaticamente

## Modelos de Dados

### Contact
- name: Nome do contato
- phone: Número de telefone

### Agenda
- name: Nome da agenda
- contacts: Lista de contatos

## Observações

- O sistema usa MongoDB como banco de dados
- Os dados são persistidos automaticamente
- Interface em linha de comando com formatação amigável 