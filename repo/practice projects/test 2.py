def is_prime(number):
    if number <= 1:
        return False  # 1 and non-positive numbers are not prime
    if number <= 3:
        return True   # 2 and 3 are prime

    # Check divisibility by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check divisibility for numbers of the form 6k ± 1
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

x = int(input('Hasta qué número quieres chequear?: '))

for n in range(1, x + 1):  # Change the range to include x
    if is_prime(n):
        print(n)



######## fibonacci

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.

    :param n: The number of Fibonacci numbers to generate.
    :return: A list containing the Fibonacci sequence.
    """
    fib_sequence = []
    a, b = 0, 1

    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

# Example usage:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
sequence = fibonacci(n)
print(sequence)





