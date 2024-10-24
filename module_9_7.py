def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result * 0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(*nums):
    return sum(nums)


result = sum_three(2, 3, 8)
print(result)