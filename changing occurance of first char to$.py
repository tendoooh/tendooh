'''
this program changes a given string to a new string where the
first and last chars have been exchanged
'''
def front_back(string):
	if len(string)==1:
		return string
	return string[-1] + string[1:-1] + string [0]

print “hey you”

front_back(‘hey you’)
