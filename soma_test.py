# import pytest
# from pytest_mock import mocker - biblioteca para mocar dados
from soma import adicao

# teste função soma 
def test_adicao():
    assert adicao(5,5) == 10