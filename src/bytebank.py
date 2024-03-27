from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        birth_day, birth_month, birth_year  = self._data_nascimento.split("/")
        actual_year, actual_month, actual_day = str(date.today()).split("-")
        
        if int(actual_month) <=  int(birth_month) and int(birth_day) <= int(actual_day):
            return int(actual_year) - int(birth_year) - 1
        
        return int(actual_year) - int(birth_year)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'