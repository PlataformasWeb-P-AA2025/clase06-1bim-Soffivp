from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

#miSaludo = Saludo2()
#miSaludo.mensaje = "Hola que tal"
#miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
#session.add(miSaludo)
#session.add(miSaludo2)
with open("saludos_mundo.csv", newline='', encoding='utf-8') as saludos:
    lector = csv.DictReader(saludos)
    for fila in lector:
        cursor.execute('''
        
        ''', fila)

conn
# se confirma las transacciones
session.commit()


