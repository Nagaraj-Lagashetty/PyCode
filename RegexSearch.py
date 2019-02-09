#Regex search thru multiple text files
import re
import os
print(os.getcwd())
os.chdir(input('Enter directory in which you search files for pattern\n'))
#'c:\\users\\user\\desktop\\pylife\\filehandling'  = path
print(os.getcwd())
files = os.listdir()
word = input('Enter the word you want search\n')
for i in files :
    f = open(os.path.join(os.getcwd(),i),'r+')
    #g = re.search(input(),f.read())
    #g = re.findall(r'\d\d\d\d\d\d\d\d\d\d',f.read())
    #g = re.findall(word,f.read())
    g = re.sub(word,'Hello',f.read())
    #f.seek(0)
    f.write(g)
    print('{} - {}'.format(i,g))
    f.close()
