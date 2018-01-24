function QuestionsMarks(str){

  let pairFound=0;
  for(let i=0;i<str.length-1;i++)
	{
    if(isNaN(str[i]))
      {
        continue;
      }
    let count=0;
     for(let j= i+1;j<str.length;j++)
       {
         if(str[j]==='?'){
           count++;
         }
         else if(!isNaN(str[j])){
            if((Number(str[i])+Number(str[j]))===10){
           		if(count!==3)
             			return 'false';
              else
                pairFound++;
         		}
          }   
       }
  }
  if(pairFound>0)
    return 'true';
  else
    return 'false';
}

console.log(QuestionsMarks("acc?7??sss?3rr1??????5"));
