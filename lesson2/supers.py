import datetime


class DBUser:
    def __init__(self, connector):
        self.connector = connector

    def save(self):
        return self.connector.save()


class CustomDBUser(DBUser):
    def __init__(self, connector):
        super().__init__(connector)

    def save(self):
        self.last_update_at = datetime.datetime.now()
        return super(CustomDBUser, self).save()

