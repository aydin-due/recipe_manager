from django.core.exceptions import ValidationError
import pint 
from pint.errors import UndefinedUnitError
valid_units = ['pounds', 'lbs', 'oz', 'grams']

def validate_unit(value):
    ureg = pint.UnitRegistry()
    try:
       ureg[value]
    except UndefinedUnitError as e: 
        raise ValidationError(f"{value} is not a valid unit of measure")
    except:
        raise ValidationError(f"{value} is invalid")
    # if value not in valid_units:
    #     raise ValidationError(f"{value} is not a valid unit of measure")