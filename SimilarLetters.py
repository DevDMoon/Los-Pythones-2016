import fileinput



Numbers = "jdo394 dworj3 tos49a ko39j2"

Numbers = Numbers.split()
Num = list(Numbers[0])
Result = []
Final = []

for i in range(1,len(Numbers),1):
	
	NumToSearch = list(Numbers[i])
	print ("LIST TO COMPARE:" + str(Num))
	print ("MATCH" + str(NumToSearch))

	
	for e in range(0,len(NumToSearch)):
		for a in range(0,len(NumToSearch)):
			
			if Num[a] == NumToSearch[e]:
				Result.append(NumToSearch[e])

	


for p in range(0,len(Result)):
	for a in range(0,len(Result)):
		if Result[p] != Final[a]:
			print(Result[p])
			Final.append[Result[p]]

print ("FINAL RESULT: " + str(Final))

