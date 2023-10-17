const HospedeiroModel = require("../models/hospedeiroModel");

class HospedeiroController {
    getAll(request, response) {
        const hospedeiros = HospedeiroModel.getAll();
        return response.status(200).json(hospedeiros);
    }

    async getOne(request, response) {
        const id = request.params.id;
        let hospedeiro;
        try {
            hospedeiro = await HospedeiroModel.getOne(id);
        } catch (error) {
            return response.status(500).json(error);
        }
        return response.status(200).json(hospedeiro);
    }

    insert(request, response) {
        const pessoa = request.body;
        const res = HospedeiroModel.insert(pessoa);
        return response.status(200).json(res);
    }
}

module.exports = new HospedeiroController();
