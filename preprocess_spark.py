import pyspark
import json
import sys
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline 
from sparkTransform import SparkTweetTokenizer, TweetCleaner

spark = SparkSession \
		.builder \
		.appName("preprocessor") \
		.getOrCreate()
df = spark.read.json(sys.argv[1])

clean = TweetCleaner(inputCol="content", outputCol="cleaned")
tokenize = SparkTweetTokenizer(inputCol="cleaned", outputCol="tokenized")

pipeline = Pipeline(stages=[clean, tokenize])
model = pipeline.fit(df).transform(df)

model.write.mode('overwrite').save(sys.argv[1].split("/")[0] + "/output/"+sys.argv[1].split("/")[1], format="json")


	