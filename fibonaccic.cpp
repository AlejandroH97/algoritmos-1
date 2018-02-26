#include <iostream>
#include <cstdlib>
using namespace std;

 int fibo2(int n){  //empieza a mandar overflow despues de fibonacci de 46
        if(n==0){
            return 0;
        }
       int a=0;
        int b = 1;
        for(int i = 1;i<n;i++ ){
            b=	(a+b);
            a=(b-a);
            
                    
        }
        return b;        
    }
    short fibo3(short n){//empieza a mandar overflow despues de fibonacci de 23
        if(n==0){
            return 0;
        }
        short a=0;
        short b = 1;
        for(short i = 1;i<n;i++ ){
            b=	(short) (a+b);
            a=(short)(b-a);
            
                    
        }
        return b;        
    }
   long fibo4(long n){//empieza a mandar overflow despues de fibonacci de 92
        if(n==0){
            return 0;
        }
        long a=0;
        long b = 1;
        for(long i = 1;i<n;i++ ){
            b=(a+b);
            a=(b-a);
            
                    
        }
        return b;        
    }
     long long fibo5(long long n){//empieza a mandar overflow despues de fibonacci de 92
        if(n==0){
            return 0;
        }
        long long a=0;
        long long b = 1;
        for(long long i = 1;i<n;i++ ){
            b=	a+b;
            a=b-a;
            
                    
        }
        return b;        
    }
 
int main()
{
	
    int a;
    short b;
    long c;
    long long d;
  
    cin>> a;
    cin>> b;
    cin>> c;
    cin>> d;

    cout<< fibo2(a)<<endl;
    cout<< fibo3(b)<<endl;
    cout<< fibo4(c)<<endl;
    cout<< fibo5(d)<<endl;

	return 0;
}