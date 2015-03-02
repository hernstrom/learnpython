from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)

# we could do in one line, how?
#in_file = open (from_file); indata = in_file.read()
indata = open (from_file).read()
#indata = 

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Done."

out_file.close()
#in_file.close()