class log4j(object):
    def __init__(self, spark):
        """

        :param spark:
        """
        jvm_log4j = spark._jvm.org.apache.log4j
        self.logger = jvm_log4j.LogManager.getLogger("sbdl")

    def warn(self, message):
        """

        :param message:
        :return:
        """
        self.logger.warn(message)


    def info(self,message):
        """

        :param message:
        :return:
        """
        self.logger.info(message)

    def error(self, message):
        """

        :param message:
        :return:
        """
        self.logger.error(message)

    def debug(self, message):
        """

        :param message:
        :return:
        """
        self.logger.debug(message)
