with open ('quotes.txt','r',encoding='utf-8')as file:
    print(file.read())

author = input('Введіть автора')
with open ('quotes.txt','a',encoding='utf-8')as file:
    file.write(author)

add = input('Хочете дадати цитату? так/ні')

if add == 'так':
    citata = input('Введіть цитату')
else:
    print('бувай')


with open ('quotes.txt','a',encoding='utf-8')as file:
    print(file.write(citata))