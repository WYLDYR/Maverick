import sys

sys.path += "../../Maverick"

from src.data.dataRunner import getUserData
from root.programs.Installer.install import install

if __name__ == "__main__":

    if sys.argv[1] in ["-help","-h","--help","--h"]:

        print("EX: install name /root/path")

    else:

        path = input("Input desired path: ")
        id = input("Input desired alias: ")

        install(id, path)

        print("Restart your system to use the new program.")