const hospedeiroModel = require("../models/hospedeiroModel");
const HospedeiroModel = require("../models/hospedeiroModel");

class HospedeiroController {
    getAll(_request, response) {
        const hospedeiros = HospedeiroModel.getAll();
        return response.status(200).json(hospedeiros);
    }

    async getOne(request, response) {
        const id = request.params.id;
        const hospedeiro = await HospedeiroModel.getOne(id);
        return response.status(200).json(hospedeiro);
    }

    insert(request, response) {
        const pessoa = request.body;
        const res = hospedeiroModel.insert(pessoa);

        if (!res.msg) return response.status(500).json(res);

        return response.status(200).json(res.return);
    }
}

module.exports = new HospedeiroController();
