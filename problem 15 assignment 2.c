/* PROBLEM 15 ASSIGNMENT 2
SOLVING 1ST ORDER ODE WITH EULER METHOD
NAME: SAGAR DAM;  DNAP*/

#include <stdio.h>
#include <math.h>
//#include <conio.h>
float f(float t,float y);
float ftrue(float t);

//main function
int main()
{
    int a=0,b=2,n,i;
    float h=0.2,v;
    n=(b-a)/h;
    float t[n],y[n];
    t[0]=a;
    y[0]=0.5;
    
    for(i=0; i<=n; i++)
    {
        t[i+1]=t[i]+h;  // set mesh points
        //printf("%f",t[i]);
    }
    
    printf("# solving the differential eqn y'(t)=y-t^2+1 from t=0 to 2 with h=0.2\n");
    printf("# Boundary condition: y(0)=0.5\n");
    printf("# Showing the result and absolute error in tabular form...\n\n");
    printf("t[i]\t    ysol\t     ytrue\t    absolute error\n");
    for(i=0; i<=n; i++)
    {
        y[i+1]=y[i]+h*f(t[i],y[i]);// solving by euler method
        v=(y[i]-ftrue(t[i]));// calculating error
        if(v>=0)
        {
            printf("%f\t%f\t%f\t%f\n",t[i],y[i],ftrue(t[i]),v);
        }
        else
        {
            printf("%f\t%f\t%f\t%f\n",t[i],y[i],ftrue(t[i]),v);
            
        }
    }
    return 0;
}

//defining dy/dt=f(t,y)
float f(float t, float y)
{
    float z;
    z=y-t*t+1;
    return(z);
}

//defining true solution:
float ftrue(float t)
{
    float ztrue;
    ztrue= (t+1)*(t+1)-exp(t);
    return(ztrue);
}
    ztrue= (t+1)*(t+1)-0.5*exp(t);
    return(ztrue);
}
