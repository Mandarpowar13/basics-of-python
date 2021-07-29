
def max_num(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


n1 = input("input number 1= ")
n2 = input("input number 2= ")
n3 = input("input number 3= ")
print(max_num(n1, n2, n3))
