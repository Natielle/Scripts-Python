from conversor_1 import converte_brl_to_eur, converte_eur_to_brl

# Fazendo a mesma coisa de cima com o pytest
# para executar esse codigo, executar pytest nome_arq.py
# ou pytest -v nome_arq.py
# ----------------------------------------------------------------------------

import pytest
def test_converte_22_brl_to_2_eur(): # vai dar certo, entao nao mostra nada no terminal
    assert 2.2 == converte_brl_to_eur(2)

def test_converte_3_brl_to_2_eur(): # vai dar erro, entao mostra no terminal
    assert 4 == converte_brl_to_eur(2)

def test_converte_brl_to_eur():
    assert False

# Passando parametros de forma mais dinamica para um teste
# Isso permite que nao tenha que fazer o mesmo teste para valores diferentes
@pytest.mark.parametrize("eur, brl, abobrinha",[
    (1,2,0),
    (2,1,0)
])
def test_convert_brl_to_eur(eur, brl, abobrinha):
    assert brl * .2 == converte_brl_to_eur(brl)


@pytest.mark.parametrize( "brl", range(10) )
def test_convert_brl_to_eur2(brl):
    assert brl * .5 == converte_brl_to_eur(brl)

# Verificando excecoes
def test_raise_error_on_none():
    with pytest.raises(TypeError):
        converte_brl_to_eur(None)

@pytest.mark.parametrize("invalid_value", [
    "aa",
    "",
    [],
    set(),
    tuple()
])
def test_raise_error_on_invalid_value(invalid_value):
    with pytest.raises(TypeError):
        converte_brl_to_eur(value=invalid_value)

@pytest.mark.parametrize("invalid_value", [
    "aa",
    "",
    [],
    set(),
    tuple()
])
def test_raise_error_on_invalid_value2(invalid_value):
    with pytest.raises(ValueError):
        converte_brl_to_eur(value=invalid_value)


# aprendendo as fixtures
"""
com parametrize temos uma lista de valores, 
com as fixtures

fixtures 
    -> recurso disponivel no pytest
    -> 

Fluxo do teste
No setup faz todas as configuracoes (busca dados em banco, conexoes)
executa o codigo
assertions
tear down 

Os testes precisam ser:
- stateless (sem estado)
- reprodutivel
- independentes

"""

@pytest.fixture
def negative_value():
    return -1

def test_accept_negative_value(negative_value):
    assert converte_brl_to_eur(negative_value)<0

# Misturando fixture com parametrize
# import conftest # Nao precisa importar

# fixture que recebe fixture
def test_accept_negative_value3(negative_value3):
    assert converte_brl_to_eur(negative_value3)<0


"""
edge cases -> sao casos alternativos 
"""


# Verificando se uma funcao da api foi chamada
"""
    0-----0 (tunel)
    input -----> 0----0 ------> output
    spy -> espiao, fica armazenando tudo que esta entrando (input)
    

"""