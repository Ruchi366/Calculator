import tkinter as tk
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = str(eval(expression))
            screen.set(expression)
        except Exception:
            screen.set("Error")
            expression=" "
    elif text == "C":
        expression=" "
        screen.set(expression)
    else:
        expression += text
        screen.set(expression)
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
expression = " "
screen = tk.StringVar()

entry = tk.Entry(root,textvar=screen,font="Arial 20 bold")
entry.pack(fill="both",ipadx=8,padx=10,pady=10)
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ]
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True,fill="both")
    for btn in row:
        b= tk.Button(frame,text=btn,font="Arial 15",height=2,width=5)
        b.pack(side="left",expand=True,fill="both")
        b.bind("<Button-1>",click)
clear_btn = tk.Button(root,text="C",font="Arial 15",height=2)
clear_btn.pack(fill="both")
clear_btn.bind("<Button-1>",click)

root.mainloop()


