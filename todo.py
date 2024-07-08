
import tkinter
from tkinter import *
 

 
root = Tk()
root.title("To-Do-List")
#root.geometry("400x650+400+100)

root.resizable(True,True)

for i in range(4):  # Adjust the range based on your layout
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)




task_list =[]
def addTask():
    task= task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)
'''
def updateListbox():
    listbox.delete(0, tkinter.END)
    for task, checked in task_list:
        check_button = tkinter.Checkbutton(listbox, text=task, variable=checked, onvalue=True, offvalue=False,
                                      command=updateTaskStatus)
        check_button.pack(anchor="w")

def updateTaskStatus():
    with open("tasklist.txt", 'w') as taskfile:
        for task, checked in task_list:
            taskfile.write(f"{task},{checked}\n")'''





def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks= taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()

#Icon
Image_icon = PhotoImage(file="C:/Users/hp/Downloads/task (1).png")
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage(file="C:/Users/hp/Downloads/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="C:/Users/hp/OneDrive/Pictures/New folder/dock.png ")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)


noteImage=PhotoImage(file="C:/Users/hp/Downloads/Image-20240626T144823Z-001/Image/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)

heading =Label(root,text="All Task",font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=130,y=20)


#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0, command=addTask)
button.place(x=300,y=0)
root.bind('<Return>', lambda event: addTask())

#listbox
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack(fill="both", expand=True)
 
# Add checkboxes to each task
'''def toggleCheckbox(index):
    task_list[index] = not task_list[index]
    updateListbox()

for i, task in enumerate(task_list):
    var = tkinter.BooleanVar(value=task)
    check_button = tkinter.Checkbutton(listbox, text=task, variable=var, onvalue=True, offvalue=False,
                                  command=lambda i=i: toggleCheckbox(i))
    check_button.pack(anchor="w")'''
 



openTaskFile()

#delete
Delete_icon=PhotoImage(file="C:/Users/hp/Downloads/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)



root.mainloop()
