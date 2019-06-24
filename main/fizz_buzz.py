class FizzBuzz:
    def get_fizzbuzz(self, num):
        if type(num) != int:
            return ""
        elif 0 >= num or num > 100:
            return ""
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 5 == 0:
            return "Buzz"
        elif num % 3 == 0:
            return "Fizz"
        return str(num)
