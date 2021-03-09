#!/usr/bin/python3

#
# import libs
# 
import os, settings

#
# Functions
#

# function for check folder 
def folderIsCreated(pathToFolder, folderName):
    # catch errors
    try:
        # checking
        os.listdir("%s/%s" % (pathToFolder, folderName))
    except FileNotFoundError:
        # create folder
        os.system("mkdir %s/%s" % (pathToFolder, folderName))


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

# 
# Variables
# 

# patch to downloads folder
downloadFolder = "%s/%s" % (settings.homeDirectory, settings.downloadFolderName)

# patch to target folder
targetFolder = "%s/%s" % (settings.homeDirectory, settings.moveTo)

# 
# Start app
# 

# check for target folder
folderIsCreated(settings.homeDirectory, settings.moveTo)

# get all files in directory
files = os.listdir(downloadFolder)

# start loop for moving
for fileName in files:

    # make array with name and type
    nameArr = fileName.split(".")

    # to lower case file type
    typeName = nameArr[len(nameArr) - 1].lower()

    # folder for file
    folderForFile = defineFolder(typeName)

    # check folder availability
    folderIsCreated(targetFolder, folderForFile)

    # make comand to terminal
    command = "mv '%s/%s' '%s/%s'" % (downloadFolder, fileName, targetFolder, folderForFile)

    # print command
    print("moving %s to %s" % (fileName, folderForFile))

    # move file
    os.system(command)
