FROM node:19 as build

ENV NODE_ENV=production 


WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
COPY vite.config.js ./
RUN npm install
RUN npm i @esbuild/linux-x64@0.18.20

COPY . ./
RUN npm run build


FROM node:19-alpine3.16
RUN mkdir /app
WORKDIR /app
COPY --from=build /app .
