def Fibonachi_Number(n):
    if n == 1 or n == 2:
        return 1
    pre, cur =1, 1   # starting from f(1) and f(2)

    for i in range(3, n+1): #Start from 3
        next_num = pre + cur
        pre, cur = cur, next_num

    return cur

def main():
    n = int(input("Enter which Fibonacci numbers to compute: "))
    print("Fibonaci Number is: ", Fibonachi_Number(n))

main()

def Fibonacci_Recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n-2)

def main():
    n = int(input("Enter which Fibonacci recursive to compute: "))
    print("Fibonacci Recursive Output is: ", Fibonacci_Recursive(n))
main()