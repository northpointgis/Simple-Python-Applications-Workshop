# Exercise 1: Tkinter Basics
###### In this exercise we will learn how to create a simple Tkinter window, add a widget, and enter the Tkinter mainloop.

## General workflow:
1. Create Tk root widget.
2. Add and style widgets.
3. Enter the Tkinter event loop.

### Creating a window:

1. Import **all** from Tkinter.
```python
from Tkinter import *
```

2. Create Tk **root** window widget.
```python
root = Tk()
```
3. Call the **mainloop** to enter the Tkinter event loop.
```python
root.mainloop()
```
4. Run the script.
```python
from Tkinter import *
#
root = Tk()
#
root.mainloop()
```

### Adding a widget:

1. Create a button widget as a child of the **root** widget.
```python
my_button = Button(root)
```
2. Configure the button.
```python
my_button = Button(root)
my_button['text'] = 'Click Here'
```  

3. Call the **pack** method on the button widget to make it visible.
```python
my_button = Button(root)
my_button['text'] = 'Click Here'
my_button.pack()
```

4. Run the script.
```python
from Tkinter import *
#
root = Tk()
#
my_button = Button(root)
my_button['text'] = 'Click Here'
my_button.pack()
#
root.mainloop()
```
