import re
from pyspark import SparkConf, SparkContext

#function to set the case to lower - break up based on words and strip punctuations, transform to lower case
def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

#creating spark context 
conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("/Users/avinash/Desktop/spark/Spark RDDs examples and solutions/datasets/book.txt")
# setting each work as an individual entity in rdd 
words = input.flatMap(normalizeWords)

wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
results = wordCountsSorted.collect()

for result in results:
    count = str(result[0])
    word = result[1].encode('ascii', 'ignore')
    if (word):
        print(word.decode() + ":\t\t" + count)
