words = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
word = input('Введите слово: ')

if word in words:
    print('Синоним:', words[word])
else:
    print('Данного слова нет в списке.')