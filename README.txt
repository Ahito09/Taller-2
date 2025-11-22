
Eduardo Ignacio Macaya Cortes

21.247.960-8


🏗️ ARQUITECTURA DEL SISTEMA - TECNOLOGÍAS COMPLETAS

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FRONTEND             │    │   FRONTEND            │    │   FRONTEND            │
│   Next.js 14           │    │   Next.js 14          │    │   Next.js 14          │
│   TypeScript           │    │   TypeScript          │    │   TypeScript          │
│   Tailwind CSS         │    │   Tailwind CSS        │    │   Tailwind CSS        │
│   React 18             │    │   React 18            │    │   React 18            │
│   localhost:3004       │    │   localhost:3004      │    │   localhost:3004      │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          │                      │                      │
┌─────────▼───────┐    ┌─────────▼───────┐    ┌─────────▼───────┐
│  API USUARIOS          │    │  API JUEGOS            │    │  COMENTARIOS          │
│  NestJS                │    │  Express.js            │    │  (Frontend)           │
│  TypeScript            │    │  JavaScript            │    │  localStorage         │
│  TypeORM               │    │  Sequelize             │    │  React State          │
│  class-validator       │    │  CORS                  │    │  Mobile First         │
│  localhost:3001        │    │  localhost:3001        │    │  Responsive           │
└─────────┬───────┘    └─────────┬───────┘    └─────────────────┘
          │                      │
          │                      │
┌─────────▼───────┐    ┌─────────▼───────┐
│  POSTGRESQL            │    │  POSTGRESQL           │
│  users_db              │    │  games_db             │
│  TypeORM               │    │  Sequelize            │
│  Migrations            │    │  Associations         │
└─────────────────┘    └─────────────────┘

📊 TECNOLOGÍAS POR CAPA

🎯 FRONTEND (Next.js + TypeScript)
├── Framework: Next.js 14 con App Router
├── Lenguaje: TypeScript
├── UI: React 18 + Hooks
├── Estilos: Tailwind CSS + CSS Modules
├── Iconos: Lucide React
├── Formularios: React Hook Form
├── HTTP Client: Axios
├── Estado: Context API + useState/useEffect
├── Routing: Next.js App Router
└── Diseño: Mobile First + Responsive

🚀 BACKEND - API 1: NESTJS (USUARIOS)
├── Framework: NestJS con Express
├── Lenguaje: TypeScript
├── ORM: TypeORM
├── BD: PostgreSQL
├── Validación: class-validator + class-transformer
├── Seguridad: CORS habilitado
├── Estructura: MVC + Modules
└── Puerto: 3001

🎮 BACKEND - API 2: EXPRESS (JUEGOS)
├── Framework: Express.js
├── Lenguaje: JavaScript/Node.js
├── ORM: Sequelize
├── BD: PostgreSQL
├── Middleware: CORS, JSON parsing
├── Validación: Manual + Sequelize
└── Puerto: 3001

🗄️ BASE DE DATOS
├── Motor: PostgreSQL
├── Instancias: 2 bases de datos separadas
├── ORMs: TypeORM (NestJS) + Sequelize (Express)
├── Relaciones: Soporte completo
├── Migraciones: TypeORM + Sequelize
└── Transacciones: ACID compliance

🔧 HERRAMIENTAS DE DESARROLLO
├── IDE: Visual Studio Code
├── API Testing: Thunder Client + curl
├── Control Versiones: Git
├── Package Managers: npm
└── Variables Entorno: .env

📡 PROTOCOLOS Y ESTÁNDARES
├── API: RESTful
├── Formato Datos: JSON
├── Comunicación: HTTP/HTTPS
├── CORS: Configurado para frontend
└── Autenticación: Session-based (planeado JWT)

🔐 API DE USUARIOS (NESTJS) - localhost:3001

📍 INFORMACIÓN TÉCNICA
Tecnología: NestJS + TypeScript + TypeORM
Base de datos: PostgreSQL (users_db)
Puerto: 3001
Prefijo: /api
ORM: TypeORM

🗂️ ESTRUCTURA DEL PROYECTO
api-nestjs/
├── src/
│   ├── entities/
│   │   └── user.entity.ts
│   ├── users/
│   │   ├── users.controller.ts
│   │   ├── users.service.ts
│   │   └── dto/
│   │       ├── create-user.dto.ts
│   │       └── update-user.dto.ts
│   ├── app.module.ts
│   └── main.ts

📊 ENDPOINTS DISPONIBLES

🔹 AUTENTICACIÓN
MÉTODO   ENDPOINT              DESCRIPCIÓN                  BODY
POST     /api/users/login      Iniciar sesión              {email, password}
POST     /api/users            Registrar nuevo usuario     {name, email, password}

🔹 GESTIÓN DE USUARIOS
MÉTODO   ENDPOINT              DESCRIPCIÓN
GET      /api/users            Obtener todos los usuarios
GET      /api/users/:id        Obtener usuario por ID
PUT      /api/users/:id        Actualizar usuario
DELETE   /api/users/:id        Eliminar usuario
GET      /api/users/health     Health check de la API

💾 MODELO DE DATOS - USER
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    isActive BOOLEAN DEFAULT true,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

🚀 EJEMPLOS DE USO

🔹 Registrar Usuario
curl -X POST http://localhost:3001/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "password": "123456"
  }'

🔹 Iniciar Sesión
curl -X POST http://localhost:3001/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan@example.com",
    "password": "123456"
  }'

