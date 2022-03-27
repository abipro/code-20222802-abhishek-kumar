# sys.path.append(".")
# import pytest
import pandas as pd
from src.BMI import BMI_ANALYSIS 
import datatest as dt



def setUpModule():
    dt.register_accessors() 
class TestBmi(dt.DataTestCase):
    # Column Check for output
    @dt.mandatory
    def validate_columns(self):
        bmi_data = BMI_ANALYSIS()
        bmi_data = bmi_data.result_handler()
        dt.validate(bmi_data.columns,
            {'BMI', 'BMI Category', 'Gender', 'Health risk','HeightCm','WeightKg'},
        )
    # Count Check for output
    @dt.mandatory
    def validate_count(self):
        bmi_data = BMI_ANALYSIS()
        self.assertIsInstance(bmi_data.overweight_count(), int)


TestBmi().validate_columns()
TestBmi().validate_count()