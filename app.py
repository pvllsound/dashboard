from pickle import load 
import streamlit as st

model = load(open('./decision_tree.sav', 'rb'))

st.title('Hello, World!')



class_dict = {
    '0': 'iris setosa',
    '1': 'iris versicolor',
    '2': 'iris virginica'
}

val_1 = st.slider('Petal Width', min_value=0.1, max_value=2.5, step=0.1)
val_2 = st.slider('Petal Length', min_value=1.0, max_value=6.9, step=0.1)
val_3 = st.slider('Sepal Width', min_value=2.0, max_value=4.4, step=0.1)
val_4 = st.slider('Sepal Length', min_value=4.3, max_value=7.9, step=0.1)

if st.button('Predict'):
    prediction = str(model.predict([[val_1, val_2, val_3, val_4]])[0])
    pred_class = class_dict[prediction]
    st.write('Prediction:', pred_class)
