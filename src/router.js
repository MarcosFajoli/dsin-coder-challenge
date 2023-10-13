const express = require("express");
const HospedeiroController = require("./controllers/HospedeiroController");
const router = express.Router();

router.get("/hospedeiro", HospedeiroController.getAll);

module.exports = router;
