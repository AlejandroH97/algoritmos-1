#include <stdlib.h>
#include <iostream>
#include <ctime>
#include <math.h> 
#include <limits>

using namespace std;

int main()
{
	int n ;
	cin >> n;
	double duracion;
	
	for(int f=2;f<n+1;f++){	
	int matrizA[f][f];
	int matrizB[f][f];
	int c[f][f];
	for (int h = 0; h<f; h++) {
		for (int j = 0; j<f; j++) {
			matrizA[h][j] = 1;
			matrizB[h][j] = 2;
			c[h][j]=0;
		}
	}
	double aux =0;
	for(int t=0; t<10;t++){
	 int start_s=clock();
	for (int i = 0; i < f; i++) {  
        for (int j = 0; j < f; j++) {   
            for (int k = 0; k < f; k++) {  
                c[i][j] += matrizA[i][k] * matrizB[k][j]; 
				
            }   
        }  
    }
    int stop_s=clock();
    duracion=  double(double(stop_s-start_s)/double(CLOCKS_PER_SEC)/(2.0*pow((double)f,3.0)));
    aux = aux +  duracion;  
}
	cout <<scientific<< double(aux/10)<<endl;
}
  



	
	system("PAUSE");
    return 0;
}

