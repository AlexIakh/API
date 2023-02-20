from tkinter import *
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

root = Tk()
root.title("Iris flower prediction")
root.geometry("400x400")
  
#______________LABEL - BUTTON______________
Label(root, text="Petal Length cm:", font="Times 15").grid(row=1, column=0, ipadx=35, ipady=10)
Label(root, text="Petal Width cm:", font="Times 15").grid(row=2, column=0, ipady=10)
Label(root, text="Sepal Length cm:", font="Times 15").grid(row=3, column=0, ipady=10)
Label(root, text="Sepal Width cm:", font="Times 15").grid(row=4, column=0, ipady=10)

#______________FIELD______________
input_text1 = StringVar()
input_text2 = StringVar()
input_text3 = StringVar()
input_text4 = StringVar()
result = StringVar()

e1 = Entry(root, font=1, width=5, textvariable=input_text1)
e1.grid(row=1, column=1)
e2 = Entry(root, font=1, width=5, textvariable=input_text2)
e2.grid(row=2, column=1)
e3 = Entry(root, font=1, width=5, textvariable=input_text3)
e3.grid(row=3, column=1)
e4 = Entry(root, font=1, width=5, textvariable=input_text4)
e4.grid(row=4, column=1)

textbox = Text(root, height=2, width=15, font="Times 16")
textbox.grid(row=5, column=1)

#______________FUNCTION______________
def entryclear():
    input_text1.set("")
    input_text2.set("")
    input_text3.set("")
    input_text4.set("")
    result.set("")
    textbox.delete(1.0, END)

def pred():
    lst = [float(e1.get()),
           float(e2.get()),
           float(e3.get()),
           float(e4.get()),]
    pred_list = np.array(lst).reshape(1, -1)
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    predict = model.predict(pred_list)
    if int(predict)==0:
        predict = 'Iris-Setosa'
    elif int(predict)==1:
        predict = 'Iris-Virginica'
    elif int(predict)==2:
        predict = 'Iris-Versicolour'
    else:
        predict = ""
    textbox.insert(END, predict)
    
#______________BUTTON______________
Button(root, text="Prediction",bg="green", fg="white",
       font="Times 20", cursor="hand2", command=pred).grid(row=5, column=0)

Button(root, text="Clear", font=10, width=8, 
       bg="red", fg="white", cursor="hand2",command=entryclear).grid(row=6, pady=10)
root.mainloop()