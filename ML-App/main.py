from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

from model import *

# tkinter start
root = Tk()
root.geometry('400x500')
root.title("Heart Failure Prediction")

def show_values():
    input = [age.get(), gender.get(), anaemia.get(), int(creatinine_phosphokinase.get()), diabetes.get(), ejection_fraction.get()
    ,high_blood_pressure.get(), int(platelets.get()), serum_creatinine.get(), serum_sodium.get(), smoking.get(), time.get()]

    output = model_train(patient_data, input)

    if output[0] == 1:            
        messagebox.showinfo("Result", "Patient is at risk!")

    elif output[0] == 0:
        messagebox.showinfo("Result", "Patient is not at risk!")


# age,
age = IntVar()
Label (root, text="Age: ", font='bold').grid(row=0, column=0)
Scale(root, from_=0, to=100, orient=HORIZONTAL, variable=age).grid(row=0, column=1)

# anaemia,
anaemia = IntVar()
Label (root, text="Anaemia: ", font='bold').grid(row=1, column=0)
Radiobutton(root, text="Yes", variable=anaemia, value=1).grid(row=1, column=1)
Radiobutton(root, text="No", variable=anaemia, value=0).grid(row=1, column=2)

# creatinine_phosphokinase,
Label (root, text="creatinine_phosphokinase: ", font='bold').grid(row=2, column=0)
creatinine_phosphokinase = Entry (root)
creatinine_phosphokinase.grid(row=2, column=1)

# diabetes,
diabetes = IntVar()
Label (root, text="Diabetes", font='bold').grid(row=3, column=0)
Radiobutton(root, text="Yes", variable=diabetes, value=1).grid(row=3, column=1)
Radiobutton(root, text="No", variable=diabetes, value=0).grid(row=3, column=2)

# ejection_fraction
ejection_fraction = IntVar()
Label (root, text="ejection_fraction", font='bold').grid(row=4, column=0)
Scale(root, from_=0, to=100, orient=HORIZONTAL, variable=ejection_fraction).grid(row=4, column=1)

# high_blood_pressure
high_blood_pressure = IntVar()
Label (root, text="high_blood_pressure", font='bold').grid(row=5, column=0)
Radiobutton(root, text="Yes", variable=high_blood_pressure, value=1).grid(row=5, column=1)
Radiobutton(root, text="No", variable=high_blood_pressure, value=0).grid(row=5, column=2)

# platelets
Label (root, text="platelets (example: 265000)", font='bold').grid(row=6, column=0)
platelets = Entry (root)
platelets.grid(row=6, column=1)

# serum_creatinine
serum_creatinine = IntVar()
Label (root, text="serum_creatinine", font='bold').grid(row=7, column=0)
Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=serum_creatinine).grid(row=7, column=1)

# serum_sodium
serum_sodium = IntVar()
Label (root, text="serum_sodium", font='bold').grid(row=8, column=0)
Scale(root, from_=0, to=500, orient=HORIZONTAL, variable=serum_sodium).grid(row=8, column=1)

# sex
gender = IntVar()
Label (root, text="Gender", font='bold').grid(row=9, column=0)
Radiobutton(root, text="Male", variable=gender, value=1).grid(row=9, column=1)
Radiobutton(root, text="Female", variable=gender, value=0).grid(row=9, column=2)

# smoking
smoking = IntVar()
Label (root, text="smoking", font='bold').grid(row=10, column=0)
Radiobutton(root, text="Yes", variable=smoking, value=1).grid(row=10, column=1)
Radiobutton(root, text="No", variable=smoking, value=0).grid(row=10, column=2)

# time
time = IntVar()
Label (root, text="time", font='bold').grid(row=11, column=0)
Scale(root, from_=0, to=500, orient=HORIZONTAL, variable=time).grid(row=11, column=1)

# # create button
Button(root, text='Predict Risk', command=show_values).grid(row=12, column=1)

# tkinter window loop
root.mainloop()
