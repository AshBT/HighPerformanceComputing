s = 1
x = 4

for x in range(6):

	print "Before iteration %s, s = %s" % (k, s)
	s = 0.5 * (s * x/s)

print "After %s iterations, s = %s" % (s)

