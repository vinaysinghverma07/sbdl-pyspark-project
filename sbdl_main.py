import sys

from lib import utils
from lib.logger import log4j

if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: sbdl {local,qa,prod} {load date} : Arguments are missing")
        sys.exit(-1)

    job_run_env =  sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = utils.get_spark_session(job_run_env)
    logger = log4j(spark)

    logger.info("Finished creating spark session")
