from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("SpendByCustomer")
sc = SparkContext(conf = conf)

def parseFunc(cusomter):
    splitCustomer = cusomter.split(',')
    customerId = int(splitCustomer[0])
    amountSpent = float(splitCustomer[2])
    return (customerId, amountSpent)

input = sc.textFile("/Users/avinash/Desktop/spark/Spark RDDs examples and solutions/datasets/customer-orders.csv")
parsedInput = input.map(parseFunc)

amountSpentByCustomer = parsedInput.reduceByKey(lambda x, y: x + y).mapValues(lambda x: round(x))
flipped = amountSpentByCustomer.map(lambda x: (x[1], x[0]))
amountSpentSorted = flipped.sortByKey()


results = amountSpentSorted.collect()

for result in results:
    print(result)



