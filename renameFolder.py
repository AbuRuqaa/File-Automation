import re,os
from pathlib import Path as path

''' How to use this script:
	You give it a path for the folders list that you want to rename and it will rename the folders as the 
	And What the regex does: if you want to rename a file with a specific name

	 '''



def renameFolder(Path,regex,fileName):

	FoldersList=os.listdir(Path)

	for i in FoldersList:
			
		FolderPath=Path+f'/{i}'
		
		try:
			RegexFind=regex.search(FolderPath).group()
		except:
			break
		startPath=Path+f'/{i}'#Get the full path for the folder we want to rename
		replaceCh=RegexFind.replace('chapter','',1)#Replace chapter to get only the number
		
		desPath=f"{Path}\\{fileName}"#The new name
		
		if RegexFind:
			print(f'\nRenaming {FolderPath} to {desPath} ...\n')
			#os.rename(startPath,desPath) Uncomment this after make sure everything is as you want

	print('Arigato Gozaimashita...')
	print('Done...')

		


fileRegex=re.compile(r'your regex')#your regex here 
fileName=input("\nEnter the new name of your folders:\n")
renameFolder('Your folders  list path',fileRegex,fileName)