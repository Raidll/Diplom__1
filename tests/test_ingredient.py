from ingredient import Ingredient
import ingredient_types


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "cucumber", 10.00)
        assert ingredient.get_price() == 10.00

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "cucumber", 10.00)
        assert ingredient.get_name() == "cucumber"

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "cucumber", 10.00)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING
