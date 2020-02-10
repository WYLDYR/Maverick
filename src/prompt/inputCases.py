class ArgChain:
    def __init__(self, args):
        args = args.split(" ")

        self.mainArg = args[0]
        self.params = args

        self.params.remove(args[0])

class ProgramID:
    def __init__(self,id,path):
        self.id = id
        self.path = path

    def run(self,args):
        import os
        import platform

        argString = ""

        for arg in args:
            argString += arg + " "

        if platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("python3 {} {}".format(self.path, argString))
        else:
            os.system("py {} {}".format(self.path, argString))

def mainCase(inp,programs):
    import colorama

    inp = ArgChain(inp)

    if inp.mainArg == "exit":
        print(colorama.Fore.RED + "Exiting..." + colorama.Style.RESET_ALL)
        exit()

    # movement commands

    if inp.mainArg == "ls":
        pass
    if inp.mainArg == "cd":
        pass
    if inp.mainArg == "pwd":
        pass

    for program in programs:

        assert isinstance(program, ProgramID)

        if inp.mainArg == program.id:

            program.run(inp.params)