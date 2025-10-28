from livro import Livro
from aluno import Aluno
from utils import saudacao

print(saudacao())
print("="*60)

# Livros iniciais
livros_disponiveis = [
    Livro("Python para Iniciantes", "João Silva"),
    Livro("Algoritmos e Estruturas de Dados", "Maria Souza"),
    Livro("Banco de Dados Simplificado", "Carlos Lima")
]

alunos = []
historico_emprestimos = []  # guarda registros de empréstimos
historico_devolucoes = []   # guarda registros de devoluções

def encontrar_aluno(nome):
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            return aluno
    return None

def relatorio_geral():
    print("\n=== Relatório Geral da Biblioteca SENAI 'Morvan Figueiredo' ===\n")

    print("Empréstimos atuais:")
    for aluno in alunos:
        for livro in aluno.livros_emprestados:
            print(f"- {aluno.nome} pegou '{livro.titulo}' de {livro.autor}")

    print("\nAvaliações dos Livros:")
    for livro in livros_disponiveis:
        if livro.avaliacoes:
            print(f"- {livro.titulo}: média {livro.media_avaliacoes():.1f}")

    print("\nAvaliações do Atendimento:")
    avaliacoes_atendimento = [a.avaliacao_atendimento for a in alunos if a.avaliacao_atendimento is not None]
    for aluno in alunos:
        if aluno.avaliacao_atendimento is not None:
            print(f"- {aluno.nome}: nota {aluno.avaliacao_atendimento}")

    if avaliacoes_atendimento:
        media_atendimento = sum(avaliacoes_atendimento) / len(avaliacoes_atendimento)
        print(f"\nMédia do atendimento: {media_atendimento:.1f}")
    print("="*60)

def relatorio_detalhado():
    while True:
        print("\n=== Submenu de Relatórios ===")
        print("1 - Quem solicitou empréstimos")
        print("2 - Quem devolveu livros")
        print("3 - Livros disponíveis")
        print("4 - Voltar ao menu principal")

        escolha = input("Digite sua opção: ")

        if escolha == "1":
            print("\n📖 Lista de empréstimos realizados:")
            if historico_emprestimos:
                for registro in historico_emprestimos:
                    print(f"- {registro}")
            else:
                print("Nenhum empréstimo registrado ainda.")

        elif escolha == "2":
            print("\n🔄 Lista de devoluções realizadas:")
            if historico_devolucoes:
                for registro in historico_devolucoes:
                    print(f"- {registro}")
            else:
                print("Nenhuma devolução registrada ainda.")

        elif escolha == "3":
            print("\n📚 Livros disponíveis:")
            disponiveis = [livro for livro in livros_disponiveis if livro.disponivel]
            if disponiveis:
                for livro in disponiveis:
                    print(f"- {livro.titulo} ({livro.autor})")
            else:
                print("Nenhum livro disponível no momento.")

        elif escolha == "4":
            break
        else:
            print("Opção inválida, tente novamente.")


# -------------------------
# Menu interativo
# -------------------------
while True:
    print("\nEscolha uma opção:")
    print("1 - Empréstimo de livro")
    print("2 - Devolução de livro")
    print("3 - Relatórios")
    print("4 - Cadastrar novo livro")
    print("5 - Sair")
    print("6 - Avaliar livro após devolução")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        aluno = encontrar_aluno(nome)
        if not aluno:
            aluno = Aluno(nome)
            alunos.append(aluno)

        print("\nLivros disponíveis:")
        for idx, livro in enumerate(livros_disponiveis):
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{idx+1}. {livro.titulo} - {livro.autor} ({status})")

        while True:
            escolha = input("Escolha o número do livro: ")
            if escolha.isdigit():
                escolha = int(escolha) - 1
                if 0 <= escolha < len(livros_disponiveis):
                    livro_escolhido = livros_disponiveis[escolha]
                    break
                else:
                    print("Número inválido. Digite um número da lista.")
            else:
                print("Entrada inválida. Digite apenas o número do livro.")

        if aluno.emprestar_livro(livro_escolhido):
            print(f"{aluno.nome} emprestou '{livro_escolhido.titulo}'.")
            historico_emprestimos.append(f"{aluno.nome} emprestou '{livro_escolhido.titulo}'")
            nota_atendimento = int(input("Qual a nota (0-10) para o atendimento da biblioteca? "))
            aluno.avaliar_atendimento(nota_atendimento)
        else:
            print("Livro indisponível!")

    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        aluno = encontrar_aluno(nome)
        if aluno and aluno.livros_emprestados:
            print("\nLivros emprestados:")
            for idx, livro in enumerate(aluno.livros_emprestados):
                print(f"{idx+1}. {livro.titulo} - {livro.autor}")

            while True:
                escolha = input("Escolha o número do livro para devolver: ")
                if escolha.isdigit():
                    escolha = int(escolha) - 1
                    if 0 <= escolha < len(aluno.livros_emprestados):
                        livro_devolver = aluno.livros_emprestados[escolha]
                        if aluno.devolver_livro(livro_devolver):
                            print(f"{aluno.nome} devolveu '{livro_devolver.titulo}'.")
                            historico_devolucoes.append(f"{aluno.nome} devolveu '{livro_devolver.titulo}'")
                        break
                    else:
                        print("Número inválido. Digite um número da lista.")
                else:
                    print("Entrada inválida. Digite apenas o número do livro.")
        else:
            print("Aluno não encontrado ou sem livros emprestados.")

    elif opcao == "3":
        print("\n=== Relatórios ===")
        print("1 - Relatório Geral")
        print("2 - Relatórios Detalhados")
        escolha = input("Digite sua opção: ")
        if escolha == "1":
            relatorio_geral()
        elif escolha == "2":
            relatorio_detalhado()
        else:
            print("Opção inválida.")

    elif opcao == "4":
        titulo = input("Digite o título do novo livro: ")
        autor = input("Digite o autor do novo livro: ")
        novo_livro = Livro(titulo, autor)
        livros_disponiveis.append(novo_livro)
        print(f"Livro '{titulo}' de {autor} cadastrado com sucesso!")

    elif opcao == "5":
        print("Encerrando o sistema. Até logo!")
        break

    elif opcao == "6":
        nome = input("Digite o nome do aluno: ")
        aluno = encontrar_aluno(nome)
        if aluno:
            print("\nLivros disponíveis para avaliação (já devolvidos):")
            livros_para_avaliar = [livro for livro in livros_disponiveis if livro.disponivel]
            if livros_para_avaliar:
                for idx, livro in enumerate(livros_para_avaliar):
                    print(f"{idx+1}. {livro.titulo} - {livro.autor}")

                while True:
                    escolha = input("Escolha o número do livro para avaliar: ")
                    if escolha.isdigit():
                        escolha = int(escolha) - 1
                        if 0 <= escolha < len(livros_para_avaliar):
                            livro_avaliar = livros_para_avaliar[escolha]
                            nota = int(input(f"Qual a nota (0-10) para o livro '{livro_avaliar.titulo}'? "))
                            aluno.avaliar_livro(livro_avaliar, nota)
                            print(f"Avaliação registrada para '{livro_avaliar.titulo}'.")
                            break
                        else:
                            print("Número inválido. Digite um número da lista.")
                    else:
                        print("Entrada inválida. Digite apenas o número do livro.")
            else:
                print("Não há livros devolvidos disponíveis para avaliação.")
        else:
            print("Aluno não encontrado.")

    else:
        print("Opção inválida, tente novamente.")
