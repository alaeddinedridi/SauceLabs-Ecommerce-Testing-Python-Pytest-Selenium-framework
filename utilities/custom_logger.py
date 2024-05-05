import logging

class LogGeneration:

    @staticmethod
    def generateLog():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p")

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
