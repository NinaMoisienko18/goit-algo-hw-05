import re

def sum_profit(text, number_generator):
    total = 0
    for number in number_generator(text):
        total += float(number)
    return total

def generator_numbers(text):
    number_pattern = r"(\d+\.\d*)"
    digits = re.findall(number_pattern, text)
    for d in digits:
        yield d

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
