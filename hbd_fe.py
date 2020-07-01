from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
windows = Tk()
img = Image.open('hd.jpg')
render = ImageTk.PhotoImage(img)
l = Label(windows, image=render, width=800, height=730)
l.image = render
l.place(x = 40, y = 40)

dic = {}
def diction(s):
    df = pd.read_csv('ge.csv')
    k=pd.DataFrame(s)
    print(k)
    try:
        x = df.iloc[:,:-1]
        y = df['target']
        x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.1,random_state = 10)
        classifier = LogisticRegression(random_state=0)
        classifier.fit(x_train, y_train)
        y_pred = classifier.predict(k)
        return y_pred
    except ValueError as er:
        print(f"something went wrong{er}")
def prediction(n):
    if n == 0:
        messagebox.showinfo("greetings", "you don't have any heart desease")
    else:
        messagebox.showinfo("greetings", "you have heart desease")
def dictio():
    dic['age'] = list([int(e1.get())])
    dic['sex'] = list([0]) if v1.get() == 'Female' else list([1])
    dic['cp'] = list([0]) if v2.get() == 'Typical Angina' else list([1]) if v2.get() == 'Atypical Angina' else list([2]) if v2.get() == "Non-anginal Pain" else list([3]) #'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'
    dic['trestbps'] = list([int(e4.get())])
    dic['chol'] = list([int(e5.get())])
    dic['fbs'] = list([0]) if v3.get() == 'lower than 120 mg/ml' else list([1])
    dic['restecg'] = list([1]) if v4.get() == 'ST-T Wave Abnormality' else list([0]) if v2.get() == 'normal' else list([2]) #  'normal', 'ST-T Wave Abnormality', 'Left Ventricular hypertrofy'
    dic['thalach'] = list([int(e8.get())])
    dic['exang'] = list([1]) if v5.get() == 'Yes' else list([0])#'No', 'Yes'
    dic['oldpeak'] = list([float(e10.get())])
    dic['slope'] = list([2]) if v6.get() == 'Downsloping' else list([1]) if v6.get() == 'Flat' else list([0])#'Flat','Upsloping','Downsloping'
    dic['ca'] = list([int(e12.get())])
    dic['thal'] = list([1]) if v7.get() == 'Normal' else list([3]) if v7.get() == 'Revrsible Defect' else list([2]) #'Normal', 'Fixed defect', 'Revrsible Defect'
    ans = diction(dic)
    if ans == 0:
        prediction(0)
    else:
        prediction(1)
l = Label(windows, text = "Heart desease prediction system", font = ('Comic_Sans Ms', 20, 'bold'))
l.place(x = 1000, y = 10)
l1 = Label(windows, text = "Age", font = ('Comic_Sans Ms',10, 'bold'))
l1.place(x = 900, y = 80)
e1 = Entry(windows, width= 20)
e1.place(x = 1100, y = 80)

l2 = Label(windows, text = "sex", font = ('Comic_Sans Ms',10, 'bold'))
l2.place(x = 900, y = 130)
v1 = StringVar()
choice = {'Female', 'Male'}
p = OptionMenu(windows, v1, *choice)
p.place(x = 1100, y = 130)

l3 = Label(windows, text = "Chest Pain Type", font = ('Comic_Sans Ms',10, 'bold'))
l3.place(x = 900, y = 180)
v2 = StringVar()
choice = {'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'}
p = OptionMenu(windows, v2, *choice)
p.place(x = 1100, y = 180)

l4 = Label(windows, text = "Resting Blood Pressure", font = ('Comic_Sans Ms',10, 'bold'))
l4.place(x = 900, y = 230)
e4 = Entry(windows, width= 20)
e4.place(x = 1100, y = 230)

l5 = Label(windows, text = "Cholestrol", font = ('Comic_Sans Ms',10, 'bold'))
l5.place(x = 900, y = 280)
e5 = Entry(windows, width= 20)
e5.place(x = 1100, y = 280)

l6 = Label(windows, text = "Fasting Blood Sugar", font = ('Comic_Sans Ms',10, 'bold'))
l6.place(x = 900, y = 330)
v3 = StringVar()
choice = {'lower than 120 mg/ml', 'greater than 120 mg/ml'}
p = OptionMenu(windows, v3, *choice)
p.place(x = 1100, y = 330)

l7 = Label(windows, text = "Rest_ecg", font = ('Comic_Sans Ms',10, 'bold'))
l7.place(x = 900, y = 380)
v4 = StringVar()
choice = { 'normal', 'ST-T Wave Abnormality', 'Left Ventricular hypertrofy'}
p = OptionMenu(windows, v4, *choice)
p.place(x = 1100, y = 380)

l8 = Label(windows, text = "Max Heart Rate Achieved", font = ('Comic_Sans Ms',10, 'bold'))
l8.place(x = 900, y = 430)
e8 = Entry(windows, width= 20)
e8.place(x = 1100, y = 430)

l9 = Label(windows, text = "Exercise Indused Angina", font = ('Comic_Sans Ms',10, 'bold'))
l9.place(x = 900, y = 480)
v5 = StringVar()
choice = {'No', 'Yes'}
p = OptionMenu(windows, v5, *choice)
p.place(x = 1100, y = 480)

l10 = Label(windows, text = "St Depression", font = ('Comic_Sans Ms',10, 'bold'))
l10.place(x = 900, y = 530)
e10 = Entry(windows, width= 20)
e10.place(x = 1100, y = 530)

l11 = Label(windows, text = "St_Slope", font = ('Comic_Sans Ms',10, 'bold'))
l11.place(x = 900, y = 580)
v6 = StringVar()
choice = { 'Flat','Upsloping','Downsloping'}
p = OptionMenu(windows, v6, *choice)
p.place(x = 1100, y = 580)

l12 = Label(windows, text = "num mMjor Vessels", font = ('Comic_Sans Ms',10, 'bold'))
l12.place(x = 900, y = 630)
e12 = Entry(windows, width= 20)
e12.place(x = 1100, y = 630)

l13 = Label(windows, text = "Thalassemia", font = ('Comic_Sans Ms',10, 'bold'))
l13.place(x = 900, y = 680)
v7 = StringVar()
choice = {'Normal', 'Fixed defect', 'Revrsible Defect'}
p = OptionMenu(windows, v7, *choice)
p.place(x = 1100, y = 680)

B = Button(windows, text = "Predict", bg="orange",  font = ('Comic_Sans Ms',10, 'bold'), width = 20, command= dictio)
B.place(x=1100, y = 730)

windows.geometry("600x500")
windows.mainloop()