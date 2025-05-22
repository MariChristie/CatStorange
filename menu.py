import tkinter as tk

root = tk.Tk()
root.geometry('400x600')
root.title('CatStorange')

menu_bar_colour = '#264653'

toggle_icon = tk.PhotoImage(file='images/toggle_btn_icon.png')
home_icon = tk.PhotoImage(file='images/home_icon.png')



menu_bar_frame = tk.Frame(root, bg=menu_bar_colour)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour)
toggle_menu_btn.place(x=4, y=10)

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate(flag=False)

menu_bar_frame.configure(width=45)


root.mainloop()