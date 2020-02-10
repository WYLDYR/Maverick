import sys

sys.path += "../../Maverick"

from src.data.dataRunner import getUserData
from root.programs.Installer.install import install

if __name__ == "__main__":

    if len(sys.argv) == 3:

        # three args met

        path = sys.argv[2]
        id = sys.argv[1]

        install(id,path)

        print("Restart your system to use the new program.")
