"""
Створити @classmethod generate candidates, який приймає в якості аргументу шлях до файлу
Метод generate candidates має повертати список об’єктів класу Candidate
Файл тут (тиць)
** Розширити метод generate candidates, щоб він міг отримувати в якості аргументу URL на файл та генерувати кандидатів з нього
Можно використовувати цей URL:
https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv

"""
import csv


class Candidate:
    def __init__(self, first_name, last_name,
                 email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.__str__()

    @classmethod
    def generate_candidates(cls, path_to_file):
        res = []
        with open(path_to_file) as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                data = dict(first_name=row['Full Name'].split()[0],
                            last_name=row['Full Name'].split()[-1],
                            email=row['Email'],
                            tech_stack=row['Technologies'].split('|'),
                            main_skill=row['Main Skill'],
                            main_skill_grade=row['Main Skill Grade'])
                res.append(cls(**data))
        return res


if __name__ == '__main__':
    candidates = Candidate.generate_candidates('candidates.csv')
    print(candidates)
