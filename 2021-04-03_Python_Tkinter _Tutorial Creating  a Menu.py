#Tutorial Creating Menu-tkinter_Template 0
# Computer Programming Tutor_April 2, 2021

from tkinter import *
class Window(Frame):
    #Define Settings Uppon Initialisation
    def __init__(self,master=None):
        Frame.__init__(self,master)

        # Reference to the Master Widget
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # Changing the Title of Master Widget
        self.master.title("Ernie's Computer Programming Application")
        #Allowing the Widget to take the full Space
        self.pack(fill=BOTH,expand=1)

        #Creation of Menu InstNCE
        menu =Menu(self.master)
        self.master.config(menu=menu)

        #Creation of CPAFile Object
        CPAFile = Menu(menu)
        CPAFile.add_command(label="New",)
        CPAFile.add_command(label="Open",)
        CPAFile.add_command(label="Exit",command=self.client_exit)

        #Add "CPAFile" to the Menu
        menu.add_cascade(label="File",menu=CPAFile)

        # Create The CPAEdit Object
        CPAedit=Menu(menu)
        CPAedit.add_command(label ="Undo")
        CPAedit.add_command(label="Redo")
        CPAedit.add_command(label="Copy")

        # Added "CPAedit" to the Menu
        menu.add_cascade(label="Edit",menu=CPAedit)

    def client_exit(self):
        exit()

#Create Root Window
root = Tk()

root.geometry("800x500")
#Creating the Instance
app = Window(root)

root.mainloop()


        
            
