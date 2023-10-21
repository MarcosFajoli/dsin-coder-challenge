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
            input()
        
        os.system("cls")
        print("Retornando ao menu principal...")
        time.sleep(1)

    except Exception as e:
        print(f'Erro: {e}')

def insert_hospedeiro():
    try:
        seguir = True
        while seguir:
            print(f"\nBem vindo a {Fore.CYAN}Interface Matriz de Cadastro de Hospedeiros{Style.RESET_ALL}. Nela você consegue cadastrar hospedeiros. :)")
            
            print(f"\nIdentificação do hospedeiro (ID): ")
            id = input()

            os.system("cls")
            print(f"Gênero do hospedeiro (M ou F): ")
            sexo = input()

            os.system("cls")
            print(f"Idade do hospedeiro: ")
            idade = input()
            while not idade.isdigit() or int(idade) < 0:
                idade = input("Digite uma idade válida: ")
            idade = int(idade)

            os.system("cls")
            print(f"Peso do hospedeiro (em KG): ")
            peso = input()
            while not peso.isdigit() or int(peso) < 0:
                peso = input("Digite um peso válido: ")
            peso = int(peso)

            os.system("cls")
            print(f"Altura do hospedeiro (em CM): ")
            altura = input()
            while not altura.isdigit() or int(altura) < 0:
                altura = input("Digite uma altura válida: ")
            altura = int(altura)

            os.system("cls")
            tipos = ["A", "B", "AB", "O"]
            print(f"Escolha o tipo sanguíneo do hospedeiro:")
            print(f"{Fore.RED}    1 - A")
            print(f"{Fore.RED}    2 - B")
            print(f"{Fore.RED}    3 - AB")
            print(f"{Fore.RED}    4 - O")
            print(f"{Fore.YELLOW}    ? - {Fore.CYAN}?{Fore.RED}?{Fore.GREEN}?{Fore.MAGENTA}?{Fore.WHITE}?{Fore.BLUE}?{Fore.YELLOW}?")
            escolha_tp = input()
            if escolha_tp == "?":
                tipo_sanguineo = "Dourado"
            else:
                while not escolha_tp.isdigit() or int(escolha_tp) < 0 or int(escolha_tp) > 4:
                    escolha_tp = input("Digite um número válido: ")
                escolha_tp = int(escolha_tp)
                tipo_sanguineo = tipos[escolha_tp - 1]
            
            tipos = ["Pop", "Rock", "Pagode", "Sertanejo", "HipHop_Rap", "Eletronica", "Funk"]
            estilos_musicais = []
            mais_musicas = True
            while mais_musicas:
                os.system("cls")
                print(f"Escolha os gostos musicais do hospedeiro (a {Fore.CYAN}Interface Matriz de Cadastro de Hospedeiros{Style.RESET_ALL} aceita 1 número por vez. Insira outros, caso queira, após o término):")
                print(f"{Fore.CYAN}    1 - Pop")
                print(f"{Fore.CYAN}    2 - Rock")
                print(f"{Fore.CYAN}    3 - Pagode")
                print(f"{Fore.CYAN}    4 - Sertanejo")
                print(f"{Fore.CYAN}    5 - HipHop / Rap")
                print(f"{Fore.CYAN}    6 - Eletrônica")
                print(f"{Fore.CYAN}    7 - Funk")
                escolha_tp = input()
                while not escolha_tp.isdigit() or int(escolha_tp) < 0 or int(escolha_tp) > 7:
                    escolha_tp = input("Digite um número válido: ")
                escolha_tp = int(escolha_tp)
                estilos_musicais.append(tipos[escolha_tp - 1])

                escolha_mais_musicas = input("Deseja adicionar mais músicas? (y/n):")
                if escolha_mais_musicas.lower() != "y": mais_musicas = False

            tipos = ["Futebol", "Basquete", "Volei", "Luta", "Atletismo", "eSports"]
            esportes = []
            mais_esportes = True
            while mais_esportes:
                os.system("cls")
                print(f"Escolha os esportes praticados pelo hospedeiro (a {Fore.CYAN}Interface Matriz de Cadastro de Hospedeiros{Style.RESET_ALL} aceita 1 número por vez. Insira outros, caso queira, após o término):")
                print(f"{Fore.GREEN}    1 - Futebol")
                print(f"{Fore.GREEN}    2 - Basquete")
                print(f"{Fore.GREEN}    3 - Volei")
                print(f"{Fore.GREEN}    4 - Luta")
                print(f"{Fore.GREEN}    5 - Atletismo")
                print(f"{Fore.GREEN}    6 - eSports")
                escolha_tp = input()
                while not escolha_tp.isdigit() or int(escolha_tp) < 0 or int(escolha_tp) > 6:
                    escolha_tp = input("Digite um número válido: ")
                escolha_tp = int(escolha_tp)
                esportes.append(tipos[escolha_tp - 1])

                escolha_mais_esportes = input("Deseja adicionar mais esportes? (y/n):")
                if escolha_mais_esportes.lower() != "y": mais_esportes = False
            
            tipos = ["CounterStrike", "Minecraft", "Fortnite", "TheWitcher", "Valorant", "AssassinsCreed", "WorldOfWarcraft", "FIFA", "LeagueOfLegends", "Dota"]
            jogos = []
            mais_jogos = True
            while mais_jogos:
                os.system("cls")
                print(f"Escolha os jogos preferidos pelo hospedeiro (a {Fore.CYAN}Interface Matriz de Cadastro de Hospedeiros{Style.RESET_ALL} aceita 1 número por vez. Insira outros, caso queira, após o término):")
                print(f"{Fore.MAGENTA}    1 - Counter Strike")
                print(f"{Fore.MAGENTA}    2 - Minecraft")
                print(f"{Fore.MAGENTA}    3 - Fortnite")
                print(f"{Fore.MAGENTA}    4 - The Witcher")
                print(f"{Fore.MAGENTA}    5 - Valorant")
                print(f"{Fore.MAGENTA}    6 - Assasins\'s Creed")
                print(f"{Fore.MAGENTA}    7 - World of Warcraft")
                print(f"{Fore.MAGENTA}    8 - Fifa")
                print(f"{Fore.MAGENTA}    9 - League of Legends")
                print(f"{Fore.MAGENTA}    10 - Dota")
                escolha_tp = input()
                while not escolha_tp.isdigit() or int(escolha_tp) < 0 or int(escolha_tp) > 10:
                    escolha_tp = input("Digite um número válido: ")
                escolha_tp = int(escolha_tp)
                jogos.append(tipos[escolha_tp - 1])

                escolha_mais_jogos = input("Deseja adicionar mais jogos? (y/n):")
                if escolha_mais_jogos.lower() != "y": mais_jogos = False

            os.system("cls")
            print(f"{Fore.BLACK}{Back.WHITE} FICHA DE INSERÇÃO DE HOSPEDEIRO ")
            print(f"\nIdentificação: {id}")
            print(f"Idade: {idade}")
            print(f"Gênero: {sexo}")
            print(f"Peso: {peso}")
            print(f"Altura: {altura}")
            print(f"Tipo sanguíneo: {tipo_sanguineo}")
            print(f"Gostos musicais: {Fore.CYAN}{estilos_musicais}")
            print(f"Esportes praticados: {Fore.GREEN}{esportes}")
            print(f"Jogos preferidos: {Fore.MAGENTA}{jogos}")

            input("\nPressione enter para realizar a inserção no sistema...")

            data = {
                'id': id,
                'idade': idade,
    	        'sexo': sexo,
                'peso': peso,
                'altura': altura,
                'tipoSanguineo': tipo_sanguineo,
                'gostoMusical': estilos_musicais,
                'esporte': esportes,
                'jogoPreferido': jogos
            }

            response = requests.post("http://localhost:8080/hospedeiro", json=data)
            os.system("cls")
            print(f"Hospedeiro inserido com sucesso. Identificação: {response.content}")
            time.sleep(2)
            escolha_seguir = input("Deseja seguir cadastrando mais hospedeiros? (y/n):")
            if escolha_seguir.lower() != "y": seguir = False
        
        os.system("cls")
        print("Retornando ao menu principal...")
        time.sleep(1)

    except Exception as e:
        print(f'Erro: {e}')
        input()

