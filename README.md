# This directory is for spark related work.

## Installation :

#### 1. Install Anaconda

https://www.anaconda.com/download

#### 2. Install Java11

```
brew install java11
```

Note: Install Homebrew in case if it's not installed already,
/usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”

#### 3. Install Pyspark:

```
brew install apache-spark
```

After installing spark:

- Create a log4j2.properties file via:
  1. `cd /usr/local/Cellar/apache-spark/2.0.0/libexec/conf` (substitute 2.0.0 for the version actually installed)
  2. `cp log4j2.properties.template log4j2.properties`
- Edit the log4j2.properties file and change the log level from INFO to ERROR on `lrootLogger.level = ERROR`.It’s OK if Homebrew does not install Spark 3; the code in the course should work fine with recent 2.x releases as well.

Test if everything works fine:

1. Open up a terminal
2. cd into the directory where you installed Spark, and then ls to get a directory listing.
3. Look for a text file we can play with, like README.md or CHANGES.txt
4. Enter pyspark
5. At this point you should have a >>> prompt. If not, double check the steps above.
6. Enter rdd = sc.textFile(“README.md”) (or whatever text file you’ve found) Enter rdd.count()
7. You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
8. Enter quit() to exit the spark shell, and close the terminal window
9. You’ve got everything set up! Hooray!

Datasets:
ml-100k -> MovieLens 100K Dataset -> finding distribution of movies across different ratings
