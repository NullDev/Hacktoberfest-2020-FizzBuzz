PROC IML;

/* 
To be able to use a Table, the usual values are replaced as follows:

Fizz = 300
Buzz = 500
FizzBuzz = 800 

*/

start fizzbuzz(n);
if mod(n,3)=0 then
	if mod(n,5)=0 then out=800;
	else out=300;
else 
	if mod(n,5)=0 then out=500;
	else out=n;
return out;
finish fizzbuzz;

i = 1;
n=100;

T=j(1,2);
a = fizzbuzz(i);
T[1,1]=i;
T[1,2]=a;
i = i+1;

do while (i<=n);
a=fizzbuzz(i);
Temp=j(1,2);
Temp[1,1]=i;
Temp[1,2]=a;
T=insert(T, temp, i);
i = i+1;
end;

names={"Value" "Evaluation"};
tbl_fb=TableCreate(names, T);

call TablePrint(tbl_fb) label="Evaluating the first 100 integers using FizzBuzz"
							 firstobs=1 numobs=i
							 var=names
							 ID="Value";
	
	
	
/* Graph the values as obtained above to see where all the multiples lie */
x = T[,1];
y = T[,2];
title "The function f(x) on the initial interval";
call Series(x,y) grid={X Y} xvalues=1:100 other="refline 300 500 800 / axis=y";
