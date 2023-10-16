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
}

module.exports = new HospedeiroController();
