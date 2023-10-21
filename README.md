# dsin-coder-challenge

Projeto feito para a etapa bônus do DSIN Coder Challenge 2023. O sistema se propôe a resolver o 1° e 2° problema do desafio.

## Inicialização

O projeto é composto em duas partes, nesse mesmo repositório. Uma API feita em Javascript que pode ser utilizada independentemente, e uma interface de linha de comando desenvolvida em Python que consome essa API, sendo essa dependente que o servidor da API esteja rodando.

### API

Para iniciar, faça o clone do repositório e instale as dependências:

```bash
  npm i
```

Após isso, execute o seguinte comando para inicializar o servidor:

```bash
  npm start
```

Pronto. Agora a API está pronta para receber requisições.

### Interface 'main.py'

Conforme explicado acima, a Interface que consome a API é feita em Python e necessita que algumas bibliotecas sejam instaladas. Comando para instalação de todas:

```bash
  pip install requests
  pip install colorama
```

Para executar a interface, execute o seguinte comando:

```bash
  npm run start:system
```

ou

```bash
  python main.py
```

Após isso, a interface do Python irá abrir no CLI.

## Documentação da API

### Retorna todos os hospedeiros

```http
  GET /hospedeiro
```

Exemplo de resposta:

```json
[
    {
        "id": "Marcos",
        "idade": "19",
        "sexo": "M",
        "peso": "110",
        "altura": "175",
        "tipoSanguineo": "A",
        "gostoMusical": ["Sertanejo", "Eletronica"],
        "esporte": ["Basquete", "eSports"],
        "jogoPreferido": ["LeagueOfLegends", "Dota"]
    }
]
```

### Insere um hospedeiro

```http
  POST /hospedeiro
```

Modelo de corpo da requisição:

```json
{
    "id": "1",
    "idade": "60",
    "sexo": "M",
    "peso": "80",
    "altura": "190",
    "tipoSanguineo": "A",
    "gostoMusical": ["Rock", "Pop", "Funk"],
    "esporte": ["Futebol"],
    "jogoPreferido": ["Minecraft"]
}
```

Exemplo de resposta:

```json
"1" // retorna o ID
```

### Classifica um hospedeiro para zumbi

```http
  GET /zumbi/:id
```

| Parâmetro | Tipo     | Descrição                                                    |
| :-------- | :------- | :----------------------------------------------------------- |
| `id`      | `string` | **Obrigatório**. O ID hospedeiro que você deseja classificar |

Exemplo de resposta:

```json
{
    "id": "1",
    "idade": "60",
    "peso": "80",
    "altura": "190",
    "forca": 70,
    "velocidade": 75,
    "inteligencia": 84,
    "especiais": [
        {
            "Zomb Old": "Esse zumbi viveu por muitos anos, ele é..."
        }
    ]
}
```

## Autores

-   Marcos Fajoli de Almeida - [@marcosfajoli](https://github.com/MarcosFajoli)
