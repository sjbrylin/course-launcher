

import tkinter as tk
import datetime, webbrowser, sys


# FONT SELECTION
hdr = ("Times", 20, "bold")
dayHdr = ("Times", 14, "bold")
btnTxt = ("Times", 12)



day = datetime.datetime.today().weekday()
# 0 is Monday, 2 = Tuesday...

if day == 0:
    dayString = "Monday"
elif day == 1:
    dayString = "Tuesday"
elif day == 2:
    dayString = "Wednesday"
elif day == 3:
    dayString = "Thursday"
elif day == 4:
    dayString = "Friday"
elif day == 5:
    dayString = "Saturday"
elif day == 6:
    dayString = "Sunday"

window = tk.Tk()
window.title('Spring 2020 Course Launcher')

todayLstring = "Welcome!\nToday is " + dayString + ", " + datetime.date.today().strftime("%B %d, %Y")
todayL = tk.Label(text=todayLstring, font=hdr, background="white")
todayL.pack(fill=tk.X) 



if day == 0:
    Monday = tk.Frame(master=window, borderwidth=10, relief=tk.GROOVE, background="white")
else:
    Monday = tk.Frame(master=window, borderwidth=10, background="white")

Monday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

if day == 1:
    Tuesday = tk.Frame(master=window, borderwidth=10, relief=tk.GROOVE, background="white")
else:
    Tuesday = tk.Frame(master=window, borderwidth=10, background="white")

Tuesday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

if day == 2:
    Wednesday = tk.Frame(master=window, borderwidth=10, relief=tk.GROOVE, background="white")
else:
    Wednesday = tk.Frame(master=window, borderwidth=10, background="white")

Wednesday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

if day == 3:
    Thursday = tk.Frame(master=window, borderwidth=10, relief=tk.GROOVE, background="white")
else:
    Thursday = tk.Frame(master=window, borderwidth=10, background="white")

Thursday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

if day == 4:
    Friday = tk.Frame(master=window, borderwidth=10, relief=tk.GROOVE, background="white")
else:
    Friday = tk.Frame(master=window, borderwidth=10, background="white")

Friday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Mon = tk.Label(master=Monday, text="Monday", font=dayHdr, background="white")
Mon.pack()

Tue = tk.Label(master=Tuesday, text="Tuesday", font=dayHdr, background="white")
Tue.pack()

Wed = tk.Label(master=Wednesday, text="Wednesday", font=dayHdr, background="white")
Wed.pack()

Thu = tk.Label(master=Thursday, text="Thursday", font=dayHdr, background="white")
Thu.pack()

Fri = tk.Label(master=Friday, text="Friday", font=dayHdr, background="white")
Fri.pack()

# Defined Methods
# For zoom meetings, paste the meeting ID in confno and password (if applicable) in the password spot
# I don't think it matters whether you use the numerical/letter password or the long encrypted one
# This should also start a Zoom meeting without the web browser opening - it should connect and open Zoom
# I've found it useful to use the https:// to precede the link - without that, mine opened in Internet Explorer,
#   but with that, it opens in my default browser.
# The print statements are also not really necessary, except for testing purposes


def cs4121r01():
    print("CS4121 R01: Programming Languages")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

def cs4821r01():
    print("CS4821 R01: Data Mining")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

def sat3310r01():
    print("SAT3310 R01: Scripting Admin & Automation (Class)")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

def cs4321r01():
    print("CS4321 R01: Introduction to Algorithms")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

def hu3015r03():
    print("HU3015 R03: Advanced Composition")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

def sat3310l02():
    print("SAT3310 R01: Scripting Admin & Automation (Lab)")
    webbrowser.open('zoommtg://michigantech.zoom.us/join?action=join&confno=MEETING_NUMBER_GOES_HERE&pwd=PASSWORD_GOES_HERE')
    webbrowser.open('https://maps.google.com')
    sys.exit()

# Add Buttons
# There may be a better way to do this, but I found that this worked for making modifications when necessary
# (i.e. some classes synchronous, some asynchronous on different days).
# Please customize to fit your schedule.
# Monday

CS4121M = tk.Button(master=Monday, text="CS 4121 R01\nProgramming Languages\n9:00 am - 9:50 am", borderwidth=5, command=cs4121r01, font=btnTxt, background="green", activebackground="gray", fg="white")
CS4121M.pack(fill=tk.X)

spacerM = tk.Label(master=Monday, text="", borderwidth=0, font=btnTxt, background="white")
spacerM.pack()

CS4821M = tk.Button(master=Monday, text="CS 4821 R01\nData Mining\n11:00 am - 11:50 am", borderwidth=5, command=cs4821r01, font=btnTxt, background="orange", activebackground="gray")
CS4821M.pack(fill=tk.X)

spacerM2 = tk.Label(master=Monday, text="", borderwidth=0, font=btnTxt, background="white")
spacerM2.pack()

SAT3310M = tk.Button(master=Monday, text="SAT 3310 R01\nScripting Admin & Automation\n1:00 pm - 1:50 pm", borderwidth=5, command=sat3310r01, font=btnTxt, background="purple", activebackground="gray", fg="white")
SAT3310M.pack(fill=tk.X)

# Tuesday

CS4321T = tk.Button(master=Tuesday, text="CS 4321 R01\nIntroduction to Algorithms\n9:30 am - 10:45 am", borderwidth=5, command=cs4321r01, font=btnTxt, background="blue", activebackground="gray", fg="white")
CS4321T.pack(fill=tk.X)

spacerT = tk.Label(master=Tuesday, text="", borderwidth=0, font=btnTxt, background="white")
spacerT.pack()

HU3015T = tk.Button(master=Tuesday, text="HU 3015 R03\nAdvanced Composition\n11:00 am - 12:15 pm", borderwidth=5, command=hu3015r03, font=btnTxt, background="red", activebackground="gray")
HU3015T.pack(fill=tk.X)

# Wednesday
CS4121W = tk.Button(master=Wednesday, text="CS 4121 R01\nProgramming Languages\n9:00 am - 9:50 am", borderwidth=5, command=cs4121r01, font=btnTxt, background="green", activebackground="gray", fg="white")
CS4121W.pack(fill=tk.X)

spacerW = tk.Label(master=Wednesday, text="", borderwidth=0, font=btnTxt, background="white")
spacerW.pack()

CS4821W = tk.Button(master=Wednesday, text="CS 4821 R01\nData Mining\n11:00 am - 11:50 am", borderwidth=5, command=cs4821r01, font=btnTxt, background="orange", activebackground="gray")
CS4821W.pack(fill=tk.X)

spacerW2 = tk.Label(master=Wednesday, text="", borderwidth=0, font=btnTxt, background="white")
spacerW2.pack()

SAT3310W = tk.Button(master=Wednesday, text="SAT 3310 R01\nScripting Admin & Automation\n1:00 pm - 1:50 pm", borderwidth=5, command=sat3310r01, font=btnTxt, background="purple", activebackground="gray", fg="white")
SAT3310W.pack(fill=tk.X)

# Thursday
CS4321R = tk.Button(master=Thursday, text="CS 4321 R01\nIntroduction to Algorithms\n9:30 am - 10:45 am", borderwidth=5, command=cs4321r01, font=btnTxt, background="blue", activebackground="gray", fg="white")
CS4321R.pack(fill=tk.X)

spacerR = tk.Label(master=Thursday, text="", borderwidth=0, font=btnTxt, background="white")
spacerR.pack()

HU3015R = tk.Button(master=Thursday, text="HU 3015 R03\nAdvanced Composition\n11:00 am - 12:15 pm", borderwidth=5, command=hu3015r03, font=btnTxt, background="red", activebackground="gray")
HU3015R.pack(fill=tk.X)

# Friday
CS4121F = tk.Button(master=Friday, text="CS 4121 R01\nProgramming Languages\n9:00 am - 9:50 am", borderwidth=5, command=cs4121r01, font=btnTxt, background="green", activebackground="gray", fg="white")
CS4121F.pack(fill=tk.X)

spacerF = tk.Label(master=Friday, text="", borderwidth=0, font=btnTxt, background="white")
spacerF.pack()

CS4821F = tk.Button(master=Friday, text="CS 4821 R01\nData Mining\n11:00 am - 11:50 am", borderwidth=5, command=cs4821r01, font=btnTxt, background="orange", activebackground="gray")
CS4821F.pack(fill=tk.X)

spacerF2 = tk.Label(master=Friday, text="", borderwidth=0, font=btnTxt, background="white")
spacerF2.pack()

SAT3310F = tk.Button(master=Friday, text="SAT 3310 L02\nScripting Admin & Automation\n12:00 pm - 1:50 pm", borderwidth=5, command=sat3310l02, font=btnTxt, background="purple", activebackground="gray", fg="white")
SAT3310F.pack(fill=tk.X)


window.mainloop()





