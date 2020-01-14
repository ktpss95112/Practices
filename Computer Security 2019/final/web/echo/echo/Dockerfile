FROM node:12

# Create app directory
RUN mkdir -p /usr/src/app
RUN useradd appuser

WORKDIR /usr/src/app

COPY . .

RUN npm install
RUN echo "flag is here" > /flag

EXPOSE 49007

USER appuser:appuser
CMD [ "node", "app.js" ]
