from sys import argv
from os.path import exists

script, file1, file2 = argv

indata = open(file1).read()

print "This will copy %r to %r." % (file1, file2)
print "The length of %r is %r bytes." % (file1, len(indata))
print "Does %r exist? %r\n" % (file2, exists(file2))

print "This will overwrite %r. Hit ENTER to continue" % file2
raw_input()

outdata = open(file2, 'w')
outdata.write(indata)

print "All done!"

outdata.close()
