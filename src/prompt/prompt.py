def prompt():
    from src.data.dataRunner import getUserData, buildData
    from src.prompt.inputCases import mainCase
    import colorama
    import sys

    print("Maverick 0.0.3")

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

        user_input = input("#> ")

        mainCase(user_input,programs)