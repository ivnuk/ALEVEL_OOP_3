"""
* Зробити можливим передавати температуру та шкалу в метод з п.2

"""
from snippets.lesson4.myexc import MyOwnException


class Element:
    def __init__(self, t_melt, t_boil):
        if t_melt < -273:
            raise MyOwnException(dict(t_melt=t_melt, t_boil=t_boil, reason="Too cold"))
        self.t_melt = t_melt
        self.t_boil = t_boil

    def agg_state(self, temp, scale="C"):
        temp = self.convert_temp(temp, scale)
        if temp < self.t_melt:
            return "solid"
        if temp > self.t_boil:
            return "vapour"
        return "liquid"

    @staticmethod
    def convert_temp(temp, scale="C"):
        if scale == 'K':
            return temp - 273
        if scale == "F":
            return (temp - 32) * 5 / 9
        return temp


class SuperElement(Element):
    def __init__(self, t_melt, t_boil, t_plasm):
        super().__init__(t_melt, t_boil)
        self.t_plasm = t_plasm

    def agg_state(self, temp, scale="C"):
        temp = self.convert_temp(temp, scale)
        if temp > self.t_plasm:
            return "plasm"
        return super().agg_state(temp)


if __name__ == '__main__':
    water = Element(0, 100)
    print(Element.convert_temp(12, 'K'))
    print(water.convert_temp(150, 'F'))
    print(water.agg_state(150, 'F'))
