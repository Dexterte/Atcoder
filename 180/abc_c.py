_n = int(input())


def make_divisors(n: int):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans_list = make_divisors(_n)
for ans in ans_list:
    print(ans)
