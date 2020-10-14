import numpy as np
import pandas as pd
# import json as js
dfNew = pd.DataFrame()
df_ref = pd.read_excel("BMI_table.xlsx")
df = pd.read_json("data.json")

value = 0
bmi_category = None
health_risk = None

def calculate_bmi_value( height, weight):
     value = weight / (height * 0.01)
     return value

def determine_bmi_category( height, weight):
    value1 = calculate_bmi_value(height, weight)
    if value1 >= 40:
         bmi_category = "Underweight"
    elif value1 >= 18.5 and value1 <= 24.9:
         bmi_category = "Normal weight"
    elif value1 >= 25 and value1 <= 29.9:
         bmi_category = "Overweight"
    elif value1 >= 30 and value1 <= 34.9:
         bmi_category = "Moderately obese"
    elif value1 >= 35 and value1 <= 39.9:
         bmi_category = "Severely obese"
    else:
         bmi_category = "Very severely obese"

    return bmi_category

def determine_health_risk( height, weight):
    value1 = calculate_bmi_value(height, weight)
    if value1 >= 40:
         health_risk = "Malnutrition risk"
    elif value1 >= 18.5 and value1 <= 24.9:
         health_risk = "Low risk"
    elif value1 >= 25 and value1 <= 29.9:
         health_risk = "Enhanced risk"
    elif value1 >= 30 and value1 <= 34.9:
         health_risk = "Medium risk"
    elif value1 >= 35 and value1 <= 39.9:
         health_risk = "High risk"
    else:
         health_risk = "Very high risk"

    return health_risk

height = df['HeightCm']
weight = df['WeightKg']

bmi_value_object = map(calculate_bmi_value, height, weight)
df['BMI Value'] = np.array(list(bmi_value_object))

bmi_category_object = map(determine_bmi_category, height, weight)
df['BMI Category'] = np.array(list(bmi_category_object))

health_risk_object = map(determine_health_risk, height, weight)
df['Health Risk'] = np.array(list(health_risk_object))

df_json = df.to_json("dataNew.json", orient='records')



'''
dfNew.to_json('dataNew.json')
print(df1)
'''

