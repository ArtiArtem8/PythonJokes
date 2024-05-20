import logging
from abc import ABC

from ABCRepository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository, ABC):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    def __del__(self):
        logging.info("Closing session in __del__ method")
        self.session.close()
