# 🏛️ Sistema de Gestão Acadêmica - UFC (CRUD em Python OOP)

**Status:** Projeto Acadêmico Concluído

Este é um projeto de console (CLI) desenvolvido em Python para demonstrar os princípios da **Programação Orientada a Objetos (OOP)**. A aplicação simula um sistema de gestão para a universidade (UFC), permitindo o cadastro hierárquico de Campus, Cursos e Alunos.

O projeto foca em **Encapsulamento**, **Modularização** (uso de pacotes) e **Composição** (objetos compostos por outros objetos).

---

## 🚀 Funcionalidades

O sistema é interativo, baseado em menus, e **já inicia com dados pré-carregados** para facilitar os testes (não é necessário cadastrar tudo do zero).

### Níveis de Gerenciamento (CRUD)

* **Nível 1: Campus**
    * Gerenciar unidades (ex: Pici, Benfica, Sobral).
    * Impede a exclusão de um Campus que possua cursos ativos.
* **Nível 2: Curso**
    * Gerenciar cursos dentro de um Campus específico.
    * Impede a exclusão de um Curso que possua alunos matriculados.
* **Nível 3: Aluno**
    * Gerenciar alunos dentro de um Curso.
    * Permite atualizar e-mail e semestre.

---

## 🏛️ Estrutura do Projeto

O código foi refatorado para utilizar uma estrutura de **Pacote Python**. As regras de negócio estão isoladas dentro do diretório `classes/`.

```text
ufc-campus-lista/
│
├── main.py             # Ponto de entrada, menus e inicialização de dados
│
├── README.md           # Documentação do projeto
│
└── classes/            # Pacote contendo as classes (Regras de Negócio)
    ├── __init__.py     # Expõe as classes para o main.py
    ├── campus.py       # Classe Campus (Gerencia Cursos)
    ├── curso.py        # Classe Curso (Gerencia Alunos)
    └── aluno.py        # Classe Aluno (Dados do estudante)