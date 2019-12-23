def gather_info():
    height = float(input("enter height: "))
    weight = float(input("enter weight"))
    unit = 'is the above metrices in metric or imperial'.lower().strip()
    return height, weight, unit


def calculate_bmi(height, weight, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2))

    else:
        bmi = 703 * (weight / (height * 2))
    print('your bmi is: ', bmi)


while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight, unit)
        break
    elif unit.startswith('m'):
        calculate_bmi(weight)
        break
    else:
        print('unit must be imperial or metric')
