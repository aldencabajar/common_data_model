 devtools::install_github("OHDSI/ETL-Synthea")

 library(ETLSyntheaBuilder)
 library()

 # We are loading a version 5.4 CDM into a local PostgreSQL database called "synthea10".
 # The ETLSyntheaBuilder package leverages the OHDSI/CommonDataModel package for CDM creation.
 # Valid CDM versions are determined by executing CommonDataModel::listSupportedVersions().
 # The strings representing supported CDM versions are currently "5.3" and "5.4". 
 # The Synthea version we use in this example is 2.7.0.  Since Synthea's MASTER branch is always active,
 # the only other version we support is 3.0.0.
 # The schema to load the Synthea tables is called "native".
 # The schema to load the Vocabulary and CDM tables is "cdm_synthea10".  
 # The username and pw are "postgres" and "lollipop".
 # The Synthea and Vocabulary CSV files are located in /tmp/synthea/output/csv and /tmp/Vocabulary_20181119, respectively.
 
 # For those interested in seeing the CDM changes from 5.3 to 5.4, please see: http://ohdsi.github.io/CommonDataModel/cdm54Changes.html
 
cd <- DatabaseConnector::createConnectionDetails(
  dbms     = "postgresql", 
  server   = "localhost/synthea10", 
  user     = "user1", 
  password = "lollipop", 
  port     = 5432, 
  pathToDriver = "d:/drivers"  
)

cdmSchema      <- "cdm_synthea10"
cdmVersion     <- "5.4"
syntheaVersion <- "2.7.0"
syntheaSchema  <- "native"
syntheaFileLoc <- "/tmp/synthea/output/csv"
vocabFileLoc   <- "/tmp/Vocabulary_20181119"

ETLSyntheaBuilder::CreateCDMTables(connectionDetails = cd, cdmSchema = cdmSchema, cdmVersion = cdmVersion)
