import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig ( format='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%a, %d of %b %Y %H:%M:%S',
                              filename="first.log",
                              filemode='w' )

        logger = logging.getLogger ()
        logger.setLevel ( logging.INFO )
        return logger
