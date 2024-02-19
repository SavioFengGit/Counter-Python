# tkinter GUI
import tkinter as tk

# Finestra 
window = tk.Tk()
window.title("Contatore")

# variabile per memorizzare il valore del contatore
counter = tk.IntVar()
counter.set(0)

# funzione per incrementare il contatore
def increment():
    counter.set(counter.get() + 1)

# funzione per decrementare il contatore
def decrement():
    counter.set(counter.get() - 1)

# funzione per resettare il contatore
def reset():
    counter.set(0)

# label per mostrare il valore del contatore
label = tk.Label(window, textvariable=counter, font=("Arial", 30))
label.pack()

# bottone per incrementare il contatore
button_inc = tk.Button(window, text="+", command=increment, font=("Arial", 30))
button_inc.pack(side=tk.LEFT)

# bottone per decrementare il contatore
button_dec = tk.Button(window, text="-", command=decrement, font=("Arial", 30))
button_dec.pack(side=tk.RIGHT)

# bottone per resettare il contatore
button_reset = tk.Button(window, text="Reset", command=reset, font=("Arial", 30))
button_reset.pack(side=tk.BOTTOM)

# variabili per memorizzare le coordinate del mouse
mouse_x = 0
mouse_y = 0

# funzione per catturare l'evento di clic del mouse
def mouse_press(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y

# funzione per catturare l'evento di movimento del mouse
def mouse_move(event):
    global mouse_x, mouse_y
    delta_x = event.x - mouse_x
    delta_y = event.y - mouse_y
    window.geometry(f"+{window.winfo_x() + delta_x}+{window.winfo_y() + delta_y}")

# Aggancio le funzioni agli eventi della finestra
window.bind("<Button-1>", mouse_press)
window.bind("<B1-Motion>", mouse_move)

# Avvio 
window.mainloop()


#use the command pyinstaller nome_script.py --noconsole --onefile to run the application with double click