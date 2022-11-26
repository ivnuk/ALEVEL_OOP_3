from employees.empl_exceptions import EmailAlreadyExistsException
from employees.employee import Employee

import datetime

def main():
    emp1 = Employee()


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        pass
        # write traceback to the logs txt
        # 1. with open...
        # 2. message = f"{datetime.date.today()}
        # {datetime.datetime.now().hour}:
        # {datetime.datetime.now().minute} {traceback.format_exc}"
        # 3. log a message in the file
        # 3*. implement with logging https://docs.python.org/3/library/logging.html
