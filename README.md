# python_tkinter_alpha

- Tkinter is mainly used to build desktop applications with an user interface.
- Tkinter comes from python installation itself.
- To check if tkinter is available in your machine run the below file it should display a popup.

```python
import tkinter

tkinter._test()
```

## Label

- To add a label with tkinter use the ttk.Label and provide appropriate options
- For label, we can pass text and styling options.
- the `.pack()` function at the end is used to build the label on to the root element.
- Root element is `tk.Tk()`.
- For initiating the event look we need to use `root.mainloop()`

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text="This is an example app", padding=(30, 10)).pack()

root.mainloop()
```

## Buttons

```python
import tkinter as tk
from tkinter import ttk


def greet():
    print("Example project")


root = tk.Tk()
greet_button = ttk.Button(text="greet", command=greet, padding=(20, 10))
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(text="quit", command=root.destroy, padding=(20, 10))
quit_button.pack(side="left", fill="x")

root.mainloop()
```

- Use `ttk.Button` for adding a button
- With `command` option pass in a function which will be triggered on clicking button.
- Styling can be done.
- Use `root.destroy` as for command to quit the root window.
- While applaying pack, side on which the control should be stuck can be passed with `side` option.
- Use `fill` option for occupying available space