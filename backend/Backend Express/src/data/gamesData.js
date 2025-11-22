let games = [
  {
    id: 1,
    name: "The Legend of Zelda: Breath of the Wild",
    category: "Aventura",
    description: "Explora el vasto mundo de Hyrule en esta épica aventura",
    releaseYear: 2017,
    price: 59.99,
    rating: 4.9,
    platform: ["Nintendo Switch", "Wii U"]
  },
  {
    id: 2,
    name: "Cyberpunk 2077",
    category: "RPG",
    description: "Un RPG de mundo abierto en la distópica Night City",
    releaseYear: 2020,
    price: 49.99,
    rating: 4.2,
    platform: ["PC", "PS5", "Xbox Series X"]
  },
  {
    id: 3,
    name: "FIFA 24",
    category: "Deportes",
    description: "El simulador de fútbol más realista",
    releaseYear: 2023,
    price: 69.99,
    rating: 4.0,
    platform: ["PS5", "Xbox Series X", "PC"]
  },
  {
    id: 4,
    name: "Resident Evil 4 Remake",
    category: "Terror",
    description: "Reimaginación del clásico de terror de supervivencia",
    releaseYear: 2023,
    price: 59.99,
    rating: 4.8,
    platform: ["PS5", "Xbox Series X", "PC"]
  },
  {
    id: 5,
    name: "Minecraft",
    category: "Sandbox",
    description: "Crea y explora mundos infinitos",
    releaseYear: 2011,
    price: 26.95,
    rating: 4.7,
    platform: ["Todas las plataformas"]
  }
];

// Generar IDs automáticamente
let nextId = games.length + 1;

module.exports = { games, nextId };