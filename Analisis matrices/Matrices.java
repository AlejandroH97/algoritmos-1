/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matrices;

/**
 *
 * @author juanitobanana
 */
import java.io.File;
import java.util.*;
import java.lang.*;







public class Matrices {
   

    /**
     * @param args the command line arguments
     */
     static int [][] multiplicar(int [][]matrizA,int [][]matrizB){
         int [][] c = new int[matrizA.length][matrizB[0].length];
         for(int i=0; i<c.length; i++){
             for(int j=0;j<c[i].length;j++){
                 for(int k =0; k< matrizA.length;k++){
                     c[i][j]+= matrizA[i][k]*matrizB[k][j]; 
                 }
             }
         }
         return c;
         
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        
        
        
        
        long startTime;
        long endTime;
        double duration;
        double [] arraytimes= new double[n-1];
        for(int i=2; i<n+1; i++){
            int matrizA[][] = new int[i][i];
            int matrizB[][] = new int [i][i];
            int resultado[][]= new int[i][i];
            for(int h=0; h<i; h++){
                for(int j=0; j<i;j++){
                    matrizA[h][j]=1;
                    matrizB[h][j]=2;       
                }               
            }
                double aux =0;
                for(int j=0; j<10;j++){
                    startTime = System.nanoTime();
                    resultado = multiplicar(matrizA,matrizB);
                    endTime = System.nanoTime();
                    duration = (endTime - startTime)/(2*(Math.pow((double)i, 3.0))); 
                    aux += duration;
            }
            arraytimes[i-2]= (aux/10.0)*0.000000001;
    }
    for(int i =0; i<arraytimes.length; i++){
        System.out.println(arraytimes[i]);
    }

}
}