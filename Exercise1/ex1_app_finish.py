'''App 1 Finished'''

from Tkinter import *

root = Tk()

new_entry_box = Entry(root)
new_entry_box['width'] = 50
new_entry_box.grid(row=0, column=0)

new_button = Button(root)
new_button['text'] = 'Click Me!'
new_button.grid(row=0, column=1)

root.mainloop()
