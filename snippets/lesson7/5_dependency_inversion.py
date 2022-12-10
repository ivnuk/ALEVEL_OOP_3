"""
5. Принцип інверсії залежностей

Він складається з двох тверджень:
- високорівневі модулі не повинні залежати від низькорівневих. І ті, і ті мають залежати від абстракцій;
- абстракції не мають залежати від деталей реалізації. Деталі реалізації повинні залежати від абстракцій.
"""


class BaseSender:
    def send(self, send_to, message):
        raise NotImplementedError


class SMSSender:
    def send(self, send_to, message):
        pass


class EmailSender:
    def send(self, send_to, message):
        pass


class SQLReader:
    def get_users_to_notify(self):
        return []

    def get_notification_text(self):
        return "text"


class APIReader:
    def get_users_to_notify(self):
        return []

    def get_notification_text(self):
        return "text"


class Notifier:
    def __init__(self, data_receiver, sender):
        self.data_receiver = data_receiver
        self.sender = sender

    def send_notification(self):
        recipients_list = self.data_receiver.get_users_to_notify()
        text = self.data_receiver.get_notification_text()
        for recipient in recipients_list:
            self.sender.send(recipient['send_to'], text)


if __name__ == '__main__':
    reader = APIReader()
    notif_sender = SMSSender()
    Notifier(reader, notif_sender).send_notification()
