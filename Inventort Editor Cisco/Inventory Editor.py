import glob
import textfsm
import csv
import os
import pathlib

read_files = glob.glob(r"C:\Users\Office-BIG\Desktop\JustPython\Network Inventory\inventory1\*.txt")

with open("result1.txt", "wb") as outfile:
    for f in read_files:
        Path1 = pathlib.PurePath(f).name.encode()
        print(Path1)
        outfile.write(Path1)
        with open(f, "rb") as infile:
            outfile.write(infile.read())
        Endtext = ('\n'+'*************************'+'\n').encode()
        outfile.write(Endtext)

input_file = open("result1.txt", encoding='utf-8')
raw_text_data = input_file.read()
input_file.close()

# Run the text through the FSM.
# The argument 'template' is a file handle and 'raw_text_data' is a
# string with the content from the show_inventory.txt file
template = open("show_inventory_multiple.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

print(re_table.header)

with open('OutputInventory1234.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(re_table.header)

    writer.writerows(fsm_results)

############ Remove combinetxt file ###########
if os.path.exists("result1.txt"):
  os.remove("result1.txt")
else:
  print("The file does not exist")