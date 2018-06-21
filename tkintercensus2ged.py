#clear the log file
try:
    with open("myapp.log", 'w') as the_file:
        the_file.close()
except:
    pass

#Imports
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pickle
import sys

#modify system path
sys.path.insert(0, "./Sweden-Household-Surveys")
sys.path.insert(0, "./Sweden-Household-Surveys/Word-Lists")

#import custom modules
from header import *
from census1850 import *
from census1860 import *
from census1870 import *
from census1880 import *
from census1900 import *
from census1910 import *
from household1881_1885 import *



#load up that pickle
try:
    with open('config.pickle', 'rb') as handle:
        user_config = pickle.load(handle)
        print (user_config)
except:
    print("couldn't load user config")
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        self.create_widgets()


    #change the gui based on the option selected
    def guiUpdate(self, value):
        
        #gui updated to US options
        if value == "United States":

            print("switched to USA")

            #if there is already a grid, forget it
            try:
                self.frame.grid_forget()
            except:
                pass

            #create the frame
            self.frame = tk.Frame(root)
            self.frame.grid(sticky = 'nsew')

            #United States Vars

            #checkbox Immigration
            self.optionImmigration = tk.IntVar(self)
            #checkbox Occupation
            self.optionOccupation = tk.IntVar(self)
            #checkbox Race
            self.optionRace = tk.IntVar(self)
            #checkbox literacy
            self.optionLiteracy=tk.IntVar(self)
            #checkbox Disability
            self.optionDisability=tk.IntVar(self)
            #checkbox Children Born
            self.optionChildrenBorn=tk.IntVar(self)
            #checkbox Military
            self.optionMilitary=tk.IntVar(self)
            #checkbox Property
            self.optionProperty=tk.IntVar(self)
            #checkbox Language
            self.optionLanguage=tk.IntVar(self)
            #checkbox Naturalization
            self.optionNaturalize=tk.IntVar(self)

            #update Immigration variable
            self.optionImmigration.trace('w', self.__update_immigration__)

            #update Occupation variable
            self.optionOccupation.trace('w', self.__update_occupation__)
            
            #update Race variable
            self.optionRace.trace('w', self.__update_race__)

            #update Literacy variable
            self.optionLiteracy.trace('w', self.__update_literacy__)

            #update disability variable
            self.optionDisability.trace('w', self.__update_disability__)

            #update children variable
            self.optionChildrenBorn.trace('w', self.__update_children__)

            #update Military variable
            self.optionMilitary.trace('w', self.__update_military__)

            #update Property variable
            self.optionProperty.trace('w', self.__update_property__)

            #update Language variable
            self.optionLanguage.trace('w', self.__update_language__)

            #update Naturalization variable
            self.optionNaturalize.trace('w', self.__update_naturalize__)


            #label for Tag Inclusion
            includeTagLabel = tk.Label(self.frame, text="Tags to include",font = "Helvetica 10 bold underline")
            #render on left side of screen
            includeTagLabel.grid(row = 4, sticky="w")

            #label for custom tagging
            includeCustomLabel = tk.Label(self.frame, text="Custom tag name",font = "Helvetica 10 bold underline")
            #render on left side of screen
            includeCustomLabel.grid(row = 4, column = 1, sticky="w")

            #---checkbutton widgets---#
 
            #Immigration
            self.CheckboxImmigration = tk.Checkbutton(self.frame, text="Immigration Year", variable=self.optionImmigration)
            self.CheckboxImmigration.grid(row=5, sticky="w")    
                    
            #Immigration tag entry box
            self.immigrationSet = tk.Entry(self.frame)
            self.immigrationSet.grid(row=5,column=1, sticky = "w")
            
            #Occupation
            self.CheckboxOccupation = tk.Checkbutton(self.frame, text="Occupation", variable=self.optionOccupation)
            self.CheckboxOccupation.grid(row=5,column=2, sticky="w")

            #Occupation tag entry box
            self.occupationSet = tk.Entry(self.frame)
            self.occupationSet.grid(row=5,column=3, sticky = "w")

            #Race
            self.CheckboxRace = tk.Checkbutton(self.frame,text="Race", variable=self.optionRace)
            self.CheckboxRace.grid(row=6, sticky="w")

            #Race tag entry box
            self.raceSet = tk.Entry(self.frame)
            self.raceSet.grid(row=6,column=1, sticky = "w")

            #Literacy
            self.CheckboxLiteracy = tk.Checkbutton(self.frame, text = "Literacy", variable=self.optionLiteracy)
            self.CheckboxLiteracy.grid(row=6, column = 2, sticky = "w")
            
            #Literacy tag entry box
            self.literacySet = tk.Entry(self.frame)
            self.literacySet.grid(row=6,column=3, sticky = "w")


            #Disability
            self.CheckboxDisability = tk.Checkbutton(self.frame, text = "Disability", variable = self.optionDisability)
            self.CheckboxDisability.grid(row = 7, sticky = "w")
            
            #Disability tag entry box
            self.disabilitySet = tk.Entry(self.frame)
            self.disabilitySet.grid(row=7,column=1, sticky = "w")

            #Children Born
            self.CheckboxChildrenBorn = tk.Checkbutton(self.frame, text="Children Born", variable = self.optionChildrenBorn)
            self.CheckboxChildrenBorn.grid(row=7, column=2, sticky="w")

            #Children Born tag entry box
            self.childrenBornSet = tk.Entry(self.frame)
            self.childrenBornSet.grid(row=7,column=3, sticky = "w")

            #Military
            self.CheckboxMilitary = tk.Checkbutton(self.frame, text="Military", variable=self.optionMilitary)
            self.CheckboxMilitary.grid(row=8,sticky="w")

            #Military tag entry box
            self.militarySet = tk.Entry(self.frame)
            self.militarySet.grid(row=8,column=1, sticky = "w")

            #Property
            self.CheckboxProperty = tk.Checkbutton(self.frame, text = "Property", variable=self.optionProperty)
            self.CheckboxProperty.grid(row=8,column=2,sticky="w")

            #Property tag entry box
            self.propertySet = tk.Entry(self.frame)
            self.propertySet.grid(row=8,column=3, sticky = "w")

            #Language
            self.CheckboxLanguage = tk.Checkbutton(self.frame,text="Language", variable=self.optionLanguage)
            self.CheckboxLanguage.grid(row=9,sticky="w")

            #Language tag entry box
            self.languageSet = tk.Entry(self.frame)
            self.languageSet.grid(row=9,column=1, sticky = "w")

            #Naturalization
            self.CheckboxNaturalize = tk.Checkbutton(self.frame,text="Naturalization", variable=self.optionNaturalize)
            self.CheckboxNaturalize.grid(row=9, column=2,sticky="w")

            #Naturalization tag entry box
            self.naturalizeSet = tk.Entry(self.frame)
            self.naturalizeSet.grid(row=9,column=3, sticky = "w")

            #set up previous user configurations for USA
            try:
                if user_config["UnitedStates"]["Race"] == 1:
                    self.CheckboxRace.select()
                if user_config["UnitedStates"]["Military"] == 1:
                    self.CheckboxMilitary.select()
                if user_config["UnitedStates"]["Literacy"] == 1:
                    self.CheckboxLiteracy.select()
                if user_config["UnitedStates"]["Immigration"] == 1:
                    self.CheckboxImmigration.select()
                if user_config["UnitedStates"]["Disability"] == 1:
                    self.CheckboxDisability.select()
                if user_config["UnitedStates"]["Children Born"] == 1:
                    self.CheckboxChildrenBorn.select()
                if user_config["UnitedStates"]["Occupation"] == 1:
                    self.CheckboxOccupation.select()
                if user_config["UnitedStates"]["Property"] == 1:
                    self.CheckboxProperty.select()
                if user_config["UnitedStates"]["Language"] == 1:
                    self.CheckboxLanguage.select()
                if user_config["UnitedStates"]["Naturalize"] == 1:
                    self.CheckboxNaturalize.select()
                if user_config ["UnitedStates"]["immigTag"] != "IMMI":
                    self.immigrationSet.insert(0, user_config["UnitedStates"]["immigTag"])
                if user_config ["UnitedStates"]["occupTag"] != "OCCU":
                    self.occupationSet.insert(0, user_config["UnitedStates"]["occupTag"])
                if user_config ["UnitedStates"]["raceTag"] != "DSCR":
                    self.raceSet.insert(0, user_config["UnitedStates"]["raceTag"])
                if user_config ["UnitedStates"]["natuTag"] != "NATU":
                    self.naturalizeSet.insert(0, user_config["UnitedStates"]["natuTag"])
                if user_config ["UnitedStates"]["literTag"] != "EDUC":
                    self.literacySet.insert(0, user_config["UnitedStates"]["literTag"])
                if user_config ["UnitedStates"]["chilTag"] != "DSCR":
                    self.childrenBornSet.insert(0, user_config["UnitedStates"]["chilTag"])
                if user_config ["UnitedStates"]["langTag"] != "DSCR":
                    self.languageSet.insert(0, user_config["UnitedStates"]["langTag"])
                if user_config ["UnitedStates"]["militTag"] != "DSCR":
                    self.militarySet.insert(0, user_config["UnitedStates"]["militTag"])
                if user_config ["UnitedStates"]["disiTag"] != "DSCR":
                    self.disabilitySet.insert(0, user_config["UnitedStates"]["disiTag"])
                if user_config ["UnitedStates"]["propTag"] != "PROP":
                    self.propertySet.insert(0, user_config["UnitedStates"]["propTag"])

            except:
                print("nope")

            #CSV file select label
            self.PathLabel = tk.Label(self.frame)
            self.PathLabel.grid(row=10,column=1, sticky="w")

            #CSV file select button
            self.BrowseButton = tk.Button(self.frame, text="Input CSV",font = "Helvetica 10 bold", command=self.browse_func)
            self.BrowseButton.grid(row=10, sticky ="w")

            #submit button
            self.submit = tk.Button(self.frame, text="Submit",
                                    command = self.__Submit_Button__)
            self.submit.grid(row=11,column=1, sticky="w")

            #Quit button
            self.quit = tk.Button(self.frame, text="QUIT", fg="red",
                                 command= self.quit_sequence)
            self.quit.grid(row =11, column =2,sticky="w")
        
        #gui updated to English Options
        if value == "England":

            print("Switched to England")

            #if grid already exists, forget it
            try:
                self.frame.grid_forget()
            except:
                pass

            #create the frame
            self.frame = tk.Frame(root)
            self.frame.grid(sticky = 'nsew')

            #label for Tag Inclusion
            includeTagLabel = tk.Label(self.frame, text="Tags to include",font = "Helvetica 10 bold underline")
            #render on left side of screen
            includeTagLabel.grid(row = 4, sticky="w")

            #label for custom tagging
            includeCustomLabel = tk.Label(self.frame, text="Custom tag name",font = "Helvetica 10 bold underline")
            #render on left side of screen
            includeCustomLabel.grid(row = 4, column = 1, sticky="w")


        #gui updated to Swedish Options
        if value == "Sweden":

            print("Switched to Sweden")

            #if grid already exists, forget it
            try:
                self.frame.grid_forget()
            except:
                pass

            #create the frame
            self.frame = tk.Frame(root)
            self.frame.grid(sticky = 'nsew')

        #Swedish vars

            #checkbox Swedish Occupation
            self.optionSwedOccupation=tk.IntVar(self)

            #checkbox Swedish Communion
            self.optionSwedCommunion=tk.IntVar(self)

            #checkbox Swedish Examination
            self.optionSwedExamination=tk.IntVar(self)

            #checkbox Swedish moving in records
            self.optionSwedMovingIn= tk.IntVar(self)

            #checkbox Swedish moving out records
            self.optionSwedMovingOut= tk.IntVar(self)

            #checkbox Swedish death records
            self.optionSwedDeath= tk.IntVar(self)

            #Swedish vars

            #update occupation value
            self.optionSwedOccupation.trace('w', self.__update_swedOccupation__)

            #update Communion value
            self.optionSwedCommunion.trace('w', self.__update_swedCommunion__)

            #update Examination value
            self.optionSwedExamination.trace('w', self.__update_swedExamination__)

            #update Moving In value
            self.optionSwedMovingIn.trace('w', self.__update_swedMovingIn__)

            #update Moving Out value
            self.optionSwedMovingOut.trace('w', self.__update_swedMovingOut__)

            #update Death value
            self.optionSwedDeath.trace('w', self.__update_swedDeath__)

            #label for Swedish tags to include
            swedishTagLabel = tk.Label(self.frame, text='Tags to include',font = "Helvetica 10 bold underline")
            swedishTagLabel.grid(row = 4, column = 0,sticky="w")
            

            #checkboxes


            #Occupation
            self.CheckboxSwedOccupation = tk.Checkbutton(self.frame, text="Occupation", variable=self.optionSwedOccupation)
            self.CheckboxSwedOccupation.grid(row=6, sticky="w") 

            #Occupation tag entry box
            self.swedOccupationSet = tk.Entry(self.frame)
            self.swedOccupationSet.grid(row=6,column=1, sticky = "w")

            #Communion
            self.CheckboxSwedCommunion = tk.Checkbutton(self.frame, text="Communion", variable=self.optionSwedCommunion)
            self.CheckboxSwedCommunion.grid(row=7, sticky="w")

            #Communion tag entry box
            self.swedCommunionSet = tk.Entry(self.frame)
            self.swedCommunionSet.grid(row=7,column=1, sticky = "w")

            #Examination
            self.CheckboxSwedExamination = tk.Checkbutton(self.frame, text="Examination", variable=self.optionSwedExamination)
            self.CheckboxSwedExamination.grid(row=8, sticky="w")

            #Examination tag entry box
            self.swedExaminationSet = tk.Entry(self.frame)
            self.swedExaminationSet.grid(row=8,column=1, sticky = "w")

            #Moving In
            self.CheckboxSwedMovingIn = tk.Checkbutton(self.frame, text="Moving In Records", variable=self.optionSwedMovingIn)
            self.CheckboxSwedMovingIn.grid(row=9, sticky="w")

            #Moving in tag entry box
            self.swedMovingInSet = tk.Entry(self.frame)
            self.swedMovingInSet.grid(row=9,column=1, sticky = "w")

            #Moving Out
            self.CheckboxSwedMovingOut = tk.Checkbutton(self.frame, text="Moving Out Records", variable=self.optionSwedMovingOut)
            self.CheckboxSwedMovingOut.grid(row=10, sticky="w")

            #Moving Out tag entry box
            self.swedMovingOutSet = tk.Entry(self.frame)
            self.swedMovingOutSet.grid(row=10,column=1, sticky = "w")

            #Death
            self.CheckboxSwedDeath = tk.Checkbutton(self.frame, text="Death", variable=self.optionSwedDeath)
            self.CheckboxSwedDeath.grid(row=11, sticky="w")

            #Death tag entry box
            self.swedDeathSet = tk.Entry(self.frame)
            self.swedDeathSet.grid(row=11,column=1, sticky = "w")

            #set up previous user configurations for Sweden
            try:
                #Swedish Occupation
                if user_config["Sweden"]["swedOccupation"] == 1:
                    self.CheckboxSwedOccupation.select()

                #Swedish Comunion
                if user_config["Sweden"]["swedCommunion"] == 1:
                    self.CheckboxSwedCommunion.select()

                #Swedish Examination
                if user_config["Sweden"]["swedExamination"] == 1:
                    self.CheckboxSwedExamination.select()

                #Swedish moving in
                if user_config["Sweden"]["swedMovingIn"] == 1:
                    self.CheckboxSwedMovingIn.select()

                #Swedish moving out
                if user_config["Sweden"]["swedMovingOut"] == 1:
                    self.CheckboxSwedMovingOut.select()

                #Swedish death
                if user_config["Sweden"]["swedDeath"] == 1:
                    self.CheckboxSwedDeath.select()

                #Swedish occupation tag
                if user_config ["Sweden"]["swedOccupTag"] != "OCCU":
                    self.swedOccupationSet.insert(0, user_config["Sweden"]["swedOccupTag"])

                #Swedish communion tag
                if user_config ["Sweden"]["swedCommTag"] != "ORDI":
                    self.swedCommunionSet.insert(0, user_config["Sweden"]["swedCommTag"])

                #Swedish examination tag
                if user_config ["Sweden"]["swedExamTag"] != "ORDI":
                    self.swedExaminationSet.insert(0, user_config["Sweden"]["swedExamTag"])

                #Swedish moving in tag
                if user_config ["Sweden"]["swedMoveInTag"] != "IMMI":
                    self.swedMovingInSet.insert(0, user_config["Sweden"]["swedMoveInTag"])

                #Swedish moving out tag
                if user_config ["Sweden"]["swedMoveOutTag"] != "IMMI":
                    self.swedMovingOutSet.insert(0, user_config["Sweden"]["swedMoveOutTag"])

                #Swedish death tag
                if user_config ["Sweden"]["swedDeathTag"] != "IMMI":
                    self.swedDeathSet.insert(0, user_config["Sweden"]["swedDeathTag"])

            except:
                pass


            #CSV file select label
            self.PathLabel = tk.Label(self.frame)
            self.PathLabel.grid(row=12,column=1, sticky="w")

            #CSV file select button
            self.BrowseButton = tk.Button(self.frame, text="Input CSV",font = "Helvetica 10 bold", command=self.browse_func)
            self.BrowseButton.grid(row=12, sticky ="w")
            #submit button
            self.submit = tk.Button(self.frame, text="Submit",
                                    command = self.__Submit_Button__)
            self.submit.grid(row=13,column=1, sticky="w")
            
            #Quit button
            self.quit = tk.Button(self.frame, text="QUIT", fg="red",
                                 command= self.quit_sequence)
            self.quit.grid(row =13, column =2,sticky="w")

    def create_widgets(self):

        #dictionary of countries
        self.dict = {'United States': ['1850', '1860', '1870', '1880','1900','1910'],
                    'England': ['1', '2', '3'],
                    'Sweden':['1881-1885','2','3']}


        #Label for the whole thing
        wholeLabel = tk.Label(self, text="Census2Ged", font = ("Lobster", 14, "bold italic"))
        wholeLabel.grid(row=0)

        #gedcom name label
        gednameLabel = tk.Label(self, text="Gedcom Name:", font = "Helvetica 10 bold")
        gednameLabel.grid(row=1, column=1, sticky ="e")
        #gedcom name selector
        self.gedNameSet = tk.Entry(self)
        self.gedNameSet.grid(row=1,column=2, sticky = "w")
        
        #label for country selector
        countryLabel = tk.Label(self, text="Country:", font = "Helvetica 10 bold")
        #render on left side of screen
        countryLabel.grid(row = 2,column=1, sticky="e")
        

        #label for year selector
        countryLabel = tk.Label(self, text="Census year:",font = "Helvetica 10 bold")
        #render on left side of screen
        countryLabel.grid(row = 3, column=1, sticky="e")

        #country selector
        self.countrySelect = tk.StringVar(self)
        #year selector
        self.yearSelect = tk.StringVar(self)


        #update year select based on country select
        self.countrySelect.trace('w', self.update_options)
        
        #update country variable
        self.countrySelect.trace('w', self.__update_country__)
        

        #update year variable
        self.yearSelect.trace('w', self.__update_year__)


        #render the country options menu
        self.countryOptions = tk.OptionMenu(self, self.countrySelect, *self.dict.keys(), command= self.guiUpdate)
        self.yearOptions = tk.OptionMenu(self, self.yearSelect, '')


        #set United States as the default value
        self.countrySelect.set("United States")

        #render on right side of widget
        self.countryOptions.grid(row = 2, column = 2, sticky="w")
        self.yearOptions.grid(row=3,column=2, sticky="w")

        #instantiate the frames
        self.guiUpdate("United States")


    #quit
    def quit_sequence(self, *args):
        #set the list of entries
        varsMain, unitedStatesVars, swedishVars = self.__Update_Checkbox_List__()
        #save the current file configuration
        with open ("config.pickle", 'wb') as config_file:
            #full dictionary of variables
            fullVarDict = {"MainVars": varsMain, "UnitedStates": unitedStatesVars, "Sweden":swedishVars}

            pickle.dump(fullVarDict, config_file, protocol=pickle.HIGHEST_PROTOCOL)
        root.destroy()

