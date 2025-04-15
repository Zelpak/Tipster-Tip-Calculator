import customtkinter as ctk

percentage_value = 15

def on_validate_input(P):
    return P.isdigit() or P == ""

def calculate():
    try:
        billbox_value = float(billbox.get('1.0', 'end-1c'))  
        tip_percentage = percentage_value  

        tip_amount = billbox_value * tip_percentage / 100  
        total_amount = billbox_value + tip_amount  

        result_label.configure(
            text=f'Tip: ${tip_amount:.2f} \n Total: ${total_amount:.2f}'
        )
    except ValueError:
        result_label.configure(text='Please enter valid numbers.')

def increase_tip():
    global percentage_value
    maximum_percentage_value = 100
    percentage_value += 1
    if percentage_value > maximum_percentage_value:
        percentage_value = maximum_percentage_value
    Tipbox.configure(text=f'{percentage_value}%')
    calculate()
    
def decrease_tip():
    global percentage_value
    if percentage_value > 0:
        percentage_value -= 1
        Tipbox.configure(text=f'{percentage_value}%')
        calculate()

app = ctk.CTk()
app.title('Tipster - Tip Calculator')
app.resizable(False, False)
app.geometry('200x320')

bill_label = ctk.CTkLabel(app, text='Bill', text_color='#656565')
bill_label.pack(padx=5, pady=(5, 0))

billbox = ctk.CTkTextbox(app, width=120, height=20, corner_radius=8)
billbox.pack(padx=10, pady=(0, 10))

tipframe = ctk.CTkFrame(app)
tipframe.pack(padx=10, pady=10)

tip_label = ctk.CTkLabel(tipframe, text='Tip %:')
tip_label.grid(row=0, column=0, padx=5)

Minus = ctk.CTkButton(
    tipframe, width=30, height=25, text='-', command=decrease_tip,
    fg_color='#141414', border_color='#636363', hover_color='#3b3b3b',
    border_width=1, cursor='arrow'
)
Minus.grid(row=0, column=1, padx=2)

Tipbox = ctk.CTkLabel(tipframe, width=60, height=25, corner_radius=5, text=f'{percentage_value}%', fg_color='grey')
Tipbox.grid(row=0, column=2, padx=2)

Plus = ctk.CTkButton(
    tipframe, width=30, height=25, text='+', command=increase_tip,
    fg_color='#141414', border_color='#636363', hover_color='#3b3b3b',
    border_width=1, cursor='arrow'
)
Plus.grid(row=0, column=3, padx=2)

people_label = ctk.CTkLabel(app, text='Number of people (optional)', text_color='#656565')
people_label.pack(padx=10, pady=(10, 0))

PeopleNumberbox = ctk.CTkTextbox(app, width=120, height=20, corner_radius=8)
PeopleNumberbox.pack(padx=10, pady=(0, 10))

execute = ctk.CTkButton(
    app, width=100, height=35, corner_radius=4, text='Calculate', command=calculate,
    fg_color='#141414', border_color='#636363', border_width=1, hover_color='#3b3b3b',
    cursor='arrow'
)
execute.pack(pady=(5, 10))

resultframe = ctk.CTkFrame(app, width=20, height=10)
resultframe.pack()

result_label = ctk.CTkLabel(resultframe, text='Result will appear here', anchor="center")
result_label.grid(row=0, column=1, padx=10, pady=10)

app.mainloop()
