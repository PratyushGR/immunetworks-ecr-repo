FROM node

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . /app

ENV PORT=3001

EXPOSE ${PORT}

CMD ["node","App.js"]
