const HospedeiroModel = require("../models/hospedeiroModel");

class HospedeiroController {
    getAll(request, response) {
        const hospedeiros = HospedeiroModel.getAll();
        return response.status(200).json(hospedeiros);
    }
}

module.exports = new HospedeiroController();
