
class Calculator:

    def addition(self, *nums):
        sum = 0
        for num in nums:
            sum += num
        return sum

    def subtraction(self, *nums):
        sum = 0
        for num in nums:
            sum -= num
        return sum