import unittest
# Импорт модуля, содержащего функции для тестирования
from utils.code import hello

# Название класса Testcalc - произвольное
class TestHello(unittest.TestCase):

    # Внутри пишем нужное количество методов (функций)
    def test_hello_normal(self):
        # Пишем нужное количество проверок
        self.assertEqual(hello('World'), 'Hello World')

if __name__ == '__main__':
    unittest.main()