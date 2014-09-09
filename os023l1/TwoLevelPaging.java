import java.util.Scanner;

class TwoLevelPaging {

	long inputAddress(String msg){

		Scanner sc=new Scanner(System.in);
		System.out.print(msg);
		long address = sc.nextLong();

		return address;
	}


	String convert2Binary(long number){
		String b="";
		while (number > 0){
			b = number % 2 + b;
			number /= 2;
		}
		return b;
	}

	int convert2Decimal(String s){
		int d = 0;
		int l = s.length();
		int y=0;
		for (int i=l;i>0;i--){
			d += Long.parseLong(s.substring(i-1,i))*power(2,y++);
		}
		return d;
	}

	long power(int x,int y){

		long p=1;
		for (int i=y;i>0;i--){
			p *= x;
		}

		return p;

	}

	String padLeft(String s){

		int l=s.length();
		for (int i=1;i<=32-l;i++){
			s="0"+s;
		}

		return s;

	}

	public static void main(String[] args){

		TwoLevelPaging tlp=new TwoLevelPaging();
		long address=tlp.inputAddress("Please input logical address: ");
		System.out.println("Address : "+address);
		String binary = tlp.convert2Binary(address);
		binary = tlp.padLeft(binary);
		System.out.println(binary);
		String p1=binary.substring(0,10);
		String p2=binary.substring(10,20);
		String d=binary.substring(20,32);

		System.out.println("p1 : "+p1);
		System.out.println("p2 : "+p2);
		System.out.println(" d : "+d);
		System.out.println("p1 : "+tlp.convert2Decimal(p1));
		System.out.println("p2 : "+tlp.convert2Decimal(p2));
		System.out.println(" d : "+tlp.convert2Decimal(d));


	}
}
