FROM node:21 AS buil

WORKDIR /app

COPY ./ ./ 

RUN npm install
RUN npm install -D @sveltejs/adapter-static

RUN npm run build 
EXPOSE 4173
CMD ["npm", "run", "preview", "--", "--host"]

# FROM nginx:1.23-alpine

# COPY --from=buil /app/build /usr/share/nginx/html
# COPY index.html /usr/share/nginx/html

