"""
1. Принцип єдиного обов'язку.
Кожен клас має виконувати лише один обов'язок.
"""
from datetime import date, datetime

SUBSRCIPTION_TYPES = {
    'basic': "BASIC",
    'premium': "PREMIUM"
}


class User:
    def __init__(self, first_name, last_name, email, subscription_type, subscription_end_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.subscription_type = subscription_type
        self.subscription_end_date = subscription_end_date

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class AccessManager:
    def __init__(self, user: User):
        self.user = user

    def has_unlimited_access(self):
        now = datetime.now()
        return self.user.subscription_type == SUBSRCIPTION_TYPES['premium'] and \
               self.user.subscription_end_date > now

    def get_free_movies(self):
        movies = []
        return [x for x in movies if
                x.subscription_type == SUBSRCIPTION_TYPES['basic']]






