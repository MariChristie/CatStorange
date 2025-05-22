import tkinter as tk

root = tk.tk()
root.geometry('400x600')
root.title('CatStorange')

menu_bar_frame = tk.Frame(root)

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y)
menu_bar_frame.pack_propagate(flag=False)

menu_bar_frame.configure(width=45)


root.mainloop()