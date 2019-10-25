def receive_complaint (x):
    file = open (f'google_{x}.txt', 'w')

    file.write(input('Оставьте свой отзыв: '))
    file.close()
    print('Спасибо!')
    # with open(name_doc, 'w') as file:
    #     complaint = input('Оставьте свой отзыв: ')
    #     file.write(complaint)
    #     print('Спасибо!')

# greetings = input('Для начала диалога нажмите -Enter- ')
# if greetings == '':
#     print("""Здравствуйте! Выберите из списка офис: 
# Казахстан
# Париж
# ЮАР
# Кыргызстан
# Сан-Франциско
# Германия
# Москва
# Швеция""")
#     answer = input('').lower()

#     if answer == 'казахстан':
#         receive_complaint(answer)
#     elif answer == 'париж':
#         receive_complaint(answer)
#     elif answer == 'юар':
#         receive_complaint(answer)
#     elif answer == 'кыргызстан':
#         receive_complaint(answer)
#     elif answer == 'сан-франциско':
#         receive_complaint(answer)
#     elif answer == 'германия':
#         receive_complaint(answer)
#     elif answer == 'москва':
#         receive_complaint(answer)
#     elif answer == 'швеция':
#         receive_complaint(answer)
#     else:
#         print('К сожалению, в указаном городе нет офиса.')


def receive_complain (x):
    with open(f'google_{x}.txt', 'w') as file:
        file.write(input('Give your complain here: '))
        print('Thank you!')

while True:
    greetings = input('Say "Hello" ').lower().strip()

    try: 
        if greetings == 'hello':
            print("""Hello! Pls, choice your office: 
    Kazakstan
    Paris
    UAR
    Kyrgyzstan
    San-Francisco
    Germany
    Moscow
    Sweden""")
            answer = input('').lower().strip()

            if answer == 'kazakstan':
                receive_complain(answer)
            elif answer == 'paris':
                receive_complain(answer)
            elif answer == 'uar':
                receive_complain(answer)
            elif answer == 'kyrgyzstan':
                receive_complain(answer)
            elif answer == 'san-francisco':
                receive_complain(answer)
            elif answer == 'germany':
                receive_complain(answer)
            elif answer == 'moscow':
                receive_complain(answer)
            elif answer == 'sweden':
                receive_complain(answer)
        break
    except ValueError:
            print('Error')
