# 📱 Sistema de Gerenciamento de Contatos e Agendas

Um sistema de gerenciamento de contatos e agendas desenvolvido em Python, utilizando MongoDB como banco de dados através do MongoEngine.

## 🚀 Funcionalidades

### 👥 Gestão de Contatos
- Adicionar novos contatos
- Listar todos os contatos
- Atualizar informações de contatos existentes
- Excluir contatos

### 📚 Gestão de Agendas
- Criar novas agendas
- Listar todas as agendas
- Atualizar informações de agendas
- Excluir agendas

### 🔄 Operações com Agenda
- Adicionar contatos a agendas específicas

## 📋 Pré-requisitos

- Python 3.x
- MongoDB instalado e em execução
- Pacotes Python necessários:
  - mongoengine

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Pxxx010/Sistema-de-Gerenciamento-de-Contatos-e-Agendas.git
cd ATV-CRUD-MONGO
```

2. Instale as dependências:
```bash
pip install mongoengine
```

3. Certifique-se de que o MongoDB está em execução em sua máquina.

## 💻 Como Usar

1. Execute o programa:
```bash
python main.py
```

2. Use o menu interativo para:
   - Gerenciar contatos (adicionar, listar, atualizar, excluir)
   - Gerenciar agendas (criar, listar, atualizar, excluir)
   - Adicionar contatos a agendas

## 🗄️ Estrutura do Banco de Dados

### Coleção: Contact
- name (String, obrigatório)
- phone (String, obrigatório)

### Coleção: Agenda
- name (String, obrigatório)
- contacts (Lista de referências para Contact)

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
⭐️ Desenvolvido com ❤️ 