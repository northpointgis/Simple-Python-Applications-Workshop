# Exercise 1: Tkinter Basics
###### In this exercise we will learn how to create a simple Tkinter window, add a widget, and enter the Tkinter mainloop.

## General workflow:
1. Create Tk root widget.
2. Add and style widgets.
3. Enter the Tkinter event loop.

## Creating a window:
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

  root = Tk()  

  root.mainloop()
  ```

## Adding a few widgets:

1. Create an entry box widget as a child of the **root** widget.

  ```python
  new_entry_box = Entry(root)
  ```

2. Call the **pack** method on the entry box widget to make it visible.

  ```python
  new_entry_box = Entry(root)
  new_entry_box.pack()
  ```

3. Below the entry box widget, create a button widget as a child of the **root** widget.

  ```python
  new_button = Button(root)
  ```

4. Call the **pack** method on the button widget to make it visible.

  ```python
  new_button = Button(root)
  new_button.pack()
  ```

5. Run the script.

  ```python
  from Tkinter import *  

  root = Tk()  

  new_entry_box = Entry(root)
  new_entry_box.pack()  

  new_button = Button(root)
  new_button.pack()  

  root.mainloop()
  ```

## Styling Widgets:
As you may have notice, widgets appear on the window in the order that the **pack** method was used. In this section, we will learn how to use the **grid** method in order to place widgets where we want on the window.

1. Replace the **pack** method with the **grid** method for both the entry box and button widgets.

  ```python
  new_entry_box.grid()
  ```

  ```python
  new_button.grid()
  ```   

2. Place the entry box widget in row 0, column 0.

  ```python
  new_entry_box.grid(row=0, column=0)
  ```

3. Place the button widget in row 0, column 1.

  ```python
  new_button.grid(row=0, column=1)
  ```

4. Run the script.

  ```python
  from Tkinter import *  

  root = Tk()  

  new_entry_box = Entry(root)
  new_entry_box.grid(row=0, column=0)  

  new_button = Button(root)
  new_button.grid(row=0, column=1)  

  root.mainloop()
  ```