def transformar_zumbi():
    try:
        seguir = True
        while seguir:
            print(f"\nBem vindo ao {Fore.GREEN}Transformador Hipotético de Hospedeiro em Zumbi{Style.RESET_ALL}. Nele você consegue transformar hipotéticamente hospedeiros em zumbis pra ver no que dá.")

            id = input("\nDigite o identificador do hospedeiro que deseja converter: ")

            print("Conversão sendo realizada...")
            time.sleep(1)

            response = requests.get("http://localhost:8080/zumbi/"+id)
            if response.status_code != 200:
                print(f'Erro: {response.content}')
            else:
                zumbi = response.json()
                os.system('cls')
                print(f"{Fore.RED}{Back.WHITE} IDENTIFICADOR DO ZUMBI: {zumbi['id']} ") 
                print(f"\nIdade: {zumbi['idade']}")
                print(f"Peso: {zumbi['peso']}")
                print(f"Altura: {zumbi['altura']}")
                print(f"{Fore.RED}Força: {zumbi['forca']}")
                print(f"{Fore.GREEN}Velocidade: {zumbi['velocidade']}")
                print(f"{Fore.BLUE}Inteligência: {zumbi['inteligencia']}")
                print("Especiais:")
                for especial in zumbi['especiais']:
                    for nome, descricao in especial.items():
                        print(f"    Nome: {Fore.MAGENTA}{nome}")
                        print(f"    Descrição: {Fore.BLUE}{descricao}\n")

                print(f"Hospedeiro convertido hipoteticamente com sucesso. Deseja continuar no {Fore.GREEN}Transformador Hipotético de Hospedeiro em Zumbi{Style.RESET_ALL}? (y/n):")
                escolha_seguir = input()
                if escolha_seguir.lower() != "y": seguir = False

        os.system("cls")
        print("Retornando ao menu principal...")
        time.sleep(1)

    except Exception as e:
        print(f'Erro: {e}')
        input()

