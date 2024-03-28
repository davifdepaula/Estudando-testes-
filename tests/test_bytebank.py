import sys
import pytest

from src.bytebank import Funcionario

class TestClass:

    def test_when_idade_receive_13_10_2000_should_return_22(self):
        birth_day = '05/09/1993'
        expect = 30

        employer_test = Funcionario('Luke', birth_day, 1111)
        
        age = employer_test.idade()

        assert age == expect

    def test_when_sobrenome_receive_Lucas_Carvalho_should_return_Carvalho(self):
        entry = 'Lucas Carvalho'
        expect = 'Carvalho'

        employer_test = Funcionario(entry, '13/10/2000', 1111)

        sobrenome = employer_test.sobrenome()

        assert sobrenome == expect


