from tkinter import *
from PIL import ImageTk,Image
import random
root=Tk()
root.geometry("500x500")
root.title("Country Flags")
root.configure(background="#89CFF0")
india_flag_image=ImageTk.PhotoImage(Image.open('jigglypuff.jpg'))

germany_flag_image=ImageTk.PhotoImage(Image.open('charmender.jpg'))

country_flag_dictionary={"India":india_flag_image,
                         "Germany":germany_flag_image}

label_image=Label(root)
root.mainloop()
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

input_enter_country=Entry(root)
input_enter_country.place(relx=0.5,rely=0.3,anchor=CENTER)

show_map_btn=Button(root,bg="#006400",command=show_map)
show_map_btn.place(relx=0.5,rely=0.4,anchor=CENTER)

def show_map(): 
    try:
         print(dictionary["europe"])
   
    except KeyError :
        print("Key animal is not present in dictionary")
        messagebox.showinfo("Error","THIS KEY DOES NOT EXSIST!!!")
    value=get(input_enter_country)
    label_image["image"] = country_flag_dictionary[value] 
     
    
root.mainloop()