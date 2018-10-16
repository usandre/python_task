# -*- coding: utf-8 -*-

"""
 @author  andre 
"""

class showcase():
    def __init__(self, title, number_of_items, item_price):
        self.title = title
        self.number_of_items = number_of_items
        self.item_price = item_price

    def add_items(self, number_of_items):
        self.number_of_items += number_of_items

    def remove_items(self, number):
        self.number_of_items -= number

class user():
    def __init__(self, first_name, family_name, last_name):
        self.first_name = first_name
        self.family_name = family_name
        self.last_name = last_name


class buyer(user):

    def set_buyer_data(self, address):
        self.balance = 0
        self.shiping_address = address

    def increase_balance(self, amount):
        self.balance += amount
        return self.balance

    def buy_item(self, number, showcase):

        purchase_price = showcase.item_price * number
        purchase_success = True

        #- хватает ли товаров на витрине.
        if showcase.number_of_items < number:
            purchase_success = False
            print('Было запрошено ' + str(number) + ' единиц товара ' + showcase.title + ', но на витрине присутствует только ' + str(showcase.number_of_items) + ' единиц')
        # - хватает ли покупателю денег на желаемое количество товара;
        if purchase_price > self.balance:
            purchase_success = False
            print('Было запрошено товаров на сумму: ' + str(purchase_price)  + ', но на балансе всего: ' + str(self.balance))

        if purchase_success == True:
            print('Showcase before: ' + str(vars(showcase)))
            print('Buyer before: ' + str(vars(self)))

            self.balance -= purchase_price
            showcase.remove_items(number)

            print('Showcase after: ' + str(vars(showcase)))
            print('Buyer after: ' + str(vars(self)))

            print( str(number) + ' единиц товара: ' +  showcase.title + ' отправлены по адресу ' + self.shiping_address + '. С баланса списаны ' + str(purchase_price) +' рублей.')


class seller(user):

    def add_to_showcase(self, number, showcase):
        showcase.add_items(number)


# Создать пустую витрину для товара.
Iphone_Store = showcase('Iphone6', 0, 1300)

# Создать продавца.
Seller = seller('Jannett', 'Jansen', 'Doe')
# print(vars( Iphone_Store ))

# Затем продавец наполняет витрину некоторым количеством товара.
Seller.add_to_showcase(5, Iphone_Store)
# print(vars( Iphone_Store ))

# После чего создать покупателя.
Customer = buyer('John', 'Jonny', 'Smith')
Customer.set_buyer_data('Elm Street')

# Пополнить баланс покупателя и попытаться купить товар с витрины.
Customer.increase_balance(10000)
Customer.buy_item(4, Iphone_Store)
