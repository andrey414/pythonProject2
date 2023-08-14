def generator_numbers(start, end):
    generator_numbers = []

    for num in range(start, end +1):
        generator_numbers.append(num)

    return generator_numbers

stat_range = int(input("Введите начальное число: "))
end_range = int(input("Введите конечное число: "))

generated_numbers = generator_numbers(stat_range, end_range)
print("Сгенерированные числа:", generated_numbers)