import pytest

# Uma fixture pode receber outra fixture
# o pytest jah tem algumas fixtures pre definidas
#   para ver elas basta rodar o comando no terminal: pytest --fixtures 
#    cada verdinho do resultado eh uma fixture disponivel
@pytest.fixture(params=[-1,-4,-2])
def negative_value2():
    return -1

# fixture com outra fixture
@pytest.fixture(params=[-1,-4,-2])
def negative_value3(request): # request eh uma fixture disponivel do python
    return request.param