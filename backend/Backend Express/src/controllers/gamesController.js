const Game = require('../models/Game');
const { Op } = require('sequelize');

// GET - Todos los juegos con filtros
const getAllGames = async (req, res) => {
  try {
    const { category, platform, search, minPrice, maxPrice, minRating } = req.query;
    
    const whereConditions = { isActive: true };
    
    // Filtros
    if (category) {
      whereConditions.category = { [Op.iLike]: `%${category}%` };
    }
    
    if (platform) {
      whereConditions.platform = { [Op.contains]: [platform] };
    }
    
    if (search) {
      whereConditions.name = { [Op.iLike]: `%${search}%` };
    }
    
    if (minPrice || maxPrice) {
      whereConditions.price = {};
      if (minPrice) whereConditions.price[Op.gte] = parseFloat(minPrice);
      if (maxPrice) whereConditions.price[Op.lte] = parseFloat(maxPrice);
    }
    
    if (minRating) {
      whereConditions.rating = { [Op.gte]: parseFloat(minRating) };
    }

    const games = await Game.findAll({
      where: whereConditions,
      order: [['rating', 'DESC']]
    });

    res.json({
      success: true,
      count: games.length,
      data: games
    });
  } catch (error) {
    console.error('Error getting games:', error);
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

// GET - Juego por ID
const getGameById = async (req, res) => {
  try {
    const { id } = req.params;
    const game = await Game.findOne({ 
      where: { id, isActive: true } 
    });

    if (!game) {
      return res.status(404).json({
        success: false,
        message: 'Juego no encontrado'
      });
    }

    res.json({
      success: true,
      data: game
    });
  } catch (error) {
    console.error('Error getting game:', error);
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

// POST - Crear nuevo juego
const createGame = async (req, res) => {
  try {
    const { name, category, description, releaseYear, price, rating, platform } = req.body;

    // Validaciones
    if (!name || !category || !description) {
      return res.status(400).json({
        success: false,
        message: 'Nombre, categoría y descripción son obligatorios'
      });
    }

    const newGame = await Game.create({
      name,
      category,
      description,
      releaseYear: releaseYear || new Date().getFullYear(),
      price: price || 0,
      rating: rating || 0,
      platform: platform || ['PC']
    });

    res.status(201).json({
      success: true,
      message: 'Juego creado exitosamente',
      data: newGame
    });
  } catch (error) {
    console.error('Error creating game:', error);
    
    if (error.name === 'SequelizeValidationError') {
      return res.status(400).json({
        success: false,
        message: 'Datos de validación incorrectos',
        errors: error.errors.map(err => err.message)
      });
    }
    
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

// PUT - Actualizar juego
const updateGame = async (req, res) => {
  try {
    const { id } = req.params;
    
    const game = await Game.findOne({ where: { id } });
    
    if (!game) {
      return res.status(404).json({
        success: false,
        message: 'Juego no encontrado'
      });
    }

    const updatedGame = await game.update(req.body);

    res.json({
      success: true,
      message: 'Juego actualizado exitosamente',
      data: updatedGame
    });
  } catch (error) {
    console.error('Error updating game:', error);
    
    if (error.name === 'SequelizeValidationError') {
      return res.status(400).json({
        success: false,
        message: 'Datos de validación incorrectos',
        errors: error.errors.map(err => err.message)
      });
    }
    
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

// DELETE - Eliminar juego (soft delete)
const deleteGame = async (req, res) => {
  try {
    const { id } = req.params;
    
    const game = await Game.findOne({ where: { id } });
    
    if (!game) {
      return res.status(404).json({
        success: false,
        message: 'Juego no encontrado'
      });
    }

    await game.update({ isActive: false });

    res.json({
      success: true,
      message: 'Juego eliminado exitosamente'
    });
  } catch (error) {
    console.error('Error deleting game:', error);
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

// GET - Categorías disponibles
const getCategories = async (req, res) => {
  try {
    const categories = await Game.findAll({
      attributes: ['category'],
      group: ['category'],
      where: { isActive: true },
      raw: true
    });

    const categoryList = categories.map(item => item.category);

    res.json({
      success: true,
      count: categoryList.length,
      data: categoryList
    });
  } catch (error) {
    console.error('Error getting categories:', error);
    res.status(500).json({
      success: false,
      message: 'Error interno del servidor'
    });
  }
};

module.exports = {
  getAllGames,
  getGameById,
  createGame,
  updateGame,
  deleteGame,
  getCategories
};