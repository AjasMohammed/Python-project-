
def binary(num):
    if num == 0:
        return 0
    else :
        res = num % 2 + 10 * binary (num // 2)
        return res
deci = int(input('Enter a Decimal Number : '))

print(binary(deci))
    
def decimal(num):
    sq = 0
    res = 0
    rev_num = num[::-1]
    for digit in rev_num :
        res += int(digit) * 2**sq
        sq += 1
    return res
binary = input('Enter a Binary digit : ')
print(decimal(binary))