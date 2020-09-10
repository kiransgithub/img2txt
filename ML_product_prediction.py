### Import the Pandas/ML Libarary 
#from sklearn.externals import joblib
import joblib
import pandas as pd


# import seaborn as sns

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

class MLPrediction:

    def findCategory(text):
        print("==================Text Content to categorize======================")
        print(text)
        print("==================================================================")
        ## Pass the pickle file
        # loaded_model = joblib.load("ver1_phone_feature_2250.sav")
        # loaded_model = joblib.load("ver2_phone_feature_2250.sav")
        loaded_model = joblib.load("ver3_phone_feature_2250.sav")

        # result = loaded_model.score(X_test, Y_test)
        # print(loaded_model)

        #Pass the text which we getting from image to text as description
        df=pd.DataFrame({'description': [text]})


        ## Model predict the Category
        output=loaded_model.predict(df['description'])
        Prediction=loaded_model.predict(df['description'])
        print("==================PREDICTED CATEGORY==============================")
        print(Prediction)
        print("------------------------------------------------------------------")

        # df['detail']=Prediction
        #
        # def Cat_col(v1):
        #     a=v1.split('-')
        #     return a[0]
        #
        # df['Category']=df['detail'].apply(Cat_col)
        #
        # def Prd_split(v1):
        #     a=v1.split('-')
        #     return a[1]
        # df['Product']=df['detail'].apply(Prd_split)
        #
        # df[['Category','Product']]
        #
        # print(df['Category'],df['Product'])

        # return df[['Category','Product']]
        return Prediction



