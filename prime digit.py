priceItem = input()
prime_digits = {'2','3','5','7'}
discount = sum(int(digit)for digit in priceItem if digit in prime_digits)
print(discount)
