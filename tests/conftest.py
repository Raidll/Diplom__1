from unittest.mock import Mock

import pytest

from burger import Burger
import ingredient_types


@pytest.fixture
def burger():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "ciabatta"
    mock_bun.get_price.return_value = 10.00
    burger.set_buns(mock_bun)

    mock_ingredient1 = Mock()
    mock_ingredient1.get_price.return_value = 10
    mock_ingredient1.get_name.return_value = "cucumber"
    mock_ingredient1.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    burger.add_ingredient(mock_ingredient1)

    mock_ingredient2 = Mock()
    mock_ingredient2.get_price.return_value = 15
    mock_ingredient2.get_name.return_value = "ketchup"
    mock_ingredient2.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    burger.add_ingredient(mock_ingredient2)

    return burger
