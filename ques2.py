def matrix(row,col,strArr):
	if(row+1<len(strArr) and col+1<len(strArr[0])):
		a = strArr[row][col] in ('a', 'e', 'i', 'o', 'u')
		b = strArr[row][col+1] in ('a', 'e', 'i', 'o', 'u')
		c = strArr[row+1][col] in ('a', 'e', 'i', 'o', 'u')
		d = strArr[row]+1[col+1] in ('a', 'e', 'i', 'o', 'u')

		if(a and b and c and d)
			return str(row)+'-'+str(col)
		else:
			if(b==False or d==False):
				matrix(row,col+2,strArr);
			else:
				matrix(row,col+1,strArr)
			matrix(row+1,col,strArr)

		return 'the string not found'        
def VowelSquare(strArr):
	matrix(0,0,strArr);
