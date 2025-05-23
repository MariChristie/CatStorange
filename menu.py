import tkinter as tk

root = tk.Tk()
root.geometry('400x600')
root.title('CatStorange')

menu_bar_colour = '#264653'

# Icons 
toggle_icon = tk.PhotoImage(file='images/toggle_btn_icon.png')
home_icon = tk.PhotoImage(file='images/home_icon.png')
service_icon = tk.PhotoImage(file='images/services_icon.png')
update_icon = tk.PhotoImage(file='images/updates_icon.png')
contact_icon = tk.PhotoImage(file='images/contact_icon.png')
about_icon = tk.PhotoImage(file='images/about_icon.png')

def switch_indication(indicator_lb):

    home_btn_indicator.config(bg=menu_bar_colour)
    service_btn_indicator.config(bg=menu_bar_colour)
    update_btn_indicator.config(bg=menu_bar_colour)
    about_btn_indicator.config(bg=menu_bar_colour)
    about_btn_indicator.config(bg=menu_bar_colour)

    indicator_lb.config(bg='white')

menu_bar_frame = tk.Frame(root, bg=menu_bar_colour)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour)
toggle_menu_btn.place(x=4, y=10)

home_btn = tk.Button(menu_bar_frame, image=home_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                    command=lambda: switch_indication(indicator_lb=home_btn_indicator))
home_btn.place(x=9, y=130, width=30, height=40)     


home_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)           
home_btn_indicator.place(x=3, y=130, height=40, width=3)

service_btn = tk.Button(menu_bar_frame, image=service_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                      command=lambda: switch_indication(indicator_lb=service_btn_indicator))
service_btn.place(x=9, y=190, width=30, height=40)

service_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
service_btn_indicator.place(x=3, y=190, height=40, width=3)


update_btn = tk.Button(menu_bar_frame, image=update_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=update_btn_indicator))
update_btn.place(x=9, y=250, width=30, height=40)

update_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
update_btn_indicator.place(x=3, y=250, height=40, width=3)

contact_btn = tk.Button(menu_bar_frame, image=contact_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=contact_btn_indicator))
contact_btn.place(x=9, y=310, width=30, height=40)

contact_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
contact_btn_indicator.place(x=3, y=310, height=40, width=3)

about_btn = tk.Button(menu_bar_frame, image=about_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=about_btn_indicator))
about_btn.place(x=9, y=378, width=30, height=40)

about_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
about_btn_indicator.place(x=3, y=378, height=40, width=3)

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate(flag=False)

menu_bar_frame.configure(width=45)


root.mainloop()