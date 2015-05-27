import sys

if len(sys.argv) != 2:
	print "usage: python expertSystem.py [file].exp"
	sys.exit(0)
if (sys.argv[1].find(".exp") != len(sys.argv[1]) - 4):
	print "file: " + sys.argv[1] + " not found"
f = open(sys.argv[1])
for line in f:
			print line,
