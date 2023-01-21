install.packages('remotes')
remotes::install_github("OHDSI/ETL-Synthea")

Sys.setenv("DATABASECONNECTOR_JAR_FOLDER", "/app/driver")

# download driver 
DatabaseConnector::downloadJdbcDrivers('postgres')
