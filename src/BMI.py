import pandas as pd
import numpy as np


class BMI_ANALYSIS:
    # Add this as variable we may add this as csv also if we get regular reports
    def __init__(self):
        pass

    def import_data(self):
    #could have added this in csv file
        users_data = [{"Gender": "Male", "HeightCm": 175, "WeightKg": 75}, {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
     {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
     {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        return pd.DataFrame(users_data)

    #logic handler and dataframe handler
    # could have added checks for fillna 
    def result_handler(self):
        user_data = self.import_data()

        user_data['BMI'] = user_data['WeightKg']/(user_data['HeightCm']/100)**2
        # print(user_data.dtypes)
        # Added conditions as hard code could be made dynamic if needed
        conditons = [((user_data['BMI'] >= 0) & (user_data['BMI'] < 18.4)), ((user_data['BMI'] > 18.5) & (user_data['BMI'] < 24.9)), ((user_data['BMI'] > 25) & (
            user_data['BMI'] < 29.9)), ((user_data['BMI'] > 30) & (user_data['BMI'] < 34.9)), ((user_data['BMI'] > 35) & (user_data['BMI'] < 39.9)), (user_data['BMI'] > 40)]
        values = ['Underweight', 'Normal weight', 'Overweight',
                'Moderately obese', 'Severely obese', 'Very severely obese']
        values_health_risk = ['Malnutrition risk', 'Low risk',
                            'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
        # I believe two time running numpy is 2 million checks twice 
        user_data['BMI Category'] = np.select(conditons, values, default=0)
        user_data['Health risk'] = np.select(
            conditons, values_health_risk, default=0)
        
        return user_data

    # counting
    def overweight_count(self):
        user_data = self.result_handler()
        overweight_count = len(user_data.loc[user_data['BMI Category'] == 'Overweight'])
        return overweight_count


# a = BMI_ANALYSIS()
# print(a.result_handler())
# print(a.overweight_count())


