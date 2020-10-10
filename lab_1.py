with open(r'C:\Users\Анастасия\Desktop\Учеба в ИТМО\программирование\lab1\steam_description_data.csv', encoding='utf-8') as f:
    total_number = 0
    white_spaces = 0
    letters_and_numbers= 0
    words = 0
    sentences = 0
    container_1 = ''
    container_2 = ''
    for i in f:
        for j in i:
            total_number += 1
            if j == ' ':
                white_spaces += 1
            if j.isalnum() == 1:
                letters_and_numbers += 1
            if container_1.isalnum() == 1 and (j == ' ' or j == '.' or j == ',' or j == '!' or j == '?'):
                words += 1
            container_1 = j
            if j != '.' and j != '!' and j != '?':
                container_2 += j
            elif container_2 != '':
                sentences += 1
                container_2 = ''
print(total_number)
print(total_number - white_spaces)
print(letters_and_numbers + white_spaces)
print(words)
print(sentences)