const readline = require("readline");
const fs = require("fs");

class Hospedeiro {
    data = [];
    arquivo = "src/database/database.txt";

    constructor() {
        const response = this.getAll();
    }

    getAll() {
        let linhaNum = 0;

        const leitor = readline.createInterface({
            input: fs.createReadStream(this.arquivo),
            output: process.stdout,
            terminal: false,
        });

        leitor.on("line", (linha) => {
            linhaNum++;

            if (linhaNum == 1 || linhaNum == 2) return;

            const valores = linha.split(",");

            const pessoa = {
                idade: valores[0],
                sexo: valores[1],
                peso: valores[2],
                altura: valores[3],
                tipoSanguineo: valores[4],
                gostoMusical: valores[5].split("-"),
                esporte: valores[6].split("-"),
                jogoPreferido: valores[7].split("-"),
            };

            // Adiciona o objeto ao array de dados
            this.data.push(pessoa);
        });

        return this.data;
    }
}

module.exports = new Hospedeiro();
