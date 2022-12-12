"""
Class Employee is used for ... living here.
"""


class Employee:
    """
    Main Employee functionality class
    """

    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.data_connector = 'some object'
        self.validate()
        self.save_email()  # -> write email to file

    def save_email(self):
        """Open file in append mode a+. Write email."""

    def validate(self):
        """
        1. Read the file with emails.
        2. Check that self.email in file.
        3. If not: do nothing
        4. Else: raise EmailAlreadyExistsException
        :return:
        """
