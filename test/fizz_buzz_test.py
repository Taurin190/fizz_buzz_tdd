from unittest import TestCase
from main.fizz_buzz import FizzBuzz


class FizzBuzzTest(TestCase):
    def test_1を入力した時に文字列で返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        self.assertEqual("1", fizzbuzz.get_fizzbuzz(1))

    def test_3を入力した時にFizzで返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        self.assertEqual("Fizz", fizzbuzz.get_fizzbuzz(3))

    def test_5を入力した時にFizzで返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        self.assertEqual("Buzz", fizzbuzz.get_fizzbuzz(5))
