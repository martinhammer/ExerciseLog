# Import stuff
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *

# Set up Spark
conf = SparkConf().setAppName( "exerciselog-generatejson" )
sc = SparkContext( conf = conf )
sqlContext = SQLContext( sc )

# Load the markdown input file and filter out first two rows
lines = sc.textFile( "data/markdown/sample.md" ).filter( lambda line: not( line.startswith( "Date" ) or line.startswith( "---" ) ) )
# Split lines into attributes
attrs = lines.map( lambda line: line.split( " | " ) )
# Generate RDD 
exerciseRDD = attrs.map( lambda attrs: ( attrs[0].split(" ")[0], attrs[0].split(" ")[1], attrs[1], attrs[2]) )

# for e in exerciseRDD.take(10):
# 	print e

# Define the schema 
schemaString = "DayOfWeek Date Description Location"
fields = [ StructField( fieldName, StringType(), True ) for fieldName in schemaString.split() ]
schema = StructType( fields )

# Apply the schema
exerciseSchema = sqlContext.createDataFrame( exerciseRDD, schema )

# for e in exerciseSchema.take(10):
# 	print e

# Save as JSON
exerciseSchema.write.mode( "overwrite" ).save( "data/json/sample", format = "json" )
