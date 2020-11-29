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
        os.listdir(moveFolder)
    except FileNotFoundError:
        # create root folder
        os.system("mkdir %s%s" % (settings.homeDirectory, settings.moveTo))
        # creating folders
        for folderName in settings.fileTypes:
            os.system("mkdir %s%s%s/" % (settings.homeDirectory, settings.moveTo, folderName))
            


# define file type
def defineFolder(typeFile):

    # start loop for looking files in database
    for fType in settings.fileTypes:

        # initiate folder name 
        folderName = "other"

        # start logick
        if typeFile in settings.fileTypes[fType]:
            folderName = fType
            break

    # return folder name
    return folderName

# define all specsymbols
def defineSpace(filePath):

    # define new file path
    newFilePath = ""

    # check all symbols
    for item in filePath:

        # if space add \
        if item == " " or item == "(" or item == ")":
            newFilePath += "\\"
        
        # add current symb
        newFilePath += item
    
    # return string
    return newFilePath

# 
# Variables
# 

# patch to downloads folder
downloadFolder = settings.homeDirectory + settings.downloadFolderName

# patch to move
moveFolder = settings.homeDirectory + settings.moveTo

# dict with folder pathes
folders = {
    "docs": downloadFolder + "docs/",
    "images": downloadFolder + "images/",
    "music": downloadFolder + "musics/",
    "app": downloadFolder + "apps/",
    "archiv": downloadFolder + "archives/",
    "torrent": downloadFolder + "torrents/",
    "other": downloadFolder + "others/"
}

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

    # make comand to terminal
    command = "mv %s %s" % (downloadFolder + defineSpace(item) , moveFolder + folderForFile)

    # print command
    print("%s moved to %s" % (item, folderForFile))

    # move file
    os.system(command)
