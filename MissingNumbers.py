import fileinput



# NumRows[] = fileinput.filelineno()
# RenglonInicial = NumRows[0];



with open('PracticeInput.txt', 'r') as myfile:


    Inputxt = myfile.readline()
    Inputxt = int(Inputxt)
    for i in range(0,Inputxt):
    	Numbers = myfile.readline().split()
    	

    	Numbers = list(map(int, Numbers))
    	Numbers.sort()
    	print (Numbers)
    	leng = len(Numbers)
    	

    	Dif = Numbers[1] - Numbers[0]
    	print (Dif)
    	Total = []
    	Result = []
    	for RCount in range(0,Numbers[leng - 1],Dif):
    		Total.append(RCount)
    	
 
    	for e in range(0,len(Total) - 1,Dif):
    		if Total[e] != Numbers[e]:
    			Result.append(e)
    			Numbers.append(e)
    			Numbers.sort()

    	print (Result)
    	
    	#Result = sum(xrange(a[0],a[-1]+1)) - sum(a)



