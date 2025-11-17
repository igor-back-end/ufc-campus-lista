class Aluno:
    def __init__(self, nome, matricula, email, semestre):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.semestre = semestre

    def __str__(self):
        return (f"\n--- Dados do Aluno ---\n"
                f"  Nome: {self.nome}\n"
                f"  Matrícula: {self.matricula}\n"
                f"  E-mail: {self.email}\n"
                f"  Semestre: {self.semestre}º\n"
                f"----------------------")

    def atualizar_email(self, novo_email):
        print(f"E-mail do aluno alterado com sucesso!")
        print(f"  De: {self.email}")
        print(f"  Para: {novo_email}")
        self.email = novo_email

    def atualizar_semestre(self, novo_semestre):
        print(f"Semestre do aluno alterado com sucesso!")
        print(f"  De: {self.semestre}")
        print(f"  Para: {novo_semestre}")
        self.semestre = novo_semestre