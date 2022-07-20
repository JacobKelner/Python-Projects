import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil




from datetime import datetime, timedelta
 
 
# Using current time
ini_time_for_now = datetime.now()
 
# printing initial_date
print ("initial_date", str(ini_time_for_now))
 
# Calculating future dates
# for two years
past_date_after_24hrs = ini_time_for_now - \
                        timedelta(days = 1)
 
# printing calculated future_dates
print('past_date_after_24hrs:', str(past_date_after_24hrs))
print('ini_time_for_now', str(ini_time_for_now))


print(os.path.getmtime(r'C:\Users\15037\Documents\GitHub\Python-Projects\Python Projects\Customer Source'))

class ParentWindow(Frame):
    def __init__(self, master):
        #creates function to select source directory.
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")       
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command = self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))       
        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
        #Creates button to select destination of files from destination directory
        self.desDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.desDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))
        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
        #Creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir=tkinter.filedialog.askdirectory()
        #The .delete(0,END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0,END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

 
    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:
            #we are saying  move the files represented by i to their new destination
            time=datetime.now()
            modi=os.path.getmtime(i)
            timee = time - modi
            if (timee > datetime.timedelta(days=1)):
                print('old')
            else:
                print('new')
                shutil.move(source+i, destination)



    #Creates an Exit button
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells Python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
