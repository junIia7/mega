import unittest
from main import main_function  # предполагаем, что в main.py есть такая функция

class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Добавьте здесь тесты для main_function
        pass

if __name__ == '__main__':
    unittest.main()