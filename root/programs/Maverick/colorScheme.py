import colorama

class Scheme:
    def __init__(self, color):
        self.mainColor = color
    def color(self, string,end="\""):
        print(self.mainColor + string + colorama.Style.RESET_ALL,end=end)

maverickScheme = Scheme(colorama.Fore.RED)