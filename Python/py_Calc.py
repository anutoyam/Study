while True:
    print()
    print('[1] 더하기')
    print('[2] 빼기')
    print('[3] 곱하기')
    print('[4] 나누기')
    print('[5] 나가기')
    menu = input('메뉴를 선택하세요: ')

    if menu == '1':
        num1 = float(input('첫 번째 숫자를 입력하세요: '))
        num2 = float(input('두 번째 숫자를 입력하세요: '))
        result = num1 + num2
        print('결과: %.2f' % result)

    elif menu == '2':
        num1 = float(input('첫 번째 숫자를 입력하세요: '))
        num2 = float(input('두 번째 숫자를 입력하세요: '))
        result = num1 - num2
        print('결과: %.2f' % result)

    elif menu == '3':
        num1 = float(input('첫 번째 숫자를 입력하세요: '))
        num2 = float(input('두 번째 숫자를 입력하세요: '))
        result = num1 * num2
        print('결과: %.2f' % result)

    elif menu == '4':
        num1 = float(input('첫 번째 숫자를 입력하세요: '))
        num2 = float(input('두 번째 숫자를 입력하세요: '))
        result = num1 / num2
        print('결과: %.2f' % result)

    elif menu == '5':
        print('계산기를 종료합니다.')
        break