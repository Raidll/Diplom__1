from unittest.mock import Mock

from burger import Burger
import ingredient_types


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "BunName"
        mock_bun.get_price.return_value = 10.00
        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == "BunName"
        assert burger.bun.get_price() == 10.00

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 10.0
        mock_ingredient.get_name.return_value = "Cucumber"
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_price() == 10.0
        assert burger.ingredients[0].get_name() == "Cucumber"

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        first_ingredient = burger.ingredients[0]
        second_ingredient = burger.ingredients[1]
        burger.move_ingredient(0, 1)

        assert first_ingredient == burger.ingredients[1]
        assert second_ingredient == burger.ingredients[0]

    def test_get_price(self, burger):
        assert burger.get_price() == 45.00

    def test_get_receipt(self, burger):
        expected_receipt = "(==== ciabatta ====)\n"
        expected_receipt += "= filling cucumber =\n"
        expected_receipt += "= sauce ketchup =\n"
        expected_receipt += "(==== ciabatta ====)\n\n"
        expected_receipt += "Price: 45.0"

        assert expected_receipt == burger.get_receipt()



