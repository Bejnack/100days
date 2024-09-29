from tkinter import *

def calculate():
    miles = float(mile_input.get())
    mile_in_km = miles * 1.609
    kilometers.config(text=("%.2f" % mile_in_km))

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20,pady=20)

#input for mile
mile_input = Entry(width=10)
mile_input.grid(column=1,row=0)

#mile display
mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)

#display equal to 
equal_label =Label(text="is equal to")
equal_label.grid(column=0,row=1)

#display calculated nr
kilometers = Label(text=0)
kilometers.grid(column=1,row=1)

#display km
kilometers_text = Label(text="Km")
kilometers_text.grid(column=2,row=1)

#button on middle to start calculate
calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(column=1,row=2)


window.mainloop()
