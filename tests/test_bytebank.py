import sys
import pytest

from src.bytebank import Funcionario

class TestClass:

    def test_when_idade_receive_13_10_2000_should_return_22(self):
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

    def test_whemn_adjust_salary_receive_100000_should_retorn_90000(self):
        entry = 100000
        entry_cargo = 'diretor'
        expect = 90000

        employer_test = Funcionario("Luke Skywalker", '13/10/2000', entry, entry_cargo)

        new_salary = employer_test.adjust_salary()
        new_salary = employer_test.salario
        
        assert new_salary == expect
        
