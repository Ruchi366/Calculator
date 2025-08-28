# Calculator
#My First Python Project
import tkinter as tk
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            expr = expression.replace('√','sqrt')
            expr = expression.replace('^','**')
            expr = expression.replace('ln','log')
            expr = expression.replace('log','log10')
            expr = expression.replace('e',str(e))
            expr = expression.replace('!','factorial')
            result=eval(expr)
            screen.set(result)
            expression=str(result)
        except Exception:
            screen.set("Error")
            expression=" "
    elif text == "C":
        expression=" "
        screen.set(expression)
    else:
        if text in ['√','log','ln','sin','cos','tan','factorial','e']:
            expression+=f"{text}("
        elif text == ")":
            expression+=")"
        elif text=="!":
            expression+="!"
        else:
            expression += text
            screen.set(expression)
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
expression = " "
screen = tk.StringVar()

entry = tk.Entry(root,textvar=screen,font="Arial 20 bold")
entry.pack(fill="both",ipadx=8,padx=10,pady=10)
buttons = [
    ['log','ln','√','^','e'],
    ['7','8','9','/','C'],
    ['4','5','6','*','('],
    ['1','2','3','-',')'],
    ['0','.','=','+','^'],
    ['!','sin','cos','tan',' o(=•ェ•=)m']
    ]
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True,fill="both")
    for btn in row:
        b= tk.Button(frame,text=btn,font="Arial 15",height=2,width=5)
        b.pack(side="left",expand=True,fill="both")
        b.bind("<Button-1>",click)

root.mainloop()ct Responsive Calculator.
