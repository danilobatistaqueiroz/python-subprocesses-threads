import tkinter as tk
import pickle

class Fruits: pass
banana = Fruits()
banana.color = 'yellow'
banana.value = 30

window = tk.Tk()
window.title("Welcome")

file = open('important', 'wb')
pickle.dump(banana, file)
file.close()

file = open('important', 'rb')
data = pickle.load(file)
file.close()
print(data.color)