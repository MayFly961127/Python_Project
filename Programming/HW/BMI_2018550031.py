def BMI(m,kg):
    """m is height in meters and kg is weight in kilograms"""
    BMI_num = kg/(m**2)
    BMI_num = round(BMI_num,1)
    return BMI_num

def BMI_expected(m,kg):
    """BMI_expected tells you how much weight you should lose if you are over-weight"""
    while True:
        BMI_num = BMI(m,kg)
        if BMI_num >= 23 and BMI_num <= 24.9:
            print(f'You should work out until your weight turns {kg}kg')
            break
        kg -= 1.0
def BMI_check(m, kg):
    """BMI_check tells you whether your BMI is normal or not"""
    BMI_num = BMI(m,kg)
    if BMI_num == 0.0:
        #In case users mistakenly typed their height in centimeters
        ask_mistake = input(f'Did you mistakenly type your height in centi meters like {m}cm y/[n]')
        if ask_mistake == 'y':
            m = m/100
            BMI_num = BMI(m, kg)
        elif ask_mistake == 'n':
            print('*Warning: we found error in your inputs!!')
            raise ValueError
    if BMI_num >= 18.5 and BMI_num <= 22.9:
        print(f'(BMI는 {BMI_num}) 저체중입니다. 더 열심히 드세요.')
    elif BMI_num >= 23 and BMI_num <= 24.9:
        print(f'(BMI는 {BMI_num}) 정상입니다. 지금 상태를 유지하세요.')
    elif BMI_num >= 25:
        if BMI_num <= 29.9:
            print(f'(BMI는 {BMI_num}) 1단계 비만입니다. 주의 하십시오.')
        elif BMI_num >= 30 and BMI_num <= 34.9:
            print(f'(BMI는 {BMI_num}) 2단계 비만입니다. 운동을 하십시오.')
        elif BMI_num >= 35:
            print(f'(BMI는 {BMI_num}) 고도 비만입니다. 운동과 식이조절을 권고드립니다')
        BMI_expected(m,kg)
height_ask = float(input('Please tell your height in meters'))
weight_ask = float(input('Please tell your weight in kg'))
BMI_check(height_ask, weight_ask)