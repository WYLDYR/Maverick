import sys

sys.path += "../../"

from colorama import init, Fore, Back, Style
from src.data.dataRunner import getUserData
import platform

# windows coloring
if platform.system() == "Windows":
    init(convert = True)

data = getUserData()

def showPrograms(data):

    for program in data["programs"]:
        print(
            Fore.BLUE +
            "[{}]: {}".format(program.path, program.id) +
            Style.RESET_ALL
        )

if __name__ == "__main__":
    print(Fore.RED + Back.WHITE + "APPS MANAGER" + Style.RESET_ALL)
    print(Fore.GREEN + "We are aware of the [Segmentation fault (core dumped)] error. THIS WILL BE FIXED SOON!")
    showPrograms(data)
