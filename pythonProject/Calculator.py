
a = 0
token = []
operator = ''
operand = ''
while True:
    print('')
    print('현재 값 : ', a)
    token = input('작업 명령 입력 : ')
    arr = token.split()
    operator = arr[0]

    if len(arr) == 2 and (operator == '+' or operator == '*' or operator == '/' or operator == '%' or operator == '='):
        operand = float(arr[1])

        if operator == '=':
            a = operand

        elif operator == '+':
            a += operand

        elif operator == '*':
            a *= operand

        elif operator == '/':
            if operand == 0.0:
                print('잘못된 작업 명령(0으로 나누기)!!')
                continue
            a /= operand

        elif operator == '%':
            a %= operand

    else:
        if operator == 'x' and len(arr) == 1:
            break
        print('잘못된 작업 명령!!')