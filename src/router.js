const express = require("express");
const HospedeiroController = require("./controllers/HospedeiroController");
const router = express.Router();

router.get("/hospedeiro", HospedeiroController.getAll);
router.get("/hospedeiro/:id", HospedeiroController.getOne);
router.post("/hospedeiro", HospedeiroController.insert);

module.exports = router;
