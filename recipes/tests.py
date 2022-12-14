from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
from django.core.exceptions import ValidationError
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('si', password='si123')

    def test_user_pw(self):
        checked = self.user_a.check_password('si123')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('si', password='si123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user=self.user_a
        )
        self.recipe_ingredient = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound',
        )
        self.recipe_ingredient2 = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='skfs',
            unit='pound',
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all() # modelname_set
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 1)
    
    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipe_ingredient_ids = list(user.recipe_set.all().values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipe_ingredient_ids)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_via_recipe(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list('id', flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(), 2)
    
    def test_unit_validation_error(self):
        invalid_units = ['jdks', 'asdsf']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:
                ingredient = RecipeIngredient.objects.create(
                    recipe=self.recipe_a,
                    name='New',
                    quantity='10',
                    unit=unit,
                )
                ingredient.full_clean() # validates all fields

    def test_unit_validation(self):
        valid_unit = 'ounces'
        ingredient = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='New',
            quantity='10',
            unit=valid_unit,
        )
        ingredient.full_clean() # validates all fields
    
    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient2.quantity_as_float)