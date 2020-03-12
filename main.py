import src.prompt.prompt as prompt
import platform

if int(platform.python_version().split(".")[0]) <= 3: # Check Python version
    prompt.prompt()
else:
    print("Release is not Python 3 or greater.")