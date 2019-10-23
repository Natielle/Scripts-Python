from conversor_1 import converte_brl_to_eur, converte_eur_to_brl

assert 0.5 == converte_brl_to_eur(1)


# Fazendo a mesma coisa de cima com o unittest
# ----------------------------------------------------------------------------
import unittest

class TesteConverte(unittest.TestCase):
    def test_converte_brl_to_eur(self):
        self.assertEqual(0.5, converte_brl_to_eur(1))


# ----------------------------------------------------------------------------


# Fazendo a mesma coisa de cima com o pytest
# ----------------------------------------------------------------------------

import pytest
def test_converte_3_brl_to_2_eur(): # vai dar certo, entao nao mostra nada no terminal
    assert 3 == converte_brl_to_eur(2)

def test_converte_3_brl_to_2_eur(): # vai dar erro, entao mostra no terminal
    assert 4 == converte_brl_to_eur(2)


def test_converte_brl_to_eur():
    assert False


@pytest.mark.parametrize("eur, brl, abobrinha",
    [
        (1,2,0),
        (2,1,0)
    ]
)
