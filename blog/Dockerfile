FROM node:alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV REACT_APP_BACKEND_URL=
RUN npm run build

# Set the environment variable for serving the app
ENV REACT_APP_BACKEND_URL=localhost:3001
ENV PORT=3000

EXPOSE ${PORT}

# Serve the app on port 3000
CMD ["npm", "start"]




