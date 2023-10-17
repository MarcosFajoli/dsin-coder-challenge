const HospedeiroModel = require("../models/hospedeiroModel");

class ZumbiController {
    async convertZumbi(request, response) {
        const id = request.params.id;
        let hospedeiro;
        try {
            hospedeiro = await HospedeiroModel.getOne(id);
        } catch (error) {
            return response.status(500).json(error);
        }

        return response.status(200).json(hospedeiro.tipoSanguineo);
    }
}

module.exports = new ZumbiController();
