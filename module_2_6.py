def generate_password(n):
    if n < 3 or n > 20:
        return "n должно быть в диапазоне от 3 до 20."
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result.append(f"{i}{j}")
    return ''.join(result)
n = int(input("Введите число от 3 до 20: "))
print(f"Сгенерированный пароль: {generate_password(n)}")
