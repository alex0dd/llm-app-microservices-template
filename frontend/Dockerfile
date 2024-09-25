FROM node:alpine as build

#COPY package.json package.json
#RUN npm install
#COPY . .
#RUN npm build

COPY nginx.conf nginx.conf
COPY index.html /dist/index.html

FROM nginx:stable-alpine

COPY --from=build /dist /usr/share/nginx/html
COPY --from=build ./nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]