def prompt():
    from src.data.dataRunner import getUserData, buildData, passwordProtectedCheck
    from src.prompt.inputCases import mainCase
    from root.programs.Maverick.colorScheme import maverickScheme
    import colorama
    import sys

    print("Maverick 0.0.2 Revised")

    # set up user data

    buildData() # check if this is the user's first time.

    userdata = getUserData() # get the userdata

    programs = userdata["programs"] # grab programs

    userdata.close() # close the database

    colorama.init() # init colorama for all system files

    sys.path.append("../Maverick") # make path include all directories

    #

    print()

    while True:

        if passwordProtectedCheck():

            maverickScheme.color("#> ","")

            user_input = input()

        else:

            maverickScheme.color("$> ","")

            user_input = input()

        mainCase(user_input,programs)