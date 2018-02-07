#vhodnie dannie - 2 spiska
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

#zapros parametrov u polzovatelya. te, которые будем искать
numindex = int(input('Vevdite chislo: '))
wordindex = input('Vvedite slovo: ')
#переворачиваем списки сзаду наперёд
num_list.reverse()
word_list.reverse()
#вывод на экран для контроля перевёрнутых списков
print(num_list)
print(word_list)
#вывод искомого индекса последнего встречающегося элемента. т.е. перевернули список, 
#использовали функцию index и вычли индекс из длины списка для коррекции
print((len(num_list) - 1) -  num_list.index(numindex))
print((len(word_list) - 1) -  word_list.index(wordindex))
