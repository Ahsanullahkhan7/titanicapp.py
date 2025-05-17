import streamlit as st
import pickle

st.title('Titanic Survival Prediction Web App!')
st.image('image.png', caption='Predict Survival on the Titanic')

with open('titanicpickle.pkl', 'rb') as pickleFile:
    model = pickle.load(pickleFile)

def predictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    try:
      prediction = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
      return 'survived' if prediction [0]==1 else 'Did not Survive'
    except Exception as e :
       return f'error{str(e)}'

st.sidebar.header('How to Use!')
st.sidebar.markdown("""1. Enter the Passenger Details in the Form.
2. Click 'Predict' to See the Survival Result.
3. Adjust Values to Test Different Scenarios.
""")
st.sidebar.info("Example: A 30 years old male, 3rd class, $20 fare, travelinga alone from port Southempton.")
def main():
   st.subheader("Enter Passenger Details:")
   col1,col2 = st.columns(2)
   with col1:
      Pclass = st.selectbox('Passenger class', options=[1,2,3], format_func=lambda X:f'class{X}')
      Sex = st.radio('Sex', options=['male', 'female'])
      Age = st.slider('Age', min_value=0, max_value=100, value=30)
   with col2:
      SibSp = st.slider('Siblings/Spouses Aboard:', min_value=0 ,max_value=10, value=0) 
      Parch = st.slider('Parents/Children Aboard:', min_value=0, max_value=10, value=0)
      Fare = st.slider('Fare($):', min_value=0.0, max_value=500.0, value=50.0, step=0.1)
      Embarked = st.radio('Port of Embarkation::', options=['C', 'Q', 'S'], format_func=lambda X: f'port{X}' )
   Sex = 1 if Sex == 'female' else 0
   Embarked = {'C':0, 'Q':1 , 'S':2}[Embarked]
   if st.button('predict'):
      result = predictionFunction(Pclass, Sex, Age, SibSp , Parch, Fare, Embarked)
      st.markdown(f'{result}')
      st.balloons()

if __name__ == '__main__':
   main()
