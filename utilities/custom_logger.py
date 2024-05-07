import logging

class LogGeneration:

    @staticmethod
    def generateLog():
        logging.basicConfig(filename=".\\Logs\\logs.txt",
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p")

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
