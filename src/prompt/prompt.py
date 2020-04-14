def prompt():
    from src.data.dataRunner import getUserData, buildData, passwordProtectedCheck
    from src.prompt.inputCases import mainCase
    from root.programs.Maverick.colorScheme import maverickScheme
    import colorama
    import sys

    print("Maverick 0.0.3")

    # set up user data

    buildData() # check if this is the user's first time.

    userdata = getUserData(); programs = userdata["programs"]; userdata.close()

    colorama.init() # init colorama for all system files

    sys.path.append(".") # make path include all directories, I think this is only temporary.

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