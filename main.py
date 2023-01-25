# ORM - Object Relational Mapping) - обектьно реляционное отображение) - технология которая сязывает БД с концепсиями обьектно ориентироапнных языков программирования . 
# OTM - прослойка между БД и кодом который пишет программист , которая позволяет создавать прграмме обьекты обновлять, удалять и получать их.
# Python:
# peewee
# sqlalchemy
# Gjango ORM

# Kласс - Таблица в БД
# Атрибут класса - полу в БД
# Обьекты класса - строка в таблице


from views import *
from settings import db

db.connect()

get_categories()
get_products()

# db.close()








#import peewee
# from peewee import PostgresqlDatabase
# from datetime import datetime



# Category.create_table()
# Product.create_table()

# category = Category(name='game')
# category.save()



# post_product('product1', 30, 10, 2)
# post_product('product2', 30, 10, 3)

# post_category('game')
# post_category('game2')
# get_categories()

# get_categories()
# delete_category(1)
# get_categories()

# get_categories()
# update_category(2, 'Sam')
# get_categories()

# detail_category(3)






































