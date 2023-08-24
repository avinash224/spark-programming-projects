from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("/Users/avinash/Desktop/spark/Spark RDDs examples and solutions/datasets/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))

# to run this -> spark-submit ratings-counter_ml_100k.py
# output: 
# 1 6110
# 2 11370
# 3 27145
# 4 34174
# 5 21201