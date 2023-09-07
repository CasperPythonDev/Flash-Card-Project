BACKGROUND_COLOR = "#B1DDC6"
import tkinter as tk

background_image_path = "images/card_back.png"
front_image_path = "images/card_front.png"
right_image_path = "images/right.png"
wrong_image_path = "images/wrong.png"
############# UI #############
background_image = tk.PhotoImage(file=background_image_path)
front_image = tk.PhotoImage(file=front_image_path)


app = tk.Tk()
app.geometry("500x500")
app.configure(image=background_image)


canvas = tk.Canvas()

## BUTTONS ##
wrong_button_image = tk.PhotoImage(file=wrong_image_path)
right_button_image = tk.PhotoImage(file=right_image_path)


wrong_button = tk.Button(image=wrong_button_image)
wrong_button.pack()

right_button = tk.Button(image=right_button_image)
right_button.pack()
## BUTTONS ##


############# UI #############
# No UI below this line
app.mainloop()
