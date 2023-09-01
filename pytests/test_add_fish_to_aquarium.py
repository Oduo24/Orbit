import unittest

from myfunc import add_fish_to_aquarium

class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_exception(self):
        too_many_fish = ["shark"] * 25

        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish_list=too_many_fish)
            self.assertEqual(
                    str(exception_context.exception),
                    "A maximum of 10 fish can be added to the aquarium"
                    )
