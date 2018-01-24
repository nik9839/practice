package google;

public class Assignment {

	static char[] str;
	static boolean flag= false;
	static void recurr(int sIndex,int eIndex, int count){
	
		if(sIndex>=eIndex)
			return;
		boolean x= Character.isDigit(str[sIndex]);
		boolean y= Character.isDigit(str[eIndex]);
		if(x && y){
			if((Integer.parseInt(String.valueOf(str[sIndex]))+Integer.parseInt(String.valueOf(str[eIndex]))==10)){
				if(count!=3)
				{
					flag =false;
					return;
				}
				else
					flag=true;
			}
			else{
				recurr(sIndex+1,eIndex,count);
				recurr(sIndex,eIndex-1,count);
			}
		}
		else if(x== true && y== false){
			if(str[eIndex]=='?')
				count--;
			recurr(sIndex,eIndex-1,count);
		}
		else if(x== false && y== true){
			if(str[sIndex]=='?')
				count--;
			recurr(sIndex+1,eIndex,count);
		}
		else {
			if(str[sIndex]=='?')
				count--;
			if(str[eIndex]=='?')
				count--;
			recurr(sIndex+1,eIndex-1,count);
		}
	}
	
	public static void main(String [] args){
		String abc="arrb6???4xxbl5???eee5";
		str=abc.toCharArray();
		int temp=0;
		for(int i=0;i<str.length;i++){
			if(str[i]=='?')
				temp++;
		}
		recurr(0,str.length-1,temp);	
		if(flag==true)
			System.out.println("true");
		else
			System.out.println("false");
	}
}
