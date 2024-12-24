# 1
total = sum(map(int, (input() for _ in range(4))))
print("Всего за 4 месяца:", total)
print("Среднее:", total / 4)


# 2
total = sum(
    int(input())
    for _prompt in (
        "Сколько стоит монитор",
        "Сколько стоит системный блок",
        "Сколько стоит мышка",
        "Сколько стоит клавиатура",
    )
)
print(f"Стоимость всех компов: {total * int(input())}")


# 3
print(int(input()) * 15_000 + int(input()) * 500)


# 4
print(int(input()) * 100 - int(input()) * 60)


# 5
m, l, d = map(int, (input() for _ in range(3)))
print(l + d, m - l - d, sep="\n")
