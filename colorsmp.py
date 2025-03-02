import tkinter as tk

def show_selection():
    selected_color = color_var.get()
    label.config(text=f"Выбранный цвет: {selected_color}")

root = tk.Tk()
root.title("Пример Radiobutton с цветами")

color_var = tk.StringVar(value="Красный")

radiobutton1 = tk.Radiobutton(root, text="Красный", variable=color_var, value="Красный",
                                bg="red", fg="white", selectcolor="darkred", command=show_selection)
radiobutton1.pack(anchor=tk.W)

radiobutton2 = tk.Radiobutton(root, text="Зеленый", variable=color_var, value="Зеленый",
                                bg="green", fg="white", selectcolor="darkgreen", command=show_selection)
radiobutton2.pack(anchor=tk.W)

radiobutton3 = tk.Radiobutton(root, text="Синий", variable=color_var, value="Синий",
                                bg="blue", fg="white", selectcolor="darkblue", command=show_selection)
radiobutton3.pack(anchor=tk.W)

label = tk.Label(root, text="Выбранный цвет: Красный")
label.pack()

root.mainloop()
