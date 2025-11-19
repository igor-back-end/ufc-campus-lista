from classes import Campus

lista_geral_campus = []

def buscar_campus_por_nome(nome):
    for campus in lista_geral_campus:
        if campus.nome_campus.lower() == nome.lower():
            return campus
    return None

def menu_alunos(curso_selecionado):
    while True:
        print(f"\n--- Gerenciando Curso: [{curso_selecionado.nome_curso} (Cod: {curso_selecionado.codigo_curso})] ---")
        print("[1] Adicionar Aluno")
        print("[2] Listar Alunos")
        print("[3] Atualizar Aluno")
        print("[4] Remover Aluno")
        print("[0] Voltar ao Menu de Cursos\n")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == '1':
            nome = input("\nNome do Aluno: ").upper()
            matricula = (input("Matrícula: ").strip()).upper()
            email = (input("Email: ").strip()).upper()
            try:
                semestre = int(input("Semestre (ex: 1): "))
                curso_selecionado.adicionar_aluno(nome, matricula, email, semestre)
            except ValueError:
                print("[Erro]: Semestre deve ser um número.")

        elif opcao == '2':
            if len(curso_selecionado.lista_de_alunos) == 0:
                print('Nenhum aluno adicionado a este curso.')
            else:
                curso_selecionado.listar_alunos()

        elif opcao == '3':
            if len(curso_selecionado.lista_de_alunos) == 0:
                print('Nenhum aluno adicionado a este curso.')
            else:
                matricula = (input("\nMatrícula do Aluno a atualizar: ").strip()).upper()
                aluno = curso_selecionado.buscar_aluno_por_matricula(matricula)

                if aluno:
                    print(f"\nAtualizando Aluno: {aluno.nome}")
                    novo_email = (input(f"Novo email (Enter para manter '{aluno.email}'): ").strip()).upper()
                    novo_sem_str = input(f"Novo semestre (Enter para manter '{aluno.semestre}'): ")

                    email_final = novo_email if novo_email else None
                    semestre_final = None

                    if novo_sem_str:
                        try:
                            semestre_final = int(novo_sem_str)
                        except ValueError:
                            print("[Erro]: Semestre inválido, não será atualizado.")

                    curso_selecionado.atualizar_aluno(matricula,
                                                                novo_email=email_final,
                                                                novo_semestre=semestre_final)
                else:
                    print("[Erro]: Aluno não encontrado.")

        elif opcao == '4':
            if len(curso_selecionado.lista_de_alunos) == 0:
                print('Nenhum aluno adicionado a este curso.')
            else:
                matricula = (input("\nMatrícula do Aluno a remover: ").strip()).upper()
                curso_selecionado.remover_aluno(matricula)

        elif opcao == '0':
            print("Voltando...")
            break

        else:
            print("[Erro]: Opção inválida.")

def menu_cursos(campus_selecionado):
    while True:
        print(f"\n--- Gerenciando Campus: [{campus_selecionado.nome_campus}] ---")
        print("[1] Adicionar Curso")
        print("[2] Listar Cursos")
        print("[3] Gerenciar um Curso (ver alunos)")
        print("[4] Remover Curso")
        print("[0] Voltar ao Menu Principal\n")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == '1':
            nome_curso = input("\nNome do Curso: ").upper()
            cod_curso = (input("Código do Curso (ex: AB01): ").strip()).upper()
            campus_selecionado.adicionar_curso(nome_curso, cod_curso)

        elif opcao == '2':
            campus_selecionado.listar_cursos()

        elif opcao == '3':
            if len(campus_selecionado.lista_de_cursos) == 0:
                print('Nenhum curso adicionado neste campus.')
            else:
                cod_curso = (input("\nCódigo do Curso que deseja gerenciar: ").strip()).upper()
                curso = campus_selecionado.buscar_curso_por_codigo(cod_curso)
                if curso:
                    menu_alunos(curso)
                else:
                    print("[Erro] Curso não encontrado.")

        elif opcao == '4':
            if len(campus_selecionado.lista_de_cursos) == 0:
                print('Nenhum curso adicionado neste campus.')
            else:
                cod_curso = (input("\nCódigo do Curso a remover: ").strip()).upper()
                campus_selecionado.remover_curso(cod_curso)

        elif opcao == '0':
            print("Voltando...")
            break

        else:
            print("[Erro] Opção inválida.")

def menu_principal():
    while True:
        print("\n--- Sistema de Gestão - UFC ---")
        print("[1] Criar Novo Campus")
        print("[2] Listar todos os Campus")
        print("[3] Gerenciar um Campus (ver cursos)")
        print("[4] Excluir um Campus")
        print("[0] Sair do Sistema\n")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == '1':
            nome = input("\nDigite o nome do Campus: ")
            campus_existente = buscar_campus_por_nome(nome)

            if campus_existente:
                print(f"[Erro]: O campus '{nome}' já existe no sistema!")
            else:
                cidade = input("Digite a cidade do Campus: ")
                novo_campus = Campus(nome, cidade)
                lista_geral_campus.append(novo_campus)

        elif opcao == '2':
            print("\n--- Lista de Campus Cadastrados ---")
            if not lista_geral_campus:
                print("Nenhum campus cadastrado.")
            else:
                for campus in lista_geral_campus:
                    print(campus)

        elif opcao == '3':
            if len(lista_geral_campus) == 0:
                print("Nenhum campus cadastrado.")
            else:
                nome_campus = input("\nNome do Campus que deseja gerenciar: ")
                campus = buscar_campus_por_nome(nome_campus)

                if campus:
                    menu_cursos(campus)
                else:
                    print("[Erro] Campus não encontrado.")

        elif opcao == '4':
            if len(lista_geral_campus) == 0:
                print("Nenhum campus cadastrado.")
            else:
                nome_campus = input("\nNome do Campus que deseja remover: ")
                campus = buscar_campus_por_nome(nome_campus)

                if campus:
                    if len(campus.lista_de_cursos) > 0:
                        print(f"[Erro]: Não é possível remover o Campus '{campus.nome_campus}'.")
                        print("[Motivo]: Este campus ainda possui cursos cadastrados.")
                    else:
                        lista_geral_campus.remove(campus)
                        print(f"O Campus '{campus.nome_campus}' foi removido com sucesso!")
                else:
                    print("[Erro]: Campus não encontrado.")

        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!")
            break

        else:
            print("[Erro]: Opção inválida. Tente novamente!")

if __name__ == "__main__":
    menu_principal()