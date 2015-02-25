score = raw_input("Enter score: ")
po = float(score)

if po > 1.0:
    print "Error"
	#break
if po >= 0.0 and po <= 1.0:
    if po >= 0.9:
        print "A"				
    elif po >= 0.8:
        print "B"
    elif po >= 0.7:
        print "C"
    elif po >= 0.6:
        print "D"
    elif po < 0.6:
        print "F"	
		   