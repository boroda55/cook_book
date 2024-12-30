from pprint import pprint
class Cook_book:
  def __init__(self):
    self.cook_book = {}

# Задание №1
  def basic_recipes(self):
    with open('cook_book.txt', 'r', encoding='utf-8') as f:
      x = 0
      key = ''
      for i in f.read().splitlines():
        if i != '':
          if x == 0:
            self.cook_book[i]=[]
            key = i
          if x > 1:
            cook = i.split(' | ')
            self.cook_book[key].append({'ingredient_name': cook[0] , 'quantity': cook[1] , 'measure': cook[2]})
          x += 1
        else:
          x = 0
    print(f'Функция по чтению из файла выполнена')

  # Задание №2
  def get_shop_list_by_dishes(self, dishes, person_count):
    shop_list = {}
    for dishe in dishes:
      for values in self.cook_book[dishe]:
        if shop_list.get(values['ingredient_name']) == None: # Проверка есть ли такой уже ингредиент
          shop_list[values['ingredient_name']] = {'quantity': int(values['quantity']) * person_count, 'measure': values['measure']}
        else:
          quantity = shop_list[values['ingredient_name']]['quantity']
          shop_list[values['ingredient_name']] = {'quantity': int(values['quantity']) * person_count + shop_list[values['ingredient_name']]['quantity']
          , 'measure': values['measure']}
    pprint(shop_list)








book1 = Cook_book()
print('Задание №1')
book1.basic_recipes() #Задание 1
pprint(book1.cook_book)
print('Задание №2')
book1.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) #Задание 2