def contar_historia():
    os.system("cls")
    historia = [
        "Um belo dia, um jovem avistou a possibilidade de ganhar um bom dinheiro e fazer um software diferenciado, com base na demanda do cliente.",
        "Sem saber, ele estava criando o SISTEMA ADMINISTRADOR DE HOSPEDEIROS, ou algo assim que iria ser utilizado para catálogo de uma ameaça que estava por vir.",
        "Esse jovem dedicou horas e horas de desenvolvimento no seu tempo livre, onde lendas dizem que eram pouquíssimos, afinal de contas os jovens trabalham e estudam na época que este software foi criado.",
        "Atualmente, no meio do apocalipse, utilizamos o SISTEMA ADMINISTRADOR DE HOSPEDEIROS, ou algo assim como principal meio de catálogo e verificação dos possíveis hospedeiros.",
        "Não se sabe mais quase nada sobre esse jovem, a não ser as iniciais de seu nome (M R D). Existem documentos espalhados pelo mundo que dizem que as iniciais seriam uma referência a \"Marco Rei Delas\"..."
        "Mas ninguém tem o nome assim, nem antigamente. Deve ser alguma piada do criador.", 
        "O sistema não é perfeito, e nossos programadores fazem atualizações nele sempre que necessário.",
        "Porém, o algoritmo de conversão de Hospedeiro para Zumbi continua sendo imutável, elaborado pelo próprio MRD. Ele era fera demais."
    ]

    print(f"{Fore.BLACK}{Back.WHITE} HISTÓRIA DO {Fore.BLUE}SISTEMA ADMINISTRADOR DE HOSPEDEIROS, OU ALGO ASSIM ")
    print("Pressione enter para continuar a história...\n")
    for frase in historia:
        print(frase)
        input()
    
    input("\nFinalizado. Pressione enter para continuar...")

    os.system("cls")
    print("Retornando ao menu principal...")
    time.sleep(1)


def main():
    continuar = True
    os.system('cls')
    print(f"\nBem vindo ao {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim{Style.RESET_ALL}.")
    input("\nPressione enter para continuar...")

    while continuar:
        os.system('cls')
        print(f"{Fore.BLACK}{Back.WHITE} MENU {Style.RESET_ALL} - digite o número da escolha desejada...")
        print(f"{Fore.YELLOW}1 - Relação dos Hospedeiros Catalogados{Style.RESET_ALL}\n{Fore.BLUE}2 - Inserir um novo Hospedeiro{Style.RESET_ALL}\n{Fore.GREEN}3 - Transforme um Hospedeiro em Zumbi! (hipoteticamente){Style.RESET_ALL}\n{Fore.CYAN}4 - Conheça a história do {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim.{Style.RESET_ALL}\n0 - Sair do sistema.")
        
        escolha = input()
        while not escolha.isdigit() or int(escolha) < 0 or int(escolha) > 4:
            escolha = input("Digite um número válido: ")
        escolha = int(escolha)
        os.system('cls')

        match escolha:
            case 1:
                print("Carregando o catálogo dos hospedeiros já cadastrados...")
                time.sleep(2)
                catalogo_hospedeiros()
            case 2:
                print("Carregando a interface de cadastro de hospedeiros...")
                time.sleep(2)
                insert_hospedeiro()
            case 3:
                print("Carregando a interface de transformação hipotética em zumbi...")
                time.sleep(2)
                transformar_zumbi()
            case 4:
                print(f"Carregando a história do {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim{Style.RESET_ALL}...")
                time.sleep(2)
                contar_historia()
            case 0:
                print(f"O {Fore.BLUE}sistema administrador de hospedeiros, ou algo assim{Style.RESET_ALL} está sendo encerrado...")
                time.sleep(1)
                continuar = False


if __name__ == '__main__':
    main()