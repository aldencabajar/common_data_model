FROM rocker/tidyverse:4.0

WORKDIR /app
RUN apt-get update -y
RUN apt-get install default-jdk -y


RUN Rscript -e 'remotes::install_github("OHDSI/ETL-Synthea")'
COPY ./infrastructure/scripts/setup-dependencies.R .
RUN Rscript setup-dependencies.R
COPY ./infrastructure/scripts/synthea-etl.R .

CMD Rscript synthea-etl.R