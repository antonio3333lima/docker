FROM node:18-alpine

LABEL maintainer="mateus"


HEALTHCHECK --interval=5s --timeout=2s --start-period=0s --retries=2 CMD curl -sf http://localhost:3000/ || exit 1

VOLUME [ "/var/nodeapp" ]


RUN adduser -h /var/nodeapp \
      -s /bin/bash \
      -D nodeapp && \
      apk update && apk add curl

WORKDIR /var/nodeapp

COPY . .
RUN chown nodeapp:nodeapp app.js

ARG VERSION
ENV VERSION=${VERSION:-1.0.0}

USER nodeapp
ENTRYPOINT [ "node" ]
CMD [ "app.js" ]
