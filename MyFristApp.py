import customtkinter as ctk
app = ctk.CTk()
app.title('My First App')
app.geometry("500x300")

def click():
    print('Done Clicked')
    name = NameEntry.get()
    address = addressEntry.get()
    form = [name, address]
    info = '\n'.join(form)
    infoLabel.configure(text=info)
    print(f'Information Sent Back: {form}')

Namelabel = ctk.CTkLabel(app, text="Name: ")
Namelabel.grid(row=0, column=0)



NameEntry = ctk.CTkEntry(app, placeholder_text="Enter Your Name: ")
NameEntry.grid(row=0, column=1)



addresslabel = ctk.CTkLabel(app, text = "Enter Your Address: ")
addresslabel.grid(row=1, column=0)

addressEntry = ctk.CTkEntry(app, placeholder_text="Enter Here: ")
addressEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text="Done", command=click)
enterButton.grid(row=2, column=0)

infoLabel = ctk.CTkLabel(app, text='')
infoLabel.grid(row=4, column=0)





app.mainloop()