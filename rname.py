import os

# Getting Files From Directory
files = os.listdir(".")
# Creating Temp File
with open("Mass-Rename-Temp.txt", "w") as f:
    for file in files:
        f.write(file + "\n")
time = os.path.getmtime('Mass-Rename-Temp.txt') # Getting Temp File's Modified Time
with open("Mass-Rename-Temp.txt", "r") as f: # Opening The Temp File In Reading Mode
    while True:
        if (time < os.path.getmtime("Mass-Rename-Temp.txt")): # If The File Changed
            for line in zip(f.read().split("\n"), files): # Loop Over The Changed File And The Original File Names
                os.rename(line[1], line[0]) # Rename Files
            break

os.remove("Mass-Rename-Temp.txt") # Removing The Temp File

