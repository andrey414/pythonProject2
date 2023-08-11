data = input("Введите любые символы: ")
file = open("text_1.txt", "w")
file.writelines(data)
file.close()

def sum_numbers_in_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            for number in numbers:
                try:
                    total_sum += float(number)
                except ValueError:
                    pass

    return total_sum

file_path = 'text_1.txt'
result = sum_numbers_in_file(file_path)
print("Сумма всех чисел в файле:", result)


