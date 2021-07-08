FROM weblate/weblate:4.7.1-1

# install Node.js
USER root

RUN \
  export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install --no-install-recommends -y \
    nodejs \
    jq \
  && npm i -g gulp

COPY weblate_iobroker /app/iobroker/python/weblate_iobroker/

RUN chmod a+rx /app/iobroker/python/weblate_iobroker/scripts/*.sh

# Search path for our addons
RUN echo "/app/iobroker/python" > /usr/local/lib/python3.7/dist-packages/iobroker-weblate.pth

# switch back to user "weblate"
USER 1000
