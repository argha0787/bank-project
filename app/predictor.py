import pandas as pd
import pickle


with open('models/model.pkl', 'rb') as file:
    model= pickle.load(file)


def predicting_churn(Customer: dict):
    input_df= pd.DataFrame([Customer])
    prediction= model.predict(input_df)[0]
    if prediction == 1:
        return{
            'message' : 'deposit'
        }
    else:
        return{
            'message': 'No deposit'
        }