🔹 Obtener Todos los Usuarios
curl http://localhost:3001/api/users

🎮 API DE JUEGOS (EXPRESS) - localhost:3001

📍 INFORMACIÓN TÉCNICA
Tecnología: Express.js + Sequelize + JavaScript
Base de datos: PostgreSQL (games_db)
Puerto: 3001
Prefijo: /api
ORM: Sequelize

🗂️ ESTRUCTURA DEL PROYECTO
api-express/
├── src/
│   ├── models/
│   │   └── Game.js
│   ├── routes/
│   │   └── games.js
│   ├── controllers/
│   │   └── gamesController.js
│   └── server.js

📊 ENDPOINTS DISPONIBLES

🔹 GESTIÓN DE JUEGOS
MÉTODO   ENDPOINT                  DESCRIPCIÓN                  PARÁMETROS QUERY
GET      /api/games                Obtener todos los juegos    category, platform, search, minPrice, maxPrice, minRating
GET      /api/games/:id            Obtener juego por ID        -
POST     /api/games                Crear nuevo juego           -
PUT      /api/games/:id            Actualizar juego            -
DELETE   /api/games/:id            Eliminar juego (soft delete) -

🔹 UTILIDADES
MÉTODO   ENDPOINT                  DESCRIPCIÓN
GET      /api/games/categories     Obtener categorías disponibles
GET      /health                   Health check de la API

💾 MODELO DE DATOS - GAME
CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    price DECIMAL(10,2) DEFAULT 0.00,
    rating DECIMAL(3,1) DEFAULT 0.0,
    platform TEXT[] DEFAULT ARRAY['PC'],
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

🔍 FILTROS DISPONIBLES
?category=aventura    - Filtrar por categoría
?platform=ps5         - Filtrar por plataforma  
?search=zelda         - Buscar en nombre
?minPrice=20&maxPrice=60 - Rango de precio
?minRating=4.5        - Rating mínimo

🚀 EJEMPLOS DE USO

🔹 Crear Juego
curl -X POST http://localhost:3001/api/games \
  -H "Content-Type: application/json" \
  -d '{
    "name": "The Legend of Zelda: Breath of the Wild",
    "category": "Aventura",
    "description": "Explora el vasto mundo de Hyrule",
    "releaseYear": 2017,
    "price": 59.99,
    "rating": 4.9,
    "platform": ["Nintendo Switch", "Wii U"]
  }'

🔹 Obtener Juegos con Filtros
curl "http://localhost:3001/api/games?category=aventura&minRating=4.5"

🔹 Obtener Categorías
curl http://localhost:3001/api/games/categories

💬 SISTEMA DE COMENTARIOS (FRONTEND)

📍 INFORMACIÓN TÉCNICA
Almacenamiento: localStorage del navegador
Persistencia: Por sesión de usuario
Estructura: Comentarios organizados por juego
Tecnología: React State + localStorage API

🗂️ ESTRUCTURA DE DATOS
interface Comment {
  id: string;           // Timestamp como ID único
  user_name: string;    // Nombre del usuario
  user_email: string;   // Email del usuario  
  content: string;      // Contenido del comentario
  rating: number;       // Calificación 1-5
  page_section: string; // Sección de la página
  created_at: string;   // Fecha de creación ISO
}

💾 ALMACENAMIENTO
Los comentarios se guardan en el localStorage con la clave:
`game_{gameId}_comments`

🔧 FUNCIONALIDADES
✅ Agregar comentarios con calificación (1-5 estrellas)
✅ Ver lista de comentarios organizados
✅ Eliminar comentarios propios
✅ Persistencia en el navegador (localStorage)
✅ Filtrado por juego específico
✅ Interfaz responsive y mobile-first

🚀 INSTALACIÓN Y CONFIGURACIÓN

🔹 PRERREQUISITOS
• Node.js 16 o superior
• PostgreSQL 12 o superior  
• npm o yarn
• Git

🔹 CONFIGURACIÓN DE BASES DE DATOS
-- Base de datos para usuarios
CREATE DATABASE users_db;

-- Base de datos para juegos  
CREATE DATABASE games_db;

🔹 VARIABLES DE ENTORNO

📍 API NESTJS (.env)
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=tu_password
DB_DATABASE=users_db

📍 API EXPRESS (.env)  
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres  
DB_PASSWORD=tu_password
DB_DATABASE=games_db
PORT=3001

🔹 INSTALACIÓN Y EJECUCIÓN

📍 API NESTJS (USUARIOS)
cd api-nestjs
npm install
npm run start:dev

📍 API EXPRESS (JUEGOS)  
cd api-express  
npm install
npm run dev

📍 FRONTEND NEXT.JS
cd frontend
npm install
npm run dev



🔹 VERIFICAR ESTADO DE LAS APIS
# Health Check NestJS
curl http://localhost:3001/api/users/health

# Health Check Express  
curl http://localhost:3001/health

# Listar usuarios
curl http://localhost:3001/api/users

# Listar juegos
curl http://localhost:3001/api/games


🔹 ACCESO A LA APLICACIÓN
Frontend: http://localhost:3004
API Usuarios: http://localhost:3001/api
API Juegos: http://localhost:3001/api

📞 PUERTOS EN USO
• 3004 - Frontend Next.js
• 3001 - APIs NestJS y Express
• 5432 - PostgreSQL

