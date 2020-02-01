# develop stage
FROM tiangolo/node-frontend:10 as develop-stage
WORKDIR /app
COPY package.json yarn.lock ./
COPY . .

# build stage
FROM develop-stage as build-stage
RUN yarn --pure-lockfile
RUN yarn build

# production stage
FROM nginx:1.17.3-alpine as production-stage
COPY --from=build-stage /app/build/ /usr/share/nginx/html
COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh ./

EXPOSE 80
CMD ["sh", "entrypoint.sh"]