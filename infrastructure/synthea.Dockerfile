FROM amazoncorretto:11 as javastage 

WORKDIR /app
RUN  yum install curl -y
RUN curl -LJ0 https://github.com/synthetichealth/synthea/releases/download/v3.0.0/synthea-with-dependencies.jar --output ./synthea.jar 





