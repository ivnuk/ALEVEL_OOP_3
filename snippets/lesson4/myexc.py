from datetime import datetime


class MyOwnException(Exception):
    def __init__(self, data):
        self.current_dt = datetime.now()
        self.some_data = data
        super().__init__()


class ThirdPartyServerException(Exception):
    pass
