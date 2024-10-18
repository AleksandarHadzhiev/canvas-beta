"""Connecting to the database"""
from sqlmodel import SQLModel, Session, create_engine


class DBConnector:
    """DB Connector."""

    def __init__(self):
        """Construct the object."""
        self.sqlite_file_name = 'database.db'
        self.sqlite_url = f"sqlite:///{self.sqlite_file_name}"

        self.connect_args = {"check_same_thread": False}
        self.engine = create_engine(self.sqlite_url, connect_args=self.connect_args)

    def create_db_and_tables(self):
        """Create database and its tables."""
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        """Get the connection to the database.

        Yields:
            Session: the connection to the database.
        """
        with Session(self.engine) as session:
            yield session


db = DBConnector()
