import zipfile
import sys
import threading

def unzip(file,word): ##Function which receives the file to crack
					  ### and the wordlist
	try:
	
		zfile=zipfile.ZipFile(file)
		
		f=open(word,"r")
		
		for line in f.readlines():
		
			word1=line.strip("\n")
			
		zfile.extractall(pwd=word1)
		
		
		print"Attempting to crack Password..."
			
		if zfile:
			
			print"\nPassword Cracked = "+ word1
			
			
										
	except:
	
		print"Password Could not be cracked "

		exit(1)
		
		
def main():

	if len(sys.argv)==3:
	
		file=sys.argv[1]
		wordlist=sys.argv[2]
		unzip(file,wordlist)
		
		t=threading.Thread(target=unzip,args=(file,wordlist))
		t.start()
		
main()

		