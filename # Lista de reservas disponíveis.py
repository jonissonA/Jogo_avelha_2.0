# Lista de reservas disponíveis
reservas_disponiveis = ['Sala01', 'Sala02', 'Sala03', 'Sala04', 'Sala05']
# Dicionário para armazenar reservas de usuários
reservas_usuario = {}

# Exibir menu
def exibir_menu():
    print("\nBem-vindo ao Sistema de Reservas de Salas")
    print("Escolha uma opção:")
    print("(1) Registrar Reserva")
    print("(2) Cancelar Reserva")
    print("(3) Visualizar Reserva")
    print("(4) Disponibilidade")
    print("(5) Sair do Sistema")

# Registrar reserva
def registrar_reserva(reservas_disponiveis, reservas_usuario):
    cliente = input('Digite seu nome: ').capitalize()
    if cliente in reservas_usuario:
        print(f'Você já tem uma reserva na {reservas_usuario[cliente]}.')
        return

    print('Salas disponíveis:')
    for sala in reservas_disponiveis:
        print(sala)

    sala_reservada = input('Informe a sala que você deseja reservar: ').capitalize()

    if sala_reservada in reservas_disponiveis:
        reservas_disponiveis.remove(sala_reservada)
        reservas_usuario[cliente] = sala_reservada
        print(f'Reserva realizada com sucesso para a {sala_reservada}!')
    else:
        print('Sala indisponível ou inválida.')

# Cancelar reserva
def cancelar_reserva(reservas_disponiveis, reservas_usuario):
    cliente = input('Digite seu nome: ').capitalize()
    if cliente in reservas_usuario:
        sala_reservada = reservas_usuario.pop(cliente)
        if sala_reservada == 'Sala01':
         reservas_disponiveis.insert(0, sala_reservada)
        elif sala_reservada == 'Sala02':
         reservas_disponiveis.insert(1, sala_reservada)
        elif sala_reservada == 'Sala03':
         reservas_disponiveis.insert(2, sala_reservada)
        elif sala_reservada == 'Sala04':
         reservas_disponiveis.insert(3, sala_reservada)
        elif sala_reservada == 'Sala05':
         reservas_disponiveis.insert(4, sala_reservada)
        print(f'Sua reserva para a {sala_reservada} foi cancelada.')
    else:
        print('Você não possui reservas.')

# Visualizar reserva
def visualizar_reserva(reservas_usuario):
    cliente = input('Digite seu nome: ').capitalize()
    if cliente in reservas_usuario:
        print(f'Você tem uma reserva na {reservas_usuario[cliente]}.')
    else:
        print('Você não possui reservas.')

# Consultar disponibilidade
def consultar_disponibilidade(reservas_disponiveis):
    if reservas_disponiveis:
        print('Salas disponíveis:')
        for sala in reservas_disponiveis:
            print(sala)
    else:
        print('Nenhuma sala disponível.')

# Função principal para exibir o menu e tratar as opções
def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ").upper()
        if opcao == '1':
            registrar_reserva(reservas_disponiveis, reservas_usuario)
        elif opcao == '2':
            cancelar_reserva(reservas_disponiveis, reservas_usuario)
        elif opcao == '3':
            visualizar_reserva(reservas_usuario)
        elif opcao == '4':
            consultar_disponibilidade(reservas_disponiveis)
        elif opcao == '5':
            print("Saindo do Sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
