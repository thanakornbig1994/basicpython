from tkinter import *
import glob
import datetime
import textfsm
import csv
import os
import pathlib
from tkinter import filedialog as fd
from tkinter import messagebox
from datetime import datetime


def Browse_input():
    global filename_input
    # get a directory path by user
    filename_input = fd.askdirectory(initialdir=r"F:\python\pythonProject",
                                     title="Dialog box")
    Label(root, text=str(filename_input), font=('Aerial 8')).place(x=170, y=30, width=500, height=25)
    print(filename_input)
    return filename_input

def Browse_output():
    global filename_output
    # get a directory path by user
    filename_output = fd.askdirectory(initialdir=r"F:\python\pythonProject",
                                    title="Dialog box")
    Label(root, text=str(filename_output), font=('Aerial 8')).place(x=170, y=80, width=500, height=25)
    print(filename_output)
    return filename_output

def Cancel_Button():
    root.destroy()

def Run_Program():
    #################TIME######################
    # datetime object containing current date and time
    TIME = datetime.now()
    print("now =", TIME)
    # dd/mm/YY H:M:S
    dt_string = TIME.strftime("%d%m%Y_%H%M%S")
    print("date and time =", dt_string)
    Final_input = (dt_string+'.txt')
    Final_output = ('/' + dt_string + '_' + 'Output.csv')
    #########################################################################
    global filename_input
    global filename_output
    #print(filename_input)
    #print(filename_output)
    if filename_input and filename_output != None:
        print("PASS")
        filename_input = filename_input + "/*.txt"
        read_files = glob.glob((filename_input))
        with open(Final_input, "wb") as outfile:
            for f in read_files:
                Path1 = pathlib.PurePath(f).name.encode()
                print(Path1)
                outfile.write(Path1)
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                Endtext = ('\n' + '*************************' + '\n').encode()
                outfile.write(Endtext)

        input_file = open(Final_input, encoding='utf-8')
        raw_text_data = input_file.read()
        input_file.close()

        # Run the text through the FSM.
        # The argument 'template' is a file handle and 'raw_text_data' is a
        # string with the content from the show_inventory.txt file
        template = open(r"C:\Users\Office-BIG\Desktop\InventoryFinal\show_inventory_multiple.textfsm")
        re_table = textfsm.TextFSM(template)
        fsm_results = re_table.ParseText(raw_text_data)

        print(re_table.header)

        with open(filename_output+Final_output, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(re_table.header)
            writer.writerows(fsm_results)

        ############ Remove combinetxt file ###########
        if os.path.exists(Final_input):
            os.remove(Final_input)
        else:
            print("The file does not exist")
        messagebox.showinfo(title="Inventory Editor",message="Done")
        root.destroy()
    else:
        print("Choose Input or Output Path")
        messagebox.showinfo(title="Inventory Editor", message="Choose Input or Output Path!")
        #Label(root, text="Choose Input or Output Path!", font=('Aerial 8')).place(x=450, y=170, width=500, height=25)



root = Tk()
root.title("Cisco Inventory Editor")
root.geometry("800x200")

filename_input = None
filename_output = None

#Input Welcome Label
myLabel1 = Label(root,text="Welcome to Cisco Inventory Editor").pack()
myLabel2 = Label(root,text="Input Path").place(x=10,y=30,width=150,height=30)
myLabel3 = Label(root,text="Output Path").place(x=10,y=80,width=150,height=30)
myLabel4 = Label(root,bg="#111111",).place(x=170,y=30,width=500,height=25)
myLabel5 = Label(root,bg="#111111",).place(x=170,y=80,width=500,height=25)

#Button input

btn1 = Button(root,text="Browse",command=Browse_input).place(x=700,y=30,width=80,height=30)
btn2 = Button(root,text="Browse",command=Browse_output).place(x=700,y=80,width=80,height=30)
btn3 = Button(root,text="Run",command=Run_Program).place(x=300,y=120,width=100,height=40)
btn4 = Button(root,text="Cancel",command=Cancel_Button).place(x=470,y=120,width=100,height=40)

root.mainloop()