from .aluno import Aluno

class Curso:
    def __init__(self, nome_curso, codigo_curso):
        self.nome_curso = nome_curso
        self.codigo_curso = codigo_curso
        self.lista_de_alunos = []

    def __str__(self):
        return f"[Curso: {self.nome_curso} (Cod: {self.codigo_curso}) | Alunos: {len(self.lista_de_alunos)}]"

    def adicionar_aluno(self, nome, matricula, email, semestre):
        if self.buscar_aluno_por_matricula(matricula):
            print(f"[Erro]: Aluno com matrícula {matricula} já existe neste curso!")
            return

        novo_aluno = Aluno(nome, matricula, email, semestre)

        self.lista_de_alunos.append(novo_aluno)
        print(f"\nAluno '{nome}' (Mat: {matricula}) adicionado ao curso '{self.nome_curso}'.")

    def listar_alunos(self):
        print(f"\n--- Lista de Alunos do Curso: {self.nome_curso} (Cod: {self.codigo_curso}) ---")
        if not self.lista_de_alunos:
            print("Nenhum aluno cadastrado neste curso.")
            return

        for aluno in self.lista_de_alunos:
            print(aluno)
        print(f"\n--- Total: {len(self.lista_de_alunos)} aluno(s) ---")

    def buscar_aluno_por_matricula(self, matricula):
        for aluno in self.lista_de_alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def atualizar_aluno(self, matricula, novo_email=None, novo_semestre=None):
        aluno_para_atualizar = self.buscar_aluno_por_matricula(matricula)

        if aluno_para_atualizar:

            if novo_email or novo_semestre:
                print(f"\n--- Atualizando dados do aluno: {aluno_para_atualizar.nome} ---")
            if novo_email:
                aluno_para_atualizar.atualizar_email(novo_email)
            if novo_semestre:
                aluno_para_atualizar.atualizar_semestre(novo_semestre)
        else:
            print(f"[Erro]: Aluno com matrícula {matricula} não encontrado.")

    def remover_aluno(self, matricula):
        aluno_para_remover = self.buscar_aluno_por_matricula(matricula)

        if aluno_para_remover:
            self.lista_de_alunos.remove(aluno_para_remover)
            print(f"\nAluno '{aluno_para_remover.nome}' (Mat: {matricula}) foi removido com sucesso!.")
        else:
            print(f"[Erro]: Aluno com matrícula {matricula} não encontrado.")