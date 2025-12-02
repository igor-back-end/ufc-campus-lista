# 🏛️ Sistema de Gestão Acadêmica - UFC (CRUD em Python OOP)

**Status:** Projeto Acadêmico Concluído ✅

Este é um projeto de console (CLI) desenvolvido em Python para demonstrar a aplicação prática de conceitos avançados de **Programação Orientada a Objetos (OOP)**.

O sistema simula um ambiente de gestão universitária (baseado no contexto da UFC), permitindo o gerenciamento hierárquico de **Campus**, **Cursos**, **Professores** e **Alunos**.

---

## 🚀 Funcionalidades

O sistema possui uma interface baseada em menus interativos e **já inicia com dados pré-carregados** (Campus do Pici, Benfica e Jardins de Anita) para facilitar a testagem imediata.

### 📋 Módulos do Sistema

* **Nível 1: Gestão de Campus**
    * Cadastrar, listar e remover campus.
    * *Regra de Negócio:* Não é possível remover um Campus que possua cursos ativos.

* **Nível 2: Gestão de Cursos**
    * Vincular cursos a um campus específico.
    * *Regra de Negócio:* Não é possível remover um Curso que possua alunos matriculados.

* **Nível 3: Gestão de Corpo Docente (Professores)**
    * Cadastrar professores (com SIAPE, Titulação e Área).
    * **Definir Coordenador:** Permite promover um professor da lista para o cargo de Coordenador do curso.
    * Remover professores (com aviso caso seja o coordenador atual).

* **Nível 4: Gestão de Corpo Discente (Alunos)**
    * Matricular alunos, listar, atualizar dados (e-mail/semestre) e remover.

---

## 🏗️ Arquitetura e Conceitos de OOP

O projeto foi estruturado utilizando boas práticas de desenvolvimento, incluindo a separação em pacotes e o uso de conceitos fundamentais de POO.

### 1. Herança (Generalização/Especialização)
Para evitar repetição de código, foi criada uma classe base genérica.

* **`Pessoa` (Superclasse):** Define os atributos comuns (`nome`, `email`).
* **`Aluno` (Subclasse):** Herda de Pessoa e adiciona `matricula` e `semestre`.
* **`Professor` (Subclasse):** Herda de Pessoa e adiciona `siape`, `titulacao` e `area_atuacao`.

### 2. Composição ("Tem um")
A estrutura de dados segue uma hierarquia de posse:

* O **Campus** possui uma lista de *Cursos*.
* O **Curso** possui uma lista de *Alunos* e uma lista de *Professores*.

### 3. Estrutura de Arquivos (Pacote Python)

O código foi refatorado para utilizar uma estrutura de **Pacote Python**. As regras de negócio estão isoladas dentro do diretório `classes/`.

```text
ufc-campus-lista/
│
├── main.py             # Interface do usuário, menus e inicialização (Seed Data)
│
├── README.md           # Documentação do projeto
│
└── classes/            # Pacote contendo as Regras de Negócio
    ├── __init__.py     # Exposição das classes para o sistema
    ├── pessoa.py       # Classe Base (Mãe)
    ├── aluno.py        # Classe Filha (Herança)
    ├── professor.py    # Classe Filha (Herança)
    ├── curso.py        # Classe Gerenciadora (Composição)
    └── campus.py       # Classe Gerenciadora (Composição)