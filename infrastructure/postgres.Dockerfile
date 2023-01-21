FROM postgres:11.5

COPY ./infrastructure/init-db.sh /docker-entrypoint-initdb.d/