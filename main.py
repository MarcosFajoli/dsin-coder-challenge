import requests, os, time
from colorama import Fore, Back, Style, init

init(autoreset=True)

def catalogo_hospedeiros():
    try:
        response = requests.get("http://localhost:8080/hospedeiro")

        if response.status_code == 200:
            count = 0
            data = response.json()

            for hospedeiro in data:
                count += 1
            
            for i in range(0, count, 1):
                print(f"\n{Fore.RED}{Back.WHITE} HOSPEDEIRO ID: {data[i]['id']} ") 
                print(f"\n{Fore.YELLOW}Idade: {data[i]['idade']}\n{Fore.RED}Sexo: {data[i]['sexo']}\n{Fore.GREEN}Peso: {data[i]['peso']}\n{Fore.MAGENTA}Altura: {data[i]['altura']}\n{Fore.BLUE}Tipo sanguíneo: {data[i]['tipoSanguineo']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Gêneros de música preferidos:")
                for tipo in data[i]['gostoMusical']:
                    print(f"{Fore.CYAN}    {tipo}")
                print(f"{Fore.GREEN}Esportes praticados:")
                for tipo in data[i]["esporte"]:
                    print(f"{Fore.GREEN}    {tipo}")
                print(f"{Fore.MAGENTA}Jogos preferidos:")
                for tipo in data[i]["jogoPreferido"]:
                    print(f"{Fore.MAGENTA}    {tipo}")
                input()
                os.system("cls")
            
            input("Finalizado. Pressione enter para continuar...")
        else:
            print(f'Erro na solicitação. Código de status: {response.status_code}')

    except Exception as e:
        print(f'Erro: {e}')

def main():
    continuar = True
    os.system('cls')
    print(f"\nBem vindo ao {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim{Style.RESET_ALL}.")
    input()

    while continuar:
        os.system('cls')
        print(f"{Fore.BLACK}{Back.WHITE} MENU {Style.RESET_ALL} - digite o número da escolha desejada...")
        print(f"{Fore.YELLOW}1 - Relação dos Hospedeiros Catalogados{Style.RESET_ALL}\n{Fore.BLUE}2 - Inserir um novo Hospedeiro{Style.RESET_ALL}\n{Fore.GREEN}3 - Transforme um Hospedeiro em Zumbi! (hipoteticamente){Style.RESET_ALL}\n{Fore.CYAN}4 - Conheça a história do {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim.{Style.RESET_ALL}\n0 - Sair do sistema.")
        
        escolha = input()
        while not escolha.isdigit() or int(escolha) < 0 or int(escolha) > 4:
            escolha = input("Digite um número válido: ")
        escolha = int(escolha)

        match escolha:
            case 1:
                os.system('cls')
                print("Um momento, estamos trazendo o catálogo dos hospedeiros já cadastrados...")
                time.sleep(2)
                catalogo_hospedeiros()
            case 0:
                os.system('cls')
                print(f"O {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim{Style.RESET_ALL} está sendo encerrado...")
                time.sleep(2)
                continuar = False


if __name__ == '__main__':
    main()