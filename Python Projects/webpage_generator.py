import webbrowser
from tkinter import *

webbrowser.open_new_tab('index.html')


def Submit():#function called on inside Button()
    text = txtfld.get()
    #below is the html page that will display
    html_template="""
    <html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>
    """.format(text)
    f = open("index.html", "w")
    #writing code into file
    f.write(html_template)#write allows for user to overwrite any existing content
    f.close()




window=Tk() # this is the GUI
btn=Button(window, text="To confirm body, click here", fg='blue', command=Submit)
btn.place(x=65, y=20)#button placement
txtfld=Entry(window, text="", bd=5)#allows for user input/entry
txtfld.place(x=75, y=70)#text box placement
window.title('Webpage Generator')#displayed title of GUI
window.geometry("300x200+10+10")#window dimensions
window.mainloop()





if __name__ == "__main__":
    print(Submit())
