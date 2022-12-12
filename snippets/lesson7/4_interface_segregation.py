"""
4. Принцип розділення інтерфейсу
Краще, коли є багато спеціалізованих інтерфейсів, ніж один загальний.
"""


class DataSource:
    def read(self):
        raise NotImplementedError


class RemoteDataSource:
    def connect(self):
        raise NotImplementedError


class DBSource(DataSource, RemoteDataSource):
    def connect(self):
        """implementation here"""

    def read(self):
        """implementation here"""


class FileSource(DataSource):
    def read(self):
        """implementation here"""


class APISource(DataSource, RemoteDataSource):
    def connect(self):
        """implementation here."""

    def read(self):
        """implementation here"""

# route -> controller
# api/v.1/user (UserController)
# api/v.2/user (NewUserController)
