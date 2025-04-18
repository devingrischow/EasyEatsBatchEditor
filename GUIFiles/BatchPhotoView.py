import customtkinter
import cv2
import tkinter as tk
from tkinter import filedialog
from BatchEditorFiles import photoEditor 
import os


#Set the theme of the windows 
customtkinter.set_appearance_mode("blue")




#camera connection 


class BatchPhotoView:
    def __init__(self):

        #Main Window 
        self.main_window = customtkinter.CTk()
        self.main_window.geometry("900x234")

        self.main_window.title("Easy Easts photo Batch Editor") #Title


        #New Batch Name Entry Frame 
        self.batch_entry_frame = customtkinter.CTkFrame(self.main_window, height=200)
        self.batch_entry_frame.pack(pady=25)

        #status label(Steps NEED a name), also for any other warnings (like camera not found)
        self.statusLabel = customtkinter.CTkLabel(self.batch_entry_frame, text="")
        self.statusLabel.pack()

        #New Steps Batch Name Label
        self.steps_name_label = customtkinter.CTkLabel(self.batch_entry_frame, text="Step Names:")
        self.steps_name_label.pack(side='left', padx=20)

        #Steps Name Entry Box
        self.steps_name_entry = customtkinter.CTkEntry(self.batch_entry_frame,width=200)
        self.steps_name_entry.pack(side='right')


        #Select Destinations Frame
        #Handles The Select Input File And The Output Destination Buttons 
        self.destinationsFrame = customtkinter.CTkFrame(self.main_window, width=900)
        self.destinationsFrame.pack(pady=4)

        

        #-----Choose video input  Section----
        self.open_choose_input_folder_dialog_box = customtkinter.CTkButton(self.destinationsFrame, text="Choose Video Input Folder", command=self.open_and_select_Input_location)
        self.open_choose_input_folder_dialog_box.pack(side='left', padx=20)

        #Placeholder for input folder entry box
        self.placeholderFolderInputNameStringVar = tk.StringVar(self.main_window, "IngredietImageOutput")

        #Input File Entry Box 
        self.input_entry_box = customtkinter.CTkEntry(self.destinationsFrame,textvariable=self.placeholderFolderInputNameStringVar,state='disabled', width=300)
        self.input_entry_box.pack(side='left', pady=10)



        #-----Choose Video Output Section----
        self.open_choose_output_dialog_box = customtkinter.CTkButton(self.destinationsFrame, text="Choose Output Folder Destination", command=self.open_and_select_output_location)
        self.open_choose_output_dialog_box.pack(side='left', padx=20)

        #Video Output Placeholder (Default is Dedicated Output File)
        self.placeholderFileNameStringVar = tk.StringVar(self.main_window, "StepsOutput")

        #Output Entry Box
        self.output_entry_box = customtkinter.CTkEntry(self.destinationsFrame,textvariable=self.placeholderFileNameStringVar,state='disabled', width=300)
        self.output_entry_box.pack(side='right', pady=10)


        #Start Edit Button Frame 

        self.start_edit_button_frame = customtkinter.CTkFrame(self.main_window, height=100)
        self.start_edit_button_frame.pack()


        self.startEditButton = customtkinter.CTkButton(self.start_edit_button_frame, text="Start Edit", height=70, width=200, command=self.start_Editing_Batch)
        self.startEditButton.pack()

        cv2.waitKey(25)
        self.main_window.mainloop()


    #Function to let the user select the Video input file destination
    def open_and_select_Input_location(self):
        filePath = filedialog.askdirectory(initialdir="photoOutput",
                                          title="Choose New Ingredient Output Location")
        
        self.placeholderFolderInputNameStringVar.set(str(filePath))
        
        return filePath


    #Function to let the user select the desired file destination for the Videos Output
    def open_and_select_output_location(self):
        filePath = filedialog.askdirectory(initialdir="photoOutput",
                                          title="Choose New Ingredient Output Location")
        
        self.placeholderFileNameStringVar.set(str(filePath))
        
        return filePath
    

    #start and open the batch editing sequence 
    def start_Editing_Batch(self):
        input_file_location = self.input_entry_box.get()
        output_File_location = self.output_entry_box.get()
        #photoName = self.steps_name_entry.get()        
        for filename in os.scandir(input_file_location):
            if filename.is_file():
                # get the iterationNumber from the filename 
                #stepIteration = str(filename).find('-') + 1
                #stepNumber = str(filename)[stepIteration]
                #print("step iteration", stepIteration)
                editor = photoEditor
                editor.editPhoto(filename.name, filename.path, output_File_location)
                #editor.batchVideoEditor(video_to_edit_File=filename.path, output_filePath=output_File_location, stepNumber=stepNumber, stepName=videoNames)
                print(filename.path, "done")

    
    






       





