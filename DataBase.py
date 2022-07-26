from tokenize import Double
from pony import orm
from pony.orm import Database, Required, Set, Json, PrimaryKey, Optional
from pony.orm.core import db_session
import datetime

db = Database('sqlite', 'db.test', create_db=True)
# db.bind(provider='sqlite', filename='//data/data/ru.travelfood.simple_ui/databases/SimpleWMS', create_db=True)


# Закупка;
class Ai_Purchase(db.Entity):
	name = Required(str)

# Упаковки (шт.);
class Ai_Pack(db.Entity):
	name = Required(str)

# Товары в закупке;
class Ai_Product(db.Entity):
	purch = Set('Ai_Purchase')
	pack  = Set('Ai_Pack')
	name  = Required(str)
	count = Required(int)


# Поступление;
class Ai_Receipt(db.Entity):
	name = Required(str)
	

def init():
    db.generate_mapping(create_tables=True) 