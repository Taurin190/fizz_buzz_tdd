class FizzBuzz:
    def get_fizzbuzz(self, num):
        if num == 15:
            return "FizzBuzz"
        if num % 5 == 0:
            return "Buzz"
        if num % 3 == 0:
            return "Fizz"
        return str(num)
