const readline = require("readline");
const fs = require("fs");

class Hospedeiro {
    data = [];
    arquivo = "src/database/database.txt";

    constructor() {
        this.data = this.getAll();
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

            if (linhaNum == 1) return;

            const valores = linha.split(",");

            const pessoa = {
                id: valores[0],
                idade: valores[1],
                sexo: valores[2],
                peso: valores[3],
                altura: valores[4],
                tipoSanguineo: valores[5],
                gostoMusical: valores[6].split("-"),
                esporte: valores[7].split("-"),
                jogoPreferido: valores[8].split("-"),
            };

            this.data.push(pessoa);
        });

        return this.data;
    }

    getOne(id) {
        return new Promise((resolve, reject) => {
            let linhaNum = 0;
            let pessoaEncontrada = null;

            const leitor = readline.createInterface({
                input: fs.createReadStream(this.arquivo),
                output: process.stdout,
                terminal: false,
            });

            leitor.on("line", (linha) => {
                linhaNum++;

                if (linhaNum == 1) return;

                const valores = linha.split(",");

                const pessoa = {
                    id: valores[0],
                    idade: valores[1],
                    sexo: valores[2],
                    peso: valores[3],
                    altura: valores[4],
                    tipoSanguineo: valores[5],
                    gostoMusical: valores[6].split("-"),
                    esporte: valores[7].split("-"),
                    jogoPreferido: valores[8].split("-"),
                };

                if (pessoa.id === id) {
                    pessoaEncontrada = pessoa;
                    leitor.close();
                }
            });

            leitor.on("close", () => {
                if (pessoaEncontrada) {
                    resolve(pessoaEncontrada);
                } else {
                    reject("Pessoa não encontrada");
                }
            });
        });
    }
}

module.exports = new Hospedeiro();
