import sys
import pytest

from src.bytebank import Funcionario

class TestClass:

    def test_when_idade_receive_13_10_2000_should_return_22(self):
        entry = '13/2/2000'
        expect = 24

        employer_test = Funcionario('Luke', entry, 1111, 'contador')
        
        age = employer_test.idade()

        assert age == expect

    def test_when_idade_receive_05_09_1993_should_return_30(self):
        entry = '05/09/1993'
        expect = 30

        employer_test = Funcionario('Luke', entry, 1111, 'contador')
        
        age = employer_test.idade()

        assert age == expect

    def test_when_sobrenome_receive_Lucas_Carvalho_should_return_Carvalho(self):
        entry = 'Lucas Carvalho'
        expect = 'Carvalho'

        employer_test = Funcionario(entry, '13/10/2000', 1111, 'contador')

        sobrenome = employer_test.sobrenome()

        assert sobrenome == expect

    def test_when_adjust_salary_receive_100000_should_retorn_90000(self):
        entry = 100000
        entry_cargo = 'diretor'
        expect = 90000

        employer_test = Funcionario("Luke Skywalker", '13/10/2000', entry, entry_cargo)

        new_salary = employer_test.adjust_salary()
        new_salary = employer_test.salario
        
        assert new_salary == expect

    def test_when_calcula_bonus_receive_1000_should_retorn_100(self):
        entry = 1000
        expect = 100

        employer_test = Funcionario("Luke Skywalker", '13/10/2000', entry, 'diretor')

        bonus = employer_test.calcular_bonus()
        
        assert bonus == expect

    def test_when_calcula_bonus_receive_1000000000_should_retorn_exception(self):
        entry = 1000000000
        
        with pytest.raises(Exception):
            employer_test = Funcionario("Luke Skywalker", '13/10/2000', entry, 'diretor')

            bonus = employer_test.calcular_bonus()
            
            assert bonus

    def test_return_str(self):
        Name = 'Luke Skywalker'
        data = '13/10/2000'
        salario = 15000
        cargo = 'mestre jedi'

        expect = 'Funcionario(Luke Skywalker, 13/10/2000, 15000, mestre jedi)'
        employer_test = Funcionario(Name, data, salario, cargo)
        
        assert str(employer_test) == expect
        
