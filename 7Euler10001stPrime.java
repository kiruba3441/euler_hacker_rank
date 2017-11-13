//package euler;

import java.util.BitSet;

public class 7Euler10001stPrime {

	public static void sieveOfEratosthenes(Integer n) {
		BitSet sieve = new BitSet(500000);
		int primeCount = 0;
		for(int i=2;i<500000;i++){
			if(!sieve.get(i)){
				for(int j=2*i;j<=500000;j+=i){
					sieve.set(j);
				}
				primeCount++;
				if(primeCount==n){
					System.out.println(i);
					return;
				}
			}
			
		}
	}
	
	public static void main(String[] args){
		sieveOfEratosthenes(952);
	}
}
