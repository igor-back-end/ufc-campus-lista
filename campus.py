from curso import Curso

class Campus:

    def __init__(self, nome_campus, cidade):
        self.nome_campus = nome_campus
        self.cidade = cidade
        self.lista_de_cursos = []
        print(f"\nCampus '{self.nome_campus}' ({self.cidade}) adicionado com sucesso!")

    def __str__(self):
        return f"[Campus: {self.nome_campus} ({self.cidade}) | Cursos: {len(self.lista_de_cursos)}]"

    def adicionar_curso(self, nome_curso, codigo_curso):
        if self.buscar_curso_por_codigo(codigo_curso):
            print(f"[Erro]: O curso com código {codigo_curso} já existe neste campus!")
            return

        novo_curso = Curso(nome_curso, codigo_curso)

        self.lista_de_cursos.append(novo_curso)
        print(f"\nCurso '{nome_curso}' (Cod: {codigo_curso}) adicionado ao campus '{self.nome_campus}' com sucesso!")

    def listar_cursos(self):
        print(f"\n--- Lista de Cursos do Campus: {self.nome_campus} ---")

        for curso in self.lista_de_cursos:
            print(curso)

        print(f"\n--- Total: {len(self.lista_de_cursos)} cursos ---")

    def buscar_curso_por_codigo(self, codigo_curso):
        for curso in self.lista_de_cursos:
            if curso.codigo_curso == codigo_curso:
                return curso
        return None

    def remover_curso(self, codigo_curso):
        curso_para_remover = self.buscar_curso_por_codigo(codigo_curso)

        if curso_para_remover:
            if len(curso_para_remover.lista_de_alunos) > 0:
                print(f"[Erro]: Não pode remover o curso '{curso_para_remover.nome_curso}'.")
                print(f"[Motivo]: Ainda existem alunos matriculados.")
                return

            self.lista_de_cursos.remove(curso_para_remover)
            print(f"\nCurso '{curso_para_remover.nome_curso}' foi removido do campus '{self.nome_campus}' com sucesso!")
        else:
            print(f"[Erro]: Curso com código {codigo_curso} não encontrado.")