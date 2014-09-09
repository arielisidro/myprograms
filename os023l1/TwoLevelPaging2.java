/************************
Author : Ariel E. Isidro
Date   : Sep 9, 2014
Description : Two-level paging using masking

*************************/
import java.util.Scanner;

class TwoLevelPaging2 {

	long inputAddress(String msg){

		Scanner sc=new Scanner(System.in);
		System.out.print(msg);
		long address = sc.nextLong();

		return address;
	}

	public static void main(String[] args){

		TwoLevelPaging2 tlp=new TwoLevelPaging2();
		long address=tlp.inputAddress("Please input logical address: ");
		int dmask  = 0b111111111111;
		int p2mask = 0b1111111111;
		int p1mask = 0b1111111111;

		long d = address & dmask;

		long p2=address >> 12;
		p2=p2 & p2mask;

		long p1=address >> 22;
			
		System.out.println("Address : "+address);

		System.out.println("p1 : "+p1);
		System.out.println("p2 : "+p2);
		System.out.println(" d : "+d);


	}
}
