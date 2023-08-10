class Widget():
    #властивості класа (в конструкторі)
    def __init__(self,text,x,y) :
    #методи
        self.text = text
        self.x = x
        self.y = y

    def print_info(self):
        print('Напис:',self.text)
        print('Розташування:',self.x,self.y)

class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self, text, x, y, is_clicked):
        super().__init__(self, x, y)
        self.is_clicked = is_clicked 
    #нові методи
    def click(self):
        self.is_clicked = True
        print('зареєстрований')
#створи екземпляр класа Button
q = Button('брати участь',100,100,False)
q.print_info()
#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click
w = input('Записати?')

if w == 'Так':
      q.click()
else:
      print('!!')
    
            
      