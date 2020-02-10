import shelve
import colorama
from root.programs.Installer.install import install

def getUserData():

    return shelve.open("./src/data/data", writeback = True)

def buildData():

    userdata = getUserData()

    # wacky lil test to see if account is made

    try:
        userdata["buildTest"]
    except:

        print()
        print("Welcome to Maverick OS.")
        print("Running one-time setup...")

        userdata["programs"] = []
        userdata["password"] = None
        userdata["buildTest"] = True

        userdata.close()

        install("apps","./root/programs/apps.py")
        install("psswd","./root/programs/psswd.py")
        install("install","./root/programs/installer.py")
        install("help","./root/programs/info.py")
