total_number = 0
white_spaces = 0
letters_and_numbers= 0
words = 0
sentences = 0
container_1 = ''
container_2 = ''
with open(r'C:\Users\Анастасия\Desktop\Учеба в ИТМО\программирование\lab1\steam_description_data.csv', encoding='utf-8') as f:
    for i in f:
        for j in i:
            total_number += 1
            if j == ' ':
                white_spaces += 1
            if j.isalnum() == 1:
                letters_and_numbers += 1
            if container_1.isalnum() == 1 and (j in ' .,!?'):
                words += 1
            container_1 = j
            if j not in '.!?':
                container_2 += j
            elif container_2 != '':
                sentences += 1
                container_2 = ''
print('Количество символов в файле:', total_number)
print('Количество символов без пробелов:', total_number - white_spaces)
print('Количество символов без знаков препинания:', letters_and_numbers + white_spaces)
print('Количество слов в файле:', words)
print('Количество предложений в файле:', sentences)