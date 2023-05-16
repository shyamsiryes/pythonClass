import customtkinter as ctk

def conversion():
    CtoF = CtoFentry.get()


    far = float(CtoF)
    farProces = far * 1.8 +32
    print(farProces)
    infoLabel.configure(text = str(farProces))




app = ctk.CTk()
app.geometry("350x500")
app.title("Centigrade to Farenheit")
app.configure(bg_color="white", fg_color="white")


enterButton = ctk.CTkButton(app, text="Enter", command=lambda :conversion())
enterButton.grid(row=2, column=0)


ctofLabel1 = ctk.CTkLabel(master=app, text="Celcius to Farenheit", width=330, height=70,
                          fg_color='transparent')
ctofLabel1.grid(row=0, column=0, padx=5, pady=5)

CtoFentry = ctk.CTkEntry(master=app, placeholder_text="Enter Celcius", fg_color="#4ab89a")
CtoFentry.grid(row=1, column=0, padx=5, pady=5)


infoLabel = ctk.CTkLabel(app, text='')
infoLabel.grid(row=4, column=0)





app.mainloop()

