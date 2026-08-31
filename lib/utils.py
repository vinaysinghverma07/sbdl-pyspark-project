from pyspark.sql import SparkSession

def get_spark_session(env):
    """

    :return:
    """
    if env == "LOCAL":
        return SparkSession.builder\
            .config("spark.driver.extraJavaOptions",
                    "-Dlog4j.configuration=file:log4j.properties")\
            .master("local[2]")\
            .enableHiveSupport() \
            .appName("sbdl-local") \
            .config("spark.driver.host", "127.0.0.1") \
            .config("spark.driver.bindAddress", "127.0.0.1") \
            .getOrCreate()
    else:
        return SparkSession.builder\
            .enableHiveSupport()\
            .getOrCreate()
