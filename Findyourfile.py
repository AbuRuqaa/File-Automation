#This project find any png file and put it in a specific folder

import os, shutil, re
from pathlib import Path as path
import pyinputplus as pypi
''' How this script work:
    
    1-First you choose the tree that you want to search for your file in
    2-It will copy it to another folder
    3-Then It will give you the option to rename the file 
    Note:You have to put a regex for the file you are searching I put it as pdf|jpg so if you want to find another find put the name of it'''

def move(folder,fileRegex,Destinsion,response):
    folder=os.path.abspath(folder)
    Destinsion=path(Destinsion)#The folder which will the files will be copied in.
    
    #Copy the files to another folder first.
    for folders,subfolders,files in os.walk(folder):#walk through all folder,subfolders,files in the given dir
        for file in files:#Walk through every file in files list
            file=path(folders)/file#Get the full path for the file
            #print(file)
            fileBaseName=os.path.basename(file)
            des=Destinsion/fileBaseName
            if not os.path.exists(file):
                continue
            try:
                mo=fileRegex.search(str(file)).group()
            except:
                continue
            
            print(f"\nCopying {file} to {des}\n")
            shutil.copy(file,f"{des}")#uncomment this after check


    



def rename(treeWalk):
    folWalk=os.listdir(path(treeWalk))
    newName=input("What you want the new name of your files (We will add a number for each one e.x:file(1),file(2)....):\n")
    x=1
    for i in folWalk:#Renameing files
        Destinsion=treeWalk
        fullPath=Destinsion/i
        fileType=fullPath.suffix#get the file extension
        fileNewname=Destinsion/f'{newName}({x}){fileType}'
        if os.path.exists(fileNewname):
            while True:
                fileNewname=Destinsion/f'{newName}({x}){fileType}'
                x+=1
                if not os.path.exists(fileNewname):
                    break
        x+=1
        print(f'\nRenameing  {i} to {newName}({x})\n')
        os.rename(fullPath,fileNewname)#uncomment this after check








while True:
    
    folderPath=input("\nThe path for the folders tree that you want to search your files in:\n")
    folderPath=path(folderPath)
    
    if folderPath:
         break
   



while True:
    try:
        direction=input("\nThe path for the new folder:\n")
        new_file_direction=path(direction)
        if not new_file_direction==None:
            break

    except:
        print("\nMake sure you entered the right path\n")
        continue

fileRegex=re.compile(r'.*\.png|jpg')#Put the extension/name of your files

move(folderPath,fileRegex,new_file_direction,response)

response=response = pypi.inputChoice(['no', 'yes'],prompt="\nDo you want to rename your files?(answer with yes/no)\n")

if response=="yes":
    rename(new_file_direction)

