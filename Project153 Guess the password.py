from tkinter import *
import random

root = Tk()
root.title("Guess the password")
root.geometry("500x500")

input_password = Entry(root)
input_password.place(relx = 0.5, rely = 0.3, anchor = CENTER)

guessed_password = Label(root)
guessed_password.place(relx = 0.5, rely = 0.4, anchor = CENTER)

generated_password = Label(root)
generated_password.place(relx = 0.5, rely = 0.6, anchor = CENTER)

array_3d = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], ['ANiMal','BRiGht', 'CaTaPillAr', 'DoNkEy', 'ElePhaNt', 'FlAmInGo', 'GinGerBeArD', 'HiPpoPotaMus', 'InTerNet'], ['!', '@', '#', '$', '%', '^', '&', '*']]]
print(array_3d)

def display_input():
    random_no1 = random.randint(0,8)
    random_no2 = random.randint(0,8)
    random_no3 = random.randint(0,7)
    
    character1 = str(array_3d[0][0][random_no1])
    character2 = array_3d[0][1][random_no2]
    character3 = array_3d[0][2][random_no3]
    
    guessed_password["text"] =  "Guessed Password: " + input_password.get()
    generated_password["text"] = "Generated Password: " + character1 + character2 + character3

new_password = Button(root, text = "New password", command = display_input)
new_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)



root.mainloop()
