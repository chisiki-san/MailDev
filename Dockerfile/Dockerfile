FROM djfarrelly/maildev

RUN apk add --update \
    gcc \
    make \
    g++ \
    python\
  && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

ENV NODE_ENV production

RUN npm install iconv --save
RUN npm prune
RUN npm cache clean --force
RUN rm -rf /tmp/*

CMD [ "/bin/maildev" ]
