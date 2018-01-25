ans='the string not found.';

def matrixRow(row,col,strArr):
    global ans
    if(col+1<len(strArr[0])):
        a = strArr[row][col] in ('a', 'e', 'i', 'o', 'u')
        b = strArr[row][col+1] in ('a', 'e', 'i', 'o', 'u')
        c = strArr[row+1][col] in ('a', 'e', 'i', 'o', 'u')
        d = strArr[row+1][col+1] in ('a', 'e', 'i', 'o', 'u')

        if(a and b and c and d):
           ans= str(row)+'-'+str(col)
           return
        else:
            if(b==False or d==False):
                matrixRow(row,col+2,strArr);
            else:
                matrix(row,col+1,strArr)
            

               
def VowelSquare(strArr):
    for i in range(len(strArr)-1):
        matrixRow(i,0,strArr)
        if(ans!='the string not found.'):
            break

#inputMatrix =[['a','q','r','s','t'],['u','k','a','e','i'],['f','f','o','o','o']];
#inputMatrix = [['g','g'],['f','f']]
inputMatrix =[['a','b','c','d'],['e','i','k','r'],['o','u','f','j']];
VowelSquare(inputMatrix)
print (ans)
