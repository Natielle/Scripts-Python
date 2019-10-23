from quotes_2 import QuoteAPI
import pytest

def test_variable_rate_brl_to_eur():
    assert 2 == QuoteAPI().get_rate("BRL", "EUR")

def test_invalid_currency_error():
    with pytest.raises(KeyError):
        QuoteAPI().get_rate("BRL", "Abracadabra")

"""
# instalar o plugin:
# pip install pytest-mock
# esse plugin oferece a fixture moker
def test_invalid_currency_error2():
    get_rate_mock = mocker.patch(
        "quotes_2.QuoteAPI.get_rate",
        side_effect = KeyError # gera uma excecao como efeito colateral
    )
    with pytest.raises(KeyError):
        QuoteAPI().get_rate("BRL", "Abracadabra")

"""
