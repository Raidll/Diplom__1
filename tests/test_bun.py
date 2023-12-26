import pytest
from bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', ['Тест', 'Test', 'Matt', "", "123", None])
    def test_get_bun_name(self, name):
        bun = Bun(name, 10.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [1.0, 0, 100.5, 10.25])
    def test_get_bun_name(self, price):
        bun = Bun("TestName", price)
        assert bun.get_price() == price
