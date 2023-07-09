# Usa la imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el package.json y package-lock.json a la imagen
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos del proyecto a la imagen
COPY . .

# Construye la aplicación de Nuxt
RUN npm run build

# Expone el puerto 3000 para que la aplicación sea accesible
EXPOSE 3000

# Inicia la aplicación cuando el contenedor se ejecute
CMD [ "npm", "run", "start" ]
