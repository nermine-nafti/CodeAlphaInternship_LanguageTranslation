import customtkinter as ctk
from googletrans import Translator,LANGUAGES 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x450")
        self.title("Language Translating Application")

        ctk.set_appearance_mode("System") 
        ctk.set_default_color_theme("dark-blue") 

        # addding widgets to the app
        label = ctk.CTkLabel(self, text="Translator", font=("Ariel" ,40,"bold"), text_color="purple")
        label.place(relx=0.5, rely=0.01, anchor=ctk.N)

        # Lable for the input box
        lab_txt=ctk.CTkLabel(self,text="primary text", font=("Ariel" ,30,"bold"), text_color="blue")
        lab_txt.place(relx=0.38, rely=0.2, anchor=ctk.E)

        # Lable for the output box
        lab_txt=ctk.CTkLabel(self,text="translated text", font=("Ariel" ,30,"bold"), text_color="blue")
        lab_txt.place(relx=0.92, rely=0.2, anchor=ctk.E)
        
        # Input TextBox
        self.sorc_txt = ctk.CTkTextbox(self, font=("Roboto" ,14), wrap=ctk.WORD) 
        self.sorc_txt.insert("0.0", "Type the text to translate")
        self.sorc_txt.place(relx=0.4, rely=0.5, anchor=ctk.E)

        # Output TextBox
        self.dest_txt = ctk.CTkTextbox(self, font=("Roboto" ,14),wrap=ctk.WORD) 
        self.dest_txt.insert("0.0", "The translated text")
        self.dest_txt.place(relx=0.6, rely=0.5, anchor=ctk.W)

        lang_lst = list(LANGUAGES.values())

        # Input language selection Dropdown
        self.combo_sor = ctk.CTkOptionMenu(self,values=lang_lst, hover=True) 
        self.combo_sor.place(relx=0.4, rely=0.8, anchor=ctk.E) 
        self.combo_sor.set("english")

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(master=self, text="Translate", hover=True, hover_color="purple", command=self.change)
        button.place(relx=0.5, rely=0.95, anchor=ctk.S)

        # Output language selection Dropdown
        self.combo_dest = ctk.CTkOptionMenu(self,values=lang_lst, hover=True) 
        self.combo_dest.place(relx=0.6, rely=0.8, anchor=ctk.W) 
        self.combo_dest.set("english")

    def change(self): # Action function for the button
        source = self.combo_sor.get() 
        destination = self.combo_dest.get() 
        message = self.sorc_txt.get(1.0,ctk.END)

        translator = Translator() 
        translated_txt = translator.translate(message, destination, source) # translator

        self.dest_txt.delete("0.0",ctk.END) # Delete previous entry of the output box
        self.dest_txt.insert("0.0", translated_txt.text) # Insert New Entry in the input box


if __name__ == "__main__":
    app = App()
    app.mainloop()