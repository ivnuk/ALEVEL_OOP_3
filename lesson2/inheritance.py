class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(C, B):
    pass


class E(A):
    pass


class F(D, C):
    pass


if __name__ == '__main__':
    a = F()
    print(F.__mro__)