#var.get() ---checked / 1
#not var.get() ---not checked / 0
    def browse_func(self):
        filename = tk.filedialog.askopenfilename()
        self.PathLabel.config(text=filename)
        return (filename)

    #update options list of years
    def update_options(self, *args):
        countries = self.dict[self.countrySelect.get()]
        self.yearSelect.set(countries[0])

        menu = self.yearOptions['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.yearSelect.set(nation))

    def __update_country__(self, *args):
        Country = self.countrySelect.get()
        return(Country)
    
    def __update_year__(self, *args):
        Year = self.yearSelect.get()
        return(Year)

    def __update_immigration__(self, *args):
        Immigration = self.optionImmigration.get()
        return(Immigration)

    def __update_occupation__(self, *args):
        Occupation = self.optionOccupation.get()
        return(Occupation)

    def __update_race__(self, *args):
        Race = self.optionRace.get()
        return(Race)

    def __update_literacy__(self, *args):
        Literacy = self.optionLiteracy.get()
        return(Literacy)

    def __update_disability__(self, *args):
        Disability = self.optionDisability.get()
        return(Disability)

    def __update_children__(self, *args):
        Children = self.optionChildrenBorn.get()
        return(Children)

    def __update_military__(self, *args):
        Military = self.optionMilitary.get()
        return(Military)

    def __update_property__(self, *args):
        Property = self.optionProperty.get()
        return(Property)

    def __update_language__(self, *args):
        Language = self.optionLanguage.get()
        return(Language)

    def __update_naturalize__(self, *args):
        Naturalize = self.optionNaturalize.get()
        return(Naturalize)

    def __update_swedOccupation__(self, *args):
        swedOccupation = self.optionSwedOccupation.get()
        return(swedOccupation)

    def __update_swedCommunion__(self, *args):
        swedCommunion = self.optionSwedCommunion.get()
        return(swedCommunion)

    def __update_swedExamination__(self, *args):
        swedExamination = self.optionSwedExamination.get()
        return(swedExamination)

    def __update_swedMovingIn__(self, *args):
        swedMovingIn = self.optionSwedMovingIn.get()
        return(swedMovingIn)

    def __update_swedMovingOut__(self, *args):
        swedMovingOut = self.optionSwedMovingOut.get()
        return(swedMovingOut)

    def __update_swedDeath__(self, *args):
        swedDeath = self.optionSwedDeath.get()
        return(swedDeath)

    # create configDictionary with all the values of the fields
    def __Update_Checkbox_List__(self):
        unitedStatesVars = user_config["UnitedStates"]
        swedishVars = user_config["Sweden"]
        varsMain= {
                    "Country": self.countrySelect.get(),
                    "Year" : self.yearSelect.get(), 
                    "Gedname" : self.gedNameSet.get(),    

                    }

        if self.countrySelect.get() == "United States":
            variable_list ={
                            "Year" : self.yearSelect.get(),
                            "Immigration" : self.optionImmigration.get(),
                            "Occupation" : self.optionOccupation.get(),
                            "Race" : self.optionRace.get(),
                            "Literacy" : self.optionLiteracy.get(),
                            "Disability" : self.optionDisability.get(),
                            "Children Born" : self.optionChildrenBorn.get(),
                            "Military" : self.optionMilitary.get(),
                            "Gedname" : self.gedNameSet.get(),
                            "Property" : self.optionProperty.get(),
                            "Language" : self.optionLanguage.get(),
                            "Naturalize" : self.optionNaturalize.get(),
                            "immigTag" : self.immigrationSet.get(),
                            "occupTag" : self.occupationSet.get(),
                            "raceTag" : self.raceSet.get(),
                            "natuTag" : self.naturalizeSet.get(),
                            "literTag" : self.literacySet.get(),
                            "chilTag" : self.childrenBornSet.get(),
                            "langTag" : self.languageSet.get(),
                            "militTag" : self.militarySet.get(),
                            "disiTag" : self.disabilitySet.get(),
                            "propTag" : self.propertySet.get(),
                            }
            unitedStatesVars = variable_list
            print(unitedStatesVars)
        elif self.countrySelect.get() == "Sweden":
            variable_list ={
                            "Year" : self.yearSelect.get(), 
                            "Gedname" : self.gedNameSet.get(),          
                            "swedOccupation" : self.optionSwedOccupation.get(),
                            "swedCommunion" : self.optionSwedCommunion.get(),
                            "swedExamination" : self.optionSwedExamination.get(),
                            "swedMovingIn" : self.optionSwedMovingIn.get(),
                            "swedMovingOut": self.optionSwedMovingOut.get(),
                            "swedDeath": self.optionSwedDeath.get(),
                            "swedOccupTag": self.swedOccupationSet.get(),
                            "swedCommTag": self.swedCommunionSet.get(),
                            "swedExamTag": self.swedExaminationSet.get(),
                            "swedMoveInTag": self.swedMovingInSet.get(),
                            "swedMoveOutTag": self.swedMovingOutSet.get(),
                            "swedDeathTag": self.swedDeathSet.get()
                            }
            swedishVars = variable_list

        return (varsMain, unitedStatesVars, swedishVars)

    def __Submit_Button__(self):

        #Whether or not to use default immigration value
        if len(self.immigrationSet.get()) == 0:
            self.immigrationSet.insert(0, "IMMI")
        #Whether or not to use default occupation value
        if len(self.occupationSet.get()) == 0:
            self.occupationSet.insert(0, "OCCU")
        #Whether or not to use default race value (physical decription tag)
        if len(self.raceSet.get()) == 0:
            self.raceSet.insert(0, "DSCR")
        #Whether or not to use default Naturalize value
        if len(self.naturalizeSet.get()) == 0:
            self.naturalizeSet.insert(0, "NATU")


        #Swedish
        #Whether or not to use default Ordinance values
        if len(self.swedCommunionSet.get()) == 0:
            self.swedCommunionSet.insert(0, "ORDI")
        if len(self.swedExaminationSet.get()) == 0:
            self.swedExaminationSet.insert(0, "ORDI")


        #set the list of entries
        varsMain, unitedStatesVars, swedishVars = self.__Update_Checkbox_List__()
        
        #save the current file configuration
        with open ("config.pickle", 'wb') as config_file:
            #full dictionary of variables
            fullVarDict = {"MainVars": varsMain, "UnitedStates": unitedStatesVars, "Sweden":swedishVars}

            pickle.dump(fullVarDict, config_file, protocol=pickle.HIGHEST_PROTOCOL)
        
        #run the main function
        self.main(fullVarDict)


    #based on the name of the gedcom file and year
    def main (self, configDictionary):
        g = configDictionary["MainVars"]["Gedname"]
        y = configDictionary["MainVars"]["Year"]
        c = configDictionary["MainVars"]["Country"]

        g = str(g +'.ged')

        file_path = self.PathLabel.cget("text")
        printHeader(g)

        if c == 'United States':
            if y == '1850':
                writeName1850(file_path , g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            elif y == '1860':
                writeName1860(file_path , g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            elif y == '1870':
                writeName1870(file_path , g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            elif y == '1880':
                writeName1880(file_path , g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            elif y == '1900':
                writeName1900(file_path , g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            elif y == '1910':
                writeName1910(file_path, g, configDictionary["UnitedStates"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")
            else:
                pass

        elif c == "Sweden":
            if y == "1881-1885":
                writeName1881_1885(file_path , g, configDictionary["Sweden"])
                tk.messagebox.showinfo("Census2Ged", "The gedcom file is complete.")

               
#Run the Gui
root = tk.Tk()
root.minsize(225, 225)

#background color
app = Application(master=root)


app.mainloop()

    
