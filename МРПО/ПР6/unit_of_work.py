from sqlalchemy.orm import Session
from db_setup import setup_db

class UnitOfWork:
    def __init__(self):
        self.session: Session = setup_db()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()