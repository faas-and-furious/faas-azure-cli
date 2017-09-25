FROM python:3.5.2-alpine

RUN apk --no-cache add curl \ 
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/alexellis/faas/releases/download/0.6.1/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache

RUN apk update && \
    apk add bash py-pip && \
    apk add --virtual=build gcc libffi-dev musl-dev openssl-dev make && \
    pip install azure-cli && \
    apk del --purge build

WORKDIR /root/

COPY index.py           .

RUN mkdir function

RUN touch ./function/__init__.py

WORKDIR /root/function/
COPY handler.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /root/

ENV fprocess="python index.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
