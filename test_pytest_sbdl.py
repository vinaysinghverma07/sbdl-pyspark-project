import pytest

from lib.utils import get_spark_session

@pytest.fixture(scope='session')
def spark():
    """
    def spark(spark): # Earlier it was this line and removed the spark since we are creating 1 for entire session
    Creates a single SparkSession instance for the entire test session.
    :return:
    """
    return get_spark_session("LOCAL")


def test_blank_test(spark):
    """

    :return:
    """
    print(spark.version)
    assert spark.version == "3.5.0" #3.3.0'
    # assert spark.version == "3.3.0'" This version is being used by author in video and it passed for him
