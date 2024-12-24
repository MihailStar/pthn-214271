# 1
print(
    "Проводим урок на улице" if int(input()) > 14 else "Отогреваемся в спортзале",
    "!",
    sep="",
)


# 2
admin = "Малёк"
print(
    f"Здравствуй, {admin}, я так скучала"
    if input() == admin
    else f"Уходите, я вас не знаю",
    "!",
    sep="",
)


# 3
print(
    "Ютуб",
    "растёт!" if int(input()) + int(input()) > 1_000 else "замедляется...",
)


# 4
if int(input()) + int(input()) + int(input()) < 4:
    print("Можно ещё поиграть!")
else:
    print("Игр достаточно, лучше пойти кодить!")


# 5
if int(input()) + int(input()) - int(input()) <= 0:
    print("Ура, мы вкусно покушаем!")
else:
    print("Денег не хватает, сегодня без обеда.")
