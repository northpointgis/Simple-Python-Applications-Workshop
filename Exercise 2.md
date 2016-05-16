# Exercise 2: Using Classes with Tkinter
###### In this exercise we will learn how to create a class and do other things.

## Example Class:
The example below is a class that utilizes all of the code we wrote in Exercise 1, but formatted as a class.
```python
from Tkinter import *  

class App():  

  master = Tk() # Create Tk instance  

  def __init__(self):  

    # Execute core methods
    self.config_app()
    self.config_widgets()
    self.run_app()  

  def config_app(self):  

    # Configure main window
    self.master.title('SAMPLE')
    self.master.geometry('500x300')  

  def config_widgets(self):

    # Insert widgets
    new_entry_box = Entry(root)
    new_entry_box['width'] = 50
    new_entry_box.grid(row=0, column=0)  

    new_button = Button(root)
    new_button['text'] = 'Click Me!'
    new_button.grid(row=0, column=1)  

  def run_app(self):  

    # Enter the Tkinter event loop
    self.master.mainloop()  

new_window = App()
```
## Breaking It Down:
1. Import **all** from Tkinter.
2. Define the class name as **App**.
3. Create Tk **root** window widget as a class-level attribute.
4. In the **init** method, we run the core methods
