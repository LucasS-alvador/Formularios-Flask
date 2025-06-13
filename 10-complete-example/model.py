from config import *
from datetime import datetime


class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    def __str__(self):
        return f'{self.nome}, {self.email}, {self.telefone}'

class Carro(db.Entity):
    id = PrimaryKey(int, auto=True)
    marca = Required(str)
    modelo = Required(str)
    ano = Required(int)
    quilometros = Required(float)
    disponivel = Required(bool)
    preco = Required(float)
    cor = Required(str)
    dataRevisao = Required(datetime)
    placa = Required(str)
    numeroPortas = Required(int)



    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.ano}, {self.quilometros}, {self.disponivel}, {self.preco}, {self.cor}, {self.dataRevisao}, {self.placa}, {self.numeroPortas}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)