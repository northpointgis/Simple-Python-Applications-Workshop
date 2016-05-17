# Exercise 2: Keeping it Classy
###### In this exercise we will learn how to create a class and do other things.

## Example Class:
The example below is a class that utilizes all of the code we wrote in Exercise 1, but formatted as a class.
```python
from Tkinter import *  

class App():  

  # Create class-level attribute Tk instance  

  def __init__(self):  

    # Execute core methods
    pass

  def config_app(self):  

    # Configure main window
    pass

  def config_widgets(self):

    # Insert widgets  
    pass

  def run_app(self):  

    # Enter the Tkinter event loop
    pass

new_window = App()
```
## Breaking It Down:
1. Import **all** from Tkinter.
2. Define the class name as **App**.
3. Create Tk **root** window widget as a class-level attribute.
4. In the **init** method, we run the core methods
