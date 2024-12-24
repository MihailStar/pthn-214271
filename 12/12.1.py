# 1
total = sum(
    int(input())
    for _prompt in (
        "Стоимость монитора",
        "Стоимость системного блока",
        "Стоимость мышки",
        "Стоимость клавиатуры",
    )
)
print(f"Стоимость компа: {total}")


# 2
number = int(input())
print(f"Предыдущее число: {number - 1}")
print(f"Следующее число: {number + 1}")
