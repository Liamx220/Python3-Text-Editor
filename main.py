from tkinter import * 

from tkinter.filedialog import asksaveasfile
from tkinter import filedialog



root = Tk()

root.geometry ("400x450")
root.resizable(0,0)
root.configure(bg='black')

T = Text(root, height=25, width=400, bg='black',bd=0,fg='white',borderwidth=0, highlightthickness=0)
T.insert(END, "Put text here!\n")
T.pack()
def file_save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes = files)
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(T.get(0.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()
b = Button(text='Save', command = file_save)
b.pack()

mainloop()