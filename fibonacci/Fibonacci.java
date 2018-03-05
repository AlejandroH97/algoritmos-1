/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fibonacci;

import java.util.Scanner;
import java.math.*;
import java.lang.*;

/**
 *
 * @author juanitobanana
 */
public class Fibonacci {

    /**
     * @param args the command line arguments
     */
    static int fibo(int n){ // empieza a mandar overflow despues de fibonacci de 46
        if(n==0){
            return 0;
        }
        int a=0;
        int b = 1;
        for(int i = 1;i<n;i++ ){
            b=a+b;
            a=b-a;
            
                    
        }
        return b;        
    }
    static byte fibo2(byte n){  //empieza a mandar overflow despues de fibonacci de 11
        if(n==0){
            return 0;
        }
        byte a=0;
        byte b = 1;
        for(byte i = 1;i<n;i++ ){
            b=	(byte) (a+b);
            a=(byte)(b-a);
            
                    
        }
        return b;        
    }
    static short fibo3(short n){//empieza a mandar overflow despues de fibonacci de 23
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
    static long fibo4(long n){//empieza a mandar overflow despues de fibonacci de 92
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
    static BigInteger fibo5(BigInteger n){//no hay
        if(n.equals(BigInteger.ZERO)){
            return BigInteger.ZERO;
        }
        BigInteger a=BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        for(BigInteger i = BigInteger.ONE;i.compareTo(n)<0;i=i.add(BigInteger.ONE) ){
            b=	a.add(b);
            a=b.subtract(a);
            
                    
        }
        return b;        
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        byte a=sc.nextByte();
        short b = sc.nextShort();
        int c = sc.nextInt();
        long d = sc.nextLong();
        BigInteger e = sc.nextBigInteger();
        
                
        
        System.out.println(fibo(c)+","+fibo2(a)+","+fibo3(b)+","+fibo4(d)+","+fibo5(e));
        //System.out.println(fibo5(e)); //descomentar si quiere saber solo el fibonacci del BI
    }
    
}
