class Filme:
    def __init__(self, nome):
        self.nome = nome        # armazena o nome do filme
        self.proximo = None     # aponta para o próximo filme na lista circular

class ListaFilmes:              
    def __init__(self):         # construtor iniciando a lista vazia
        self.primeiro = None  
        self.quantidade = 0

    def adicionar_filme(self, nome_filme):
        novo_filme = Filme(nome_filme)
        if self.quantidade == 0:
            novo_filme.proximo = novo_filme  # A lista está vazia, o novo filme aponta para si mesmo
            self.primeiro = novo_filme  # O primeiro filme da lista é o novo filme
        else:
            novo_filme.proximo = self.primeiro  # O novo filme aponta para o primeiro filme
            ultimo_filme = self.primeiro
            while ultimo_filme.proximo != self.primeiro:
                ultimo_filme = ultimo_filme.proximo
            ultimo_filme.proximo = novo_filme  # O último filme aponta para o novo filme
        self.quantidade += 1

    def buscar_filme(self, nome_filme):
        if self.quantidade == 0:
            return None  # A lista está vazia, não há filme para buscar

        filme_atual = self.primeiro
        while True:
            if filme_atual.nome == nome_filme:
                return filme_atual  # Filme encontrado
            filme_atual = filme_atual.proximo
            if filme_atual == self.primeiro:
                break  # Percorreu toda a lista e voltou ao início, filme não encontrado
        return None

    def remover_filme(self, nome_filme):
        if self.quantidade == 0:
            return  # A lista está vazia, não há filme para remover

        filme_anterior = None
        filme_atual = self.primeiro

        while True:
            if filme_atual.nome == nome_filme:
                if filme_anterior is None:
                    # O primeiro filme está sendo removido
                    if self.quantidade == 1:
                        self.primeiro = None  # A lista tinha apenas um filme
                    else:
                        self.primeiro = filme_atual.proximo  # Atualiza o primeiro filme
                        ultimo_filme = self.primeiro
                        while ultimo_filme.proximo != filme_atual:
                            ultimo_filme = ultimo_filme.proximo
                        ultimo_filme.proximo = self.primeiro  # O último filme aponta para o novo primeiro filme
                else:
                    # O filme no meio ou no final está sendo removido
                    filme_anterior.proximo = filme_atual.proximo
                self.quantidade -= 1
                return
            filme_anterior = filme_atual
            filme_atual = filme_atual.proximo
            if filme_atual == self.primeiro:
                break  # Percorreu toda a lista e voltou ao início, filme não encontrado

    def contar_filmes(self):
        return self.quantidade

    def mostrar_filmes(self):
        if self.quantidade == 0:
            return
        else:
            filme_atual = self.primeiro
            print("Filmes na lista:")
            for _ in range(self.quantidade):
                print(filme_atual.nome)
                filme_atual = filme_atual.proximo

# Função principal
def main():
    lista = ListaFilmes()
    escolha = None

    while escolha != 0:
        print("\nMenu:")
        print("1. Adicionar Filme")
        print("2. Remover Filme")
        print("3. Buscar Filme")
        print("4. Contar Filmes")
        print("5. Mostrar Filmes")
        print("0. Sair")

        print("\n")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            nome_filme = input("Digite o nome do filme a ser adicionado: ")
            lista.adicionar_filme(nome_filme)
            print(f"*{nome_filme}* foi adicionado com sucesso na lista!")

        elif escolha == 2:
            if lista.quantidade != 0:
                nome_filme = input("Digite o nome do filme a ser removido: ")
                lista.remover_filme(nome_filme)
                print(f"*{nome_filme}* foi removido com sucesso!")
            else:
                print("A lista está vazia, não há filmes para remover")

        elif escolha == 3:
            print("\n")
            nome_filme = input("Digite o nome do filme a ser buscado: ")
            filme_encontrado = lista.buscar_filme(nome_filme)
            if filme_encontrado:
                print("\n")
                print(f"Filme encontrado: {filme_encontrado.nome}")
            else:
                print("\n")
                print(f"{nome_filme} não encontrado, esse filme não está na lista")

        elif escolha == 4:
            print("\n")
            print(f"Quantidade de filmes na lista: {lista.contar_filmes()}")

        elif escolha == 5:
            if lista.quantidade != 0:
                print("\n")
                lista.mostrar_filmes()
            else:
                print("A lista está vazia.")

        elif escolha == 0:
            print("\n")
            print("Saindo do programa...")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()