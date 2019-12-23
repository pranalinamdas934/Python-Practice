from sys import argv
from os.path import exists

script, source, dest = argv

print('Going to copy contents from {} to {} '.format(source, dest))

sfile = open(source)
sdata = sfile.read()

print('input file is {} bytes long'.format(len(sdata)))
print('checking if destination file is exists or not: ', exists(dest))
print('Ready, press ENTER to continue or CTRL+C to cancel')
input()

print('opening {} file fot writing'.format(dest))
dfile = open(dest, 'a+')
print('writing data')
dfile.write(sdata)
print('completed writing')
sfile.close()
dfile.close()
