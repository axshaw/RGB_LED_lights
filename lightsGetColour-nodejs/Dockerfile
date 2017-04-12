FROM node:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN mkdir -p /home/pi/kidsLights
ADD ./package.json /usr/src/app/package.json
RUN npm -g install nodemon
RUN npm install


EXPOSE 3010

CMD ["nodemon","/usr/src/app/app.js"]
