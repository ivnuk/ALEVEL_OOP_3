import traceback

from lesson1.dz import Element

from lesson4.myexc import MyOwnException


class Calculate:
    def divide(self, a, b):
        return a / b


if __name__ == '__main__':
    calc = Calculate()

    # raise MyOwnException
    while 1:
        try:
            # Element(-2900, 232039)
            a = int(input("enter 'a':"))
            b = int(input("enter 'b':"))
            print("result is:", calc.divide(a, b))
        # except ValueError as err:
        #     print("Invalid Input")
        #     continue
        except ZeroDivisionError:
            print("Zero Division!")
        except MyOwnException as err:
            print(err.some_data)
            break
        except Exception:
            with open("test.txt", "a+") as fp:
                fp.write(traceback.format_exc() + '\n')
