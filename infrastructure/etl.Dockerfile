FROM r-base:3.6.3

WORKDIR /app

COPY ./infrastructure/scripts  ./scripts
RUN Rscript ./scripts/setup-dependencies.R
# RUN Rscript ./scripts/synthea-etl.R
