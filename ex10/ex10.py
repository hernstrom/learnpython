tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# extra
print "\n\n"
print "now you see me"
print "now you don't\b\b\b\b\b\b\b\b\b\b\b\b\b        "

print '''
What is the difference?
I do not know.
I guess I can """ and no one will know.
'''


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s %s %s %s %s %s\r" % (i,i,i,i,i,i),