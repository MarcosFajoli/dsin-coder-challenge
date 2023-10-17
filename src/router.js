const express = require("express");
const HospedeiroController = require("./controllers/HospedeiroController");
const ZumbiController = require("./controllers/ZumbiController");
const router = express.Router();

router.get("/hospedeiro", HospedeiroController.getAll);
router.get("/hospedeiro/:id", HospedeiroController.getOne);
router.post("/hospedeiro", HospedeiroController.insert);

router.get("/zumbi/:id", ZumbiController.convertZumbi);

module.exports = router;
