#include<stdio.h>
int main(void)
{
	int s,p,r,q,a1,a2,t,n0,n1;
	scanf("%d%d",&s,&p);
	scanf("%d%d",&r,&q);
	a1=s*60+p;
	a2=r*60+q;
	if(a1>a2)
	{
		t=a1-a2;
		n0=t/60;
		n1=t%60;
		printf("%d %d",n0,n1);
	}
	else
	{
		t=a2-a1;
		n0=t/60;
		n1=t%60;
		printf("%d %d",n0,n1);
	}
}	
