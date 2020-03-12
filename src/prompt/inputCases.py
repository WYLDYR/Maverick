class ArgChain:
    def __init__(self, args):

        args = args.split(" ") # Split agruments into list

        self.mainArg = args[0] # Get main argument (file name)
        self.params = args # Assigns all other arguments to "params"

        self.params.remove(args[0]) #Remove main argument

class ProgramID:

    def __init__(self,id,path):
        self.id = id
        self.path = path

    def run(self,args):

        import os
        import platform

        argString = "" # Create string to hold arguments

        for arg in args:
            argString += arg + " " # Add arguments to argument holder

        if platform.system() == "Linux" or platform.system() == "Darwin": # Check OS
            os.system("python3 {} {}".format(self.path, argString)) # Python call for Darwin or Linux
        elif platform.system() == "Windows":
            os.system("py {} {}".format(self.path, argString)) # Python call for Windows
        else:
            print("Unknown platform.")

def mainCase(inp,programs):

    import colorama
    import os
    import platform

    inp = ArgChain(inp)

    if inp.mainArg == "exit": # Basic exit case
        print(colorama.Fore.RED + "Exiting..." + colorama.Style.RESET_ALL)
        exit()

    if inp.mainArg == "clear":
        if platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            print("Unknown platform.")

    # movement commands

    if inp.mainArg in ["ls","cd","pwd"]:
        pass

    for program in programs: # Iterate programs

        assert isinstance(program, ProgramID) # Assure program is an ID

        if inp.mainArg == program.id:

            program.run(inp.params) # Execute program