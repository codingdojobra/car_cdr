from unittest import TestCase, main


def cons(number1, number2):
    def pair(f):
        return f(number1, number2)
    return pair


def car(pair):
    def f(number1, number2):
        return number1
    return pair(f)


def cdr(pair):
    def f(number1, number2):
        return number2
    return pair(f)


def soma(pair):
    def f(number1, number2):
        return (number1 + number2)
    return pair(f)


class TestFunction(TestCase):

    def test_is_callable(self):
        function_cons = cons(2, 3)
        self.assertTrue(hasattr(function_cons, '__call__'))

    def test_car(self):
        pair = cons(2, 3)
        self.assertEqual(2, car(pair))

    def test_cdr(self):
        pair = cons(2, 3)
        self.assertEqual(3, cdr(pair))

    def test_soma(self):
        pair = cons(2, 3)
        self.assertEqual(5, soma(pair))


if __name__ == '__main__':
    main()
