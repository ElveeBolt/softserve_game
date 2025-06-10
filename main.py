import random

NUMBER = 100
ATTEMPTS = 7

def main():
    random_number = random.randint(1, NUMBER + 1)
    print(f'Вітаю! Я загадав число від 1 до {NUMBER}. Спробуйте вгадати його за {ATTEMPTS} спроб.')

    for i in range (ATTEMPTS):
        n = int(input('Введіть ваше припущення: \n'))

        if n == random_number:
            print(f'Ви вгадали! Це число {random_number}')
            break

        if n > random_number:
            print(f'Занадто велике!')

        if n < random_number:
            print(f'Занадто маленьке!')

        continue

    else:
        print(f'Ви не вгадали! Було загадано число {random_number}')

if __name__ == '__main__':
    main()
