def is_prime_number(number: int) -> bool:
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def find_all_prime_numbers_up_to_bound(upper_bound: int) -> list[int]:
    prime_numbers = []
    for number in range(1, upper_bound + 1):
        if is_prime_number(number=number):
            prime_numbers.append(number)

    return prime_numbers


def sieve_of_eratosthenes(upper_bound: int) -> list[int]:
    a = [i for i in range(upper_bound + 1)]

    for i in range(2, upper_bound + 1):
        if a[i] != 0:
            j = i * 2
            while j <= upper_bound:
                a[j] = 0
                j += i
        i += 1

    return [_ for _ in a if _ != 0]


def main():
    upper_bound = input(
        'Enter the number up to which you want to find all prime numbers. '
        'Number mustbe greater than 1: ',
    )
    if not upper_bound.isnumeric():
        print('You entered not a number.')
        return

    upper_bound = int(upper_bound)
    if upper_bound < 2:
        print('Number must be greater than 1')
        return

    print('Prime numbers with sqrt solution:', *find_all_prime_numbers_up_to_bound(upper_bound=upper_bound))
    print('Prime numbers with sieve_of_eratosthenes:', *sieve_of_eratosthenes(upper_bound=upper_bound))


if __name__ == '__main__':
    main()
