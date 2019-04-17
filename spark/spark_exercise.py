devRDD = sc.textFile("/loudacre/devicestatus.txt")
devRDD.take(5)
delimitedRDD = devRDD. \
filter(lambda line: len(line) > 20). \
map(lambda line: line.split(line[19:20])). \
filter(lambda values: len(values) == 14)
delimitedRDD.take(5)

Result_devRDD = delimitedRDD. \
map(lambda values: (values[0], values[1].split(' ')[0], values[2], values[12], values[13]))
Result_devRDD.take(5)

Result_devRDD. \
map(lambda values: ','.join(values)). \
saveAsTextFile("/loudacre/devicestatus_etl")