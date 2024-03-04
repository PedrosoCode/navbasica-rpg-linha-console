import random

# Definindo a classe para as salas
class Room:
    def __init__(self, description, exits, items):
        self.description = description
        self.exits = exits
        self.items = items

# Definindo as salas do jogo
rooms = {
    'sala_principal': Room(
        "Você está na sala principal. Há uma porta ao norte e uma porta ao leste.",
        {'norte': 'sala_do_norte', 'leste': 'sala_do_leste'},
        ['espada']
    ),
    'sala_do_norte': Room(
        "Você entrou na sala do norte. Há uma porta ao sul.",
        {'sul': 'sala_principal'},
        ['poção']
    ),
    'sala_do_leste': Room(
        "Você chegou à sala do leste. Há uma porta ao oeste.",
        {'oeste': 'sala_principal'},
        ['chave']
    )
}

# Função para mostrar a descrição da sala atual
def mostrar_sala_atual(sala_atual):
    print(rooms[sala_atual].description)
    print("Itens nesta sala:", rooms[sala_atual].items)
    print("Saídas disponíveis:", list(rooms[sala_atual].exits.keys()))

# Função principal do jogo
def jogar():
    sala_atual = 'sala_principal'
    while True:
        mostrar_sala_atual(sala_atual)
        comando = input("Digite para onde deseja ir (ou 'sair' para encerrar): ").lower()
        if comando == 'sair':
            print("Até logo!")
            break
        elif comando in rooms[sala_atual].exits:
            sala_atual = rooms[sala_atual].exits[comando]
        else:
            print("Direção inválida!")

# Inicialização do jogo
if __name__ == "__main__":
    print("Bem-vindo ao RPG de linha de console!")
    jogar()
