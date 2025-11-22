const express = require('express');
const router = express.Router();

const {
  getAllGames,
  getGameById,
  createGame,
  updateGame,
  deleteGame,
  getCategories
} = require('../controllers/gamesController');

// Rutas principales
router.get('/', getAllGames);
router.get('/categories', getCategories);
router.get('/:id', getGameById);
router.post('/', createGame);
router.put('/:id', updateGame);
router.delete('/:id', deleteGame);

module.exports = router;