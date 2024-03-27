import sys
import pytest

from src.bytebank import Funcionario

class TestClass:

    def test_when_data_13_10_2000_should_return_22(self):
        birth_day = '05/09/1993'
        expect = 30

        employer_test = Funcionario('Luke', birth_day, 1111)
        
        age = employer_test.idade()

        assert age == expect
