#
# import libs
# 
import os, settings

#
# Functions
#

# create folders
def createFolders():
    # check for folder
    try:
        # check for folder
        os.listdir(moveFolder)
    except FileNotFoundError:
        # create root folder
        os.system("mkdir %s/%s" % (settings.homeDirectory, settings.moveTo))
            
# define file type
def defineFolder(typeFile):

    # initiate folder name 
    folderName = "other"

    # start loop for looking files in database
    for fType in settings.fileTypes:

        # start logick
        if typeFile in settings.fileTypes[fType]:
            folderName = fType
            break

    # return folder name
    return folderName

# define all specsymbols
def defineSpace(filePath):
    # define symbols for backslash
    symbols = [" ","(",")",","]

    # define new file path
    newFilePath = "/"

    # check all symbols
    for item in filePath:

        # if space add \
        if item in symbols:
            newFilePath += "\\"
        
        # add current symb
        newFilePath += item
    
    # return string
    return newFilePath

# 
# Variables
# 

# patch to downloads folder
downloadFolder = "%s/%s" % (settings.homeDirectory, settings.downloadFolderName)

# patch to move
moveFolder = "%s/%s/" % (settings.homeDirectory, settings.moveTo)

# 
# Start app
# 

# check and creating folders for moving
createFolders()

# get all files in directory
dirs = os.listdir(downloadFolder)

# start loop for moving
for item in dirs:

    # make array with name and type
    nameArr = item.split(".")

    # to lower case file type
    typeName = nameArr[len(nameArr) - 1].lower()

    # folder for file
    folderForFile = defineFolder(typeName)

    # check folder
    try:
        os.listdir(moveFolder + folderForFile)
    except FileNotFoundError:
        os.system("mkdir %s%s" % (moveFolder, folderForFile))

    # make comand to terminal
    command = "mv %s %s" % (downloadFolder + defineSpace(item) , moveFolder + folderForFile)

    # print command
    print("%s moved to %s" % (item, folderForFile))
    
    # print command for debugging
    # print(command)

    # move file
    os.system(command)
