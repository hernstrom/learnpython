from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'r')

print "I'm going to read the file."

contents = target.read()
print "The file contains:"
print "%s" % contents

print "And finally, we close it."
target.close()