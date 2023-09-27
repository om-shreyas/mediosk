import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy
from iot_devices import check_parameters
model = pickle.load(open('med_model.pkl','rb'))

symptoms_list = [
    "Joint_Ache", "Fever", "Fatigue", "Irritability", "Loss of appetite",
    "Stomach_Ache", "Headache", "Sore_Throat", "Sneezing", "Runny Nose", "Swollen_Neck_Glands",
    "Troubled_Breathing", "Speech_Problem", "Wet_Cough", "Dry Cough", "Loss_of_taste_smell",
    "Nausea_vomiting", "Diarrhea", "Rash/Itch", "Weightloss", "Night_Sweats", "Mouth_Skin_Problems",
    "Infections", "Aching Muscles", "Fainting", "Body Aches", "Sweating", "Bloating", "Bleeding",
    "Painful Urination", "Rapid Heart Rate", "Change in blood pressure", "Gas", "Vomiting",
    "Jaundice", "Hallucinations", "Anxiety", "Ulcers"
]
# parameters = check_parameters()

# st.write('Heartrate: ',parameters[0]/1000,'Sp02: ',parameters[1],'Fever: ',parameters[2])


Joint_Ache = st.checkbox("Joint Ache")
Fever = st.checkbox("Fever")
Fatigue = st.checkbox("Fatigue")
Irritability = st.checkbox("Irritability")
Loss_of_appetite = st.checkbox("Loss of appetite")
Stomach_Ache = st.checkbox("Stomach Ache")
Headache = st.checkbox("Headache")
Sore_Throat = st.checkbox("Sore Throat")
Sneezing = st.checkbox("Sneezing")
Runny_Nose = st.checkbox("Runny Nose")
Swollen_Neck_Glands = st.checkbox("Swollen Neck Glands")
Troubled_Breathing = st.checkbox("Troubled Breathing")
Speech_Problem = st.checkbox("Speech Problem")
Wet_Cough = st.checkbox("Wet Cough")
Dry_Cough = st.checkbox("Dry Cough")
Loss_of_taste_smell = st.checkbox("Loss of taste or smell")
Nausea_vomiting = st.checkbox("Nausea or vomiting")
Diarrhea = st.checkbox("Diarrhea")
Rash = st.checkbox("Rash")
Weightloss = st.checkbox("Weight loss")
Night_Sweats = st.checkbox("Night Sweats")
Mouth_Skin_Problems = st.checkbox("Mouth or Skin Problems")
Infections = st.checkbox("Infections")
Aching_Muscles = st.checkbox("Aching Muscles")
Fainting = st.checkbox("Fainting")
Body_Aches = st.checkbox("Body Aches")
Sweating = st.checkbox("Sweating")
Bloating = st.checkbox("Bloating")
Bleeding = st.checkbox("Bleeding")
Painful_Urination = st.checkbox("Painful Urination")
Rapid_Heart_Rate = st.checkbox("Rapid Heart Rate")
Change_in_blood_pressure = st.checkbox("Change in blood pressure")
Gas = st.checkbox("Gas")
Vomiting = st.checkbox("Vomiting")
Jaundice = st.checkbox("Jaundice")
Hallucinations = st.checkbox("Hallucinations")
Anxiety = st.checkbox("Anxiety")
Ulcers = st.checkbox("Ulcers")

symptoms_dict = {
    "Joint_Ache": Joint_Ache,
    "Fever": Fever,
    "Fatigue": Fatigue,
    "Irritability": Irritability,
    "Loss of apppetite": Loss_of_appetite,
    "Stomach_Ache": Stomach_Ache,
    "Headache": Headache,
    "Sore_Throat": Sore_Throat,
    "Sneeezing": Sneezing,
    "Runny Nose": Runny_Nose,
    "Swollen_Neck_Glands": Swollen_Neck_Glands,
    "Troubled_Breathing": Troubled_Breathing,
    "Speech_Problem": Speech_Problem,
    "Wet_Cough": Wet_Cough,
    "Dry Cough": Dry_Cough,
    "Loss_of_taste_smell": Loss_of_taste_smell,
    "Nausea_vomitting": Nausea_vomiting,
    "Diarrhea": Diarrhea,
    "Rash/Itch": Rash,
    "Weightloss": Weightloss,
    "Night_Sweats": Night_Sweats,
    "Mouth_Skin_Problems": Mouth_Skin_Problems,
    "Infections": Infections,
    "Aching Muscles": Aching_Muscles,
    "Fainting": Fainting,
    "Body Aches": Body_Aches,
    "Sweating": Sweating,
    "Bloating": Bloating,
    "Bleeding": Bleeding,
    "Painful Urination ": Painful_Urination,
    "Rapid Heart Rate": Rapid_Heart_Rate,
    "Change in blood pressure": Change_in_blood_pressure,
    "Gas": Gas,
    "Vomiting": Vomiting,
    "Jaundice": Jaundice,
    "Hallucinations": Hallucinations,
    "Anxiety": Anxiety,
    "Ulcers": Ulcers
}

# if(parameters[0]/1000>100):
#     symptoms_dict['Rapid Heart Rate'] = True
# else:
#     symptoms_dict['Rapid Heart Rate'] = False

# if(parameters[2]>37):
#     symptoms_dict['Fever'] = True
# else:
#     symptoms_dict['Fever'] = False

input_value_df = pd.DataFrame([symptoms_dict])
input_value_df = input_value_df.replace(True,1)
input_value_df = input_value_df.replace(False,0)
st.write(parameters)
st.write(model.predict(input_value_df))