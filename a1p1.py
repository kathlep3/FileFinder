from pathlib import Path
import sys


def printDirectories(directory):
    myPath = Path(directory)
    print(myPath)
    for currentPath in myPath.iterdir():
        print(currentPath)# currentPath is either a directory or a file, test it
        if currentPath.is_file():
            print(currentPath)
        elif currentPath.is_dir():
            printDirectories(currentPath)


def outputFiles(directory):
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        print(currentPath)
        if currentPath.is_file():
            print(currentPath)


def searchFile(directory, inputt):
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        print(currentPath)
        if currentPath.is_file():
            print(currentPath)
    

def outputFileExtension(directory, inputt):
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        print(currentPath)
        if currentPath.is_file(): 
            print(currentPath)


if __name__ == "__main__":
    command = sys.argv[1]

    if command == "Q" or command == "L":
        if command == "Q":
            sys.exit("Exited.")
        elif command == "L":
            directory = sys.argv[2] 
            for arg in sys.argv[3:]:
                if arg == "-r":
                    printDirectories(directory)
                elif arg == "-f":
                    outputFiles(directory)
                elif arg == "-s":
                    searchFile()
                elif arg == "-e":
                    outputFileExtension()
