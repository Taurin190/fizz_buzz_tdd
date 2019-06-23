from unittest import TestCase
from main.fizz_buzz import FizzBuzz


class FizzBuzzTest(TestCase):
    def setUp(self):
        # 準備
        self.fizzbuzz = FizzBuzz()

class Test3の倍数を入力した時にFizzを返す(FizzBuzzTest):
    def test_3を入力した時にFizzで返す(self):
        # 実行 & 検証
        self.assertEqual("Fizz", self.fizzbuzz.get_fizzbuzz(3))

    def test_99を入力した時にFizzで返す(self):
        # 実行 & 検証
        self.assertEqual("Fizz", self.fizzbuzz.get_fizzbuzz(99))


class Test5の倍数を入力した時にBuzzを返す(FizzBuzzTest):
    def test_5を入力した時にBuzzで返す(self):
        # 実行 & 検証
        self.assertEqual("Buzz", self.fizzbuzz.get_fizzbuzz(5))

    def test_100を入力した時にBuzzで返す(self):
        # 実行 & 検証
        self.assertEqual("Buzz", self.fizzbuzz.get_fizzbuzz(100))


class Test15の倍数を入力した時にFizzBuzzを返す(FizzBuzzTest):
    def test_15を入力した時にFizzBuzzで返す(self):
        # 実行 & 検証
        self.assertEqual("FizzBuzz", self.fizzbuzz.get_fizzbuzz(15))

    def test_90を入力した時にFizzBuzzで返す(self):
        # 実行 & 検証
        self.assertEqual("FizzBuzz", self.fizzbuzz.get_fizzbuzz(90))


class Testその他の値を入れた時にそのまま文字列を返す(FizzBuzzTest):
    def test_1を入力した時に文字列で返す(self):
        # 実行 & 検証
        self.assertEqual("1", self.fizzbuzz.get_fizzbuzz(1))

    def test_98を入力した時に文字列で返す(self):
        # 実行 & 検証
        self.assertEqual("98", self.fizzbuzz.get_fizzbuzz(98))
