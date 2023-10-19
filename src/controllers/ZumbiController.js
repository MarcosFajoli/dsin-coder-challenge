const HospedeiroModel = require("../models/hospedeiroModel");
const {
    gostoMusical,
    esporte,
    jogoPreferido,
} = require("../utils/ClassifyIndexes");

class ZumbiController {
    async convertZumbi(request, response) {
        const id = request.params.id;
        let hospedeiro;
        try {
            hospedeiro = await HospedeiroModel.getOne(id);
        } catch (error) {
            return response.status(500).json(error);
        }

        /* 
            Cálculo realizado: cada informação escolhida tem três porcentagens agregadas no arquivo utils/ClassifyIndexes,
            que influencia no valor final da métrica do zumbi.

            {
                "gostoMusical": [
                    "Rock" [1, 0.7, 0.9]
                ],
                "esporte": [
                    "Futebol" [0.9, 0.9, 0.9]
                ],
                "jogoPreferido": [
                    "Minecraft" [0.6, 0.7, 0.7]
                ]
            }
            array[0] -> FORÇA
            array[1] -> VELOCIDADE
            array[2] -> INTELIGÊNCIA
        */

        // contador utilizado para calcular quantas porcentagens foram inseridas, para realizar a média.
        // começa em 3 para compensar as atribuições de porcentagem em idade, peso e altura.
        let count = 2;
        const FORCA = 0,
            VELOCIDADE = 1,
            INTELIGENCIA = 2;

        let forca = 100;
        let forcaPorcentagem = 0;

        let velocidade = 100;
        let velocidadePorcentagem = 0;

        let inteligencia = 80; //por padrão, menos inteligente
        let inteligenciaPorcentagem = 0;

        let especiais = [];

        // DEFINE AS CARACTERISTICAS DE IDADE
        if (hospedeiro.idade < 18) {
            // todos os atributos afetados negativamente
            forcaPorcentagem += 0.5;
            forca = 80;
            velocidadePorcentagem += 0.5;
            velocidade = 80;
            inteligenciaPorcentagem += 0.5;
            inteligencia = 80;
            especiais.push({
                "New Bie":
                    'Já ouviu falar sobre o efeito Dunning-Kruger? Então... Esses são os gênios (só que não). Um "New Bie" acha que consegue fazer várias coisas, mas ainda não aprendeu porcaria nenhuma. Tadinho, se tornou um zumbi tão cedo...',
            });
        } else if (hospedeiro.idade < 25) {
            // benefício em força e velocidade
            forcaPorcentagem += 1;
            velocidadePorcentagem += 1;
            inteligenciaPorcentagem += 0.8;
        } else if (hospedeiro.idade < 40) {
            // um pouco mais fraco e lento, mas mais inteligente
            forcaPorcentagem += 0.8;
            velocidadePorcentagem += 0.8;
            inteligenciaPorcentagem += 0.9;
        } else {
            // bem mais lento e fraco, mas sem decrécimo de inteligência e com média jogada pra cima
            forcaPorcentagem += 0.3;
            velocidadePorcentagem += 0.3;
            inteligencia = 100;
            inteligenciaPorcentagem += 1;
            especiais.push({
                "Zomb Old":
                    "Esse zumbi viveu por muitos anos, ele é fera nos pensamentos. Líder e filósofo nato, prefere caçar com armadilhas do que correr atrás de você. Se você viu ele, isso já estava em seus planejamentos e provavelmente você é uma pessoa morta (viva).",
            });
        }

        // DEFINE AS CARACTERISTICAS DE PESO
        if (hospedeiro.peso < 40) {
            forcaPorcentagem += 0.5;
            velocidadePorcentagem += 1;
            inteligenciaPorcentagem += 0.8;
            especiais.push({
                Magrão: 'Quem não tem um amigo chamado Magrão? Então, agora ele é um zumbi. o "ão" não se refere a sua ALTURA, e sim sua MAGREZA, capitche? Se for mulher, chame-a de Magrinha. Talvez ela não te mate.',
            });
        } else if (hospedeiro.peso < 100) {
            forcaPorcentagem += 0.8;
            velocidadePorcentagem += 0.8;
            inteligenciaPorcentagem += 0.8;
        } else {
            forcaPorcentagem += 1;
            velocidadePorcentagem += 0.1;
            velocidade = 70;
            inteligenciaPorcentagem += 1;
            especiais.push({
                "Gordão Gente Fina":
                    "O que falar do Gordão Gente Fina? Enquanto ainda era vivo, contava umas piadas como ninguém. Pena que sua força e apetite agora é direcionado aos humanos, e não ao McDonalds. Por sorte ele é bem mais lento, como de costume.",
            });
        }

        hospedeiro.gostoMusical.forEach((element) => {
            count++;
            forcaPorcentagem += gostoMusical[element.toLowerCase()][FORCA];
            velocidadePorcentagem +=
                gostoMusical[element.toLowerCase()][VELOCIDADE];
            inteligenciaPorcentagem +=
                gostoMusical[element.toLowerCase()][INTELIGENCIA];
        });

        hospedeiro.esporte.forEach((element) => {
            count++;
            forcaPorcentagem += esporte[element.toLowerCase()][FORCA];
            velocidadePorcentagem += esporte[element.toLowerCase()][VELOCIDADE];
            inteligenciaPorcentagem +=
                esporte[element.toLowerCase()][INTELIGENCIA];
        });

        hospedeiro.jogoPreferido.forEach((element) => {
            count++;
            forcaPorcentagem += jogoPreferido[element.toLowerCase()][FORCA];
            velocidadePorcentagem +=
                jogoPreferido[element.toLowerCase()][VELOCIDADE];
            inteligenciaPorcentagem +=
                jogoPreferido[element.toLowerCase()][INTELIGENCIA];
        });

        forca = Math.floor(forca * (forcaPorcentagem / count));
        velocidade = Math.floor(velocidade * (velocidadePorcentagem / count));
        inteligencia = Math.floor(
            inteligencia * (inteligenciaPorcentagem / count)
        );

        if (hospedeiro.tipoSanguineo == "Dourado") {
            hospedeiro.idade = null;
            hospedeiro.peso = null;
            hospedeiro.altura = null;
            forca = null;
            velocidade = null;
            inteligencia = null;
            especiais = [];
            especiais.push({
                "A Cura":
                    "FALE IMEDIATAMENTE COM A CENTRAL E PASSE SUA LOCALIZAÇÃO. VOCÊ ENCONTROU A RARIDADE, VOCÊ ENCONTROU O SANGUE DOURADO. ESSE ZUMBÍ É A CURA. DESAPEGUE DE SUA VIDA, POIS VOCÊ JÁ MORREU NA PRESENÇA DELE. FALE IMEDIATAMENTE COM A CENTRAL. REPITO, FALE IMEDIATAMENTE COM A CENTRAL.",
            });
        }

        return response.status(200).json({
            idade: hospedeiro.idade,
            peso: hospedeiro.peso,
            altura: hospedeiro.altura,
            forca: forca,
            velocidade: velocidade,
            inteligencia: inteligencia,
            especiais: especiais,
        });
    }
}

module.exports = new ZumbiController();
