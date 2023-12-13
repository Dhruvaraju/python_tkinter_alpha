# python_tkinter_alpha

- Tkinter is mainly used to build desktop applications with an user interface.
- Tkinter comes from python installation itself.
- To check if tkinter is available in your machine run the below file it should display a popup.

```python
import tkinter

tkinter._test()
```

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