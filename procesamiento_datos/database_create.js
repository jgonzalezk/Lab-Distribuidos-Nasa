const { MongoClient } = require('mongodb');

// Init data
const url = 'mongodb://localhost:27017';
const dbName = 'NASA_data';
const collectionName = 'asteroids';

// Create database and collection
async function createMongoDB() {
  const client = new MongoClient(url);

  try {
    await client.connect();
    const db = client.db(dbName);
    await db.createCollection(collectionName);
    console.log('La base de datos y la colección han sido creadas exitosamente.');

  } catch (error) {
    console.error('Error al crear la base de datos y la colección:', error);

  } finally {
    client.close();
  }
}
createMongoDB();