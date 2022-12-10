from datetime import datetime

SUBSRCIPTION_TYPES = {
    'basic': "BASIC",
    'premium': "PREMIUM"
}


class User:
    def __init__(self, first_name, last_name, email, subscription_type, subscription_end_date,
                 data_connector):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.subscription_type = subscription_type
        self.subscription_end_date = subscription_end_date
        self.data_connector = data_connector

    def has_unlimited_access(self):
        now = datetime.now()
        return self.subscription_type == SUBSRCIPTION_TYPES['premium'] and \
               self.subscription_end_date > now

# class EmployeeView -> show employee information, proxy action
#
# class Employee -> calculate salary, calculate vacation days, prepare information for
#       display. Initializize action (e.g. change email)
# class DBConnector -> save to db, get to db (execute queries).
#         Perform the action.
# class APIConnector

class Figure:
    def __init__(self, a, b, shape, c=None):
        self.a = a
        self.b = b
        self.shape = shape
        if shape == "triangle":
            self.c = c

    def calculate_area(self):
        if self.shape == 'rectangle':
            return self.a * self.b
        if self.shape == 'square':
            return self.a ** 2
        # if self.c...


#
#
#

class Vehicle:
    def accelerate(self):
        pass

    def slow_down(self):
        pass

    def turn(self, angle):
        pass


class Car(Vehicle):
    pass


class Bus(Vehicle):
    pass


# class Train(Vehicle):
    # def turn(self, angle):
        # ??????


# Vehicle -> Car
# Vehicle -> turn??????