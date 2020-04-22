# Password Generator GUI
# Version 1.0 --> 1.2
# Created by Han
# Version 1.0 finished on 21/4/2020
# Version 1.2 finished on 22/4/2020
# Note: Lack validation features, will be updated in revised edition.
# Update 22/4/2020: Version 1.2: Added Validation features, added abilty to add symbols to password, and UI tweaks.


# import modules
import string
import random
import tkinter as tk


# Function to generate password
def password_generator(entry1, entry2, entry3):
    formatedentry1 = int(entry1)
    formatedentry2 = int(entry2)
    formatedentry3 = int(entry3)

    if formatedentry1 + formatedentry2 + formatedentry3  < 8:
        if formatedentry1 < 6 :
            password_label['text'] = 'Minimum 8 Characters!'

    else:
        letters = string.ascii_letters
        mixture1 = ""
        result = mixture1.join(random.choice(letters) for i in range(formatedentry1))

        numbers = string.digits
        mixture2 = ""
        result2 = mixture2.join(random.choice(numbers) for i in range(formatedentry2))

        symbols = string.punctuation
        mixture3 = ""
        result3 = mixture3.join(random.choice(symbols) for i in range(formatedentry3))

        password = result + result2 + result3
        mixed_password = ''.join(random.sample(password, len(password)))

        password_label['text'] = mixed_password


# Graphical Code Starts
root =tk.Tk()
root.title("Password Generator Tool Version 1.2")

# code to set initial size of tkinter window
canvas = tk.Canvas(root, height = 800, width = 1000)
canvas.pack()

frame = tk.Frame(root, bg = '#EDF4F4')
frame.place(relheight = 1, relwidth =1)

name_label = tk.Label(root, bg='#EDF4F4', fg = 'grey', text ='Version 1.2, created by Han, 22/4/2020', font = 'Helvectica 9')
name_label.place(relx = 0.78, rely = 0.972)

# code for upper section of the app starts
subtext1_frame = tk.Frame(root, bg = 'blue')
subtext1_frame.place(anchor = 'n', relx = 0.5, rely = 0.05, relheight = 0.05, relwidth =0.5)

label1 = tk.Label(subtext1_frame, text = 'Password Generator Tool', font = 'Helvectica', bg = '#EDF4F4', fg = 'grey')
label1.place(relheight = 1, relwidth = 1)

title_frame = tk.Frame(root, bg = 'blue')
title_frame.place(anchor = 'n', relx = 0.5 , rely = 0.09, relheight = 0.1, relwidth = 0.75)

label2 = tk.Label(title_frame, text = 'Generate a secure password', font = 'Helvecitca 40', bg = '#EDF4F4', fg = '#E74C3C' )
label2.place(relheight = 1, relwidth = 1)

subtext2_frame = tk.Frame(root, bg = 'blue')
subtext2_frame.place(anchor ='n', relx = 0.5, rely = 0.19, relheight = '0.05', relwidth = '0.75')

label3 = tk.Label(subtext2_frame, text = 'Use this generator to create a strong, random and secure password.',
                  font = 'Helvectica', bg ='#EDF4F4', fg ='grey')
label3.place(relheight = 1, relwidth = 1)
# code for upper section of the app ends

# code for middle section of the app starts
result_frame = tk.Frame(root, bg = '#D6DBDF')
result_frame.place(anchor = 'n', relx =0.5, rely = 0.29, relheight = 0.12, relwidth = 0.85)

password_label = tk.Label(result_frame, bg = '#D6DBDF', fg='#7D87A6',  font = 'Consolas 40', relief = 'flat')
password_label.place(anchor = 'n', relx = 0.5, rely = 0.005, relheight = 0.85, relwidth = 1.1)

green_stripe = tk.Label(result_frame, bg = '#69EA66',)
green_stripe.place(anchor = 'n', relx = 0.5, rely = 0.85, relheight = 0.15, relwidth = 1.1)

custom_frame = tk.Frame(root, bg ='#D6DBDF')
custom_frame.place(anchor ='n', relx = 0.5, rely = 0.45, relheight = 0.38, relwidth = 0.85)

upper_label = tk.Label(custom_frame, font='Helvectica 25' ,bg='#D6DBDF', fg='#566573', anchor='w',
                       text="     Customize your password:")
upper_label.place(relwidth=1, relheight=0.25)

upper_right_label = tk.Label(custom_frame, font='Helvectica 14' ,bg='#D6DBDF', fg='#566573', anchor='w',
                             text="(Minimium 8 characters)")
upper_right_label.place(relx = 0.710, rely = 0.01, relwidth=0.25, relheight=0.25)

line = tk.Label(custom_frame, bg='#F8F9F9')
line.place(relx =0.5, rely = 0.22, relwidth = 0.9, relheight = 0.001, anchor ='n')

clabel1 = tk.Label(custom_frame, bg ='#D6DBDF', fg ='#566573', text = 'Letters:', font = 'Helevtica, 20')
clabel1.place(relx = 0.12, rely = 0.38, relwidth = 0.12, relheight = 0.12)

clabel2 = tk.Label(custom_frame, bg ='#D6DBDF', fg ='#566573', text = 'Numbers:', font = 'Helevtica, 20')
clabel2.place(relx = 0.42, rely = 0.38, relwidth = 0.15, relheight = 0.12)

clabel3 = tk.Label(custom_frame, bg ='#D6DBDF', fg ='#566573', text = 'Symbols:', font = 'Helevtica, 20')
clabel3.place(relx = 0.735, rely = 0.38, relwidth = 0.15, relheight = 0.12)

entry1 = tk.Entry(custom_frame, bg = '#EDF4F4', fg='#566573', relief = 'flat', font = 'Helevtica, 20', justify = 'center')
entry1.place(relx = 0.15, rely = 0.55, relwidth = 0.05, relheight = 0.12)

entry2 = tk.Entry(custom_frame, bg = '#EDF4F4', fg='#566573', relief = 'flat', font = 'Helevtica, 20', justify = 'center')
entry2.place(relx = 0.465, rely = 0.55, relwidth = 0.05, relheight = 0.12)

entry3 = tk.Entry(custom_frame, bg = '#EDF4F4', fg='#566573', relief = 'flat', font = 'Helevtica, 20', justify = 'center')
entry3.place(relx = 0.78, rely = 0.55, relwidth = 0.05, relheight = 0.12)
# code for the middle section of the app ends


# code for the button in the app
button = tk.Button(root, text= 'Generate Password',font='Helvectica 15', relief = 'flat', bg ='#E74C3C', fg = '#FDFEFE',
                   command=lambda: password_generator(entry1.get(), entry2.get(), entry3.get()))
button.place(anchor ='n', relx = 0.5, rely = 0.86, relheight = 0.09, relwidth = 0.25)

root.mainloop()
# Graphical Code ends


