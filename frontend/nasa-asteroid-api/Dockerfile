# Usa la imagen base de Node.js
FROM node:16

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el package.json y package-lock.json a la imagen
COPY package*.json ./


# Copia el resto de los archivos del proyecto a la imagen
COPY . .

# Instala las dependencias
RUN npm install

# Construye la aplicación de Nuxt
RUN npm run build

# Expone el puerto 3000 para que la aplicación sea accesible
EXPOSE 3000

ENV HOST 0.0.0.0

# Inicia la aplicación cuando el contenedor se ejecute
CMD [ "node", ".output/server/index.mjs" ]
