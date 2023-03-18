FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY . /store/store

WORKDIR ./store/store

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]

