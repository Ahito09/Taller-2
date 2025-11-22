const express = require('express');
const cors = require('cors');
require('dotenv').config();

const { testConnection } = require('./config/database');
const Game = require('./models/Game');
const gamesRoutes = require('./routes/games');

const app = express();
const PORT = process.env.PORT || 3001;

// Middlewares
app.use(cors());
app.use(express.json());

// Inicializar base de datos
const initializeDatabase = async () => {
  const connected = await testConnection();
  
  if (connected) {
    try {
      // Sincronizar modelos con la base de datos
      await Game.sync({ alter: true }); // Usa { force: true } solo en desarrollo para recrear tablas
      console.log('✅ Modelos sincronizados con la base de datos');
      
      // Datos de ejemplo (opcional)
      await seedDatabase();
    } catch (error) {
      console.error('❌ Error sincronizando modelos:', error);
    }
  }
};

// Datos de ejemplo
const seedDatabase = async () => {
  try {
    const gameCount = await Game.count();
    
    if (gameCount === 0) {
      await Game.bulkCreate([
        {
          name: "The Legend of Zelda: Breath of the Wild",
          category: "Aventura",
          description: "Explora el vasto mundo de Hyrule en esta épica aventura",
          releaseYear: 2017,
          price: 59.99,
          rating: 4.9,
          platform: ["Nintendo Switch", "Wii U"]
        },
        {
          name: "Cyberpunk 2077",
          category: "RPG",
          description: "Un RPG de mundo abierto en la distópica Night City",
          releaseYear: 2020,
          price: 49.99,
          rating: 4.2,
          platform: ["PC", "PS5", "Xbox Series X"]
        },
        {
          name: "FIFA 24",
          category: "Deportes",
          description: "El simulador de fútbol más realista",
          releaseYear: 2023,
          price: 69.99,
          rating: 4.0,
          platform: ["PS5", "Xbox Series X", "PC"]
        }
      ]);
      console.log('✅ Datos de ejemplo insertados');
    }
  } catch (error) {
    console.error('❌ Error insertando datos de ejemplo:', error);
  }
};

// Routes
app.use('/api/games', gamesRoutes);

// Ruta de salud
app.get('/health', async (req, res) => {
  const dbStatus = await testConnection() ? 'connected' : 'disconnected';
  
  res.json({ 
    status: 'OK',
    server: 'Express Games API',
    port: PORT,
    database: dbStatus,
    timestamp: new Date().toISOString()
  });
});

// Ruta de prueba
app.get('/', (req, res) => {
  res.json({ 
    message: '🎮 API de Juegos con PostgreSQL funcionando!',
    database: 'PostgreSQL',
    endpoints: {
      games: '/api/games',
      health: '/health'
    }
  });
});

// Iniciar servidor
app.listen(PORT, async () => {
  console.log(`🎮 Servidor de juegos corriendo en http://localhost:${PORT}`);
  console.log('📋 Inicializando base de datos...');
  
  await initializeDatabase();
  
  console.log(`🔍 Health check: http://localhost:${PORT}/health`);
  console.log(`🎯 Endpoints: http://localhost:${PORT}/api/games`);
});