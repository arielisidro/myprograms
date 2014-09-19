
/**
 * **********************
 * Author : Ariel E. Isidro 
 * Date : Sep 9, 2014 
 * Description : Two-level paging
 * using masking
 *
 ************************
 */
import java.util.Scanner;

class TwoLevelPaging3 {

    long inputAddress(String msg) {

        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        long address = sc.nextLong();

        return address;
    }

    long computeAddress(long address, int shift, int mask) {
        long a = address >> shift;
        a &= mask;
        return a;
    }

    public static void main(String[] args) {

        TwoLevelPaging3 tlp = new TwoLevelPaging3();
        long address = tlp.inputAddress("Please input logical address: ");
        int dmask = 0b1111111111;
        int p2mask = 0b1111111111;
        int p1mask = 0b111111111111;

        long p1 = tlp.computeAddress(address, 20, p1mask);
        long p2 = tlp.computeAddress(address, 10, p2mask);
        long d = tlp.computeAddress(address, 0, dmask);

        System.out.println("Address : " + address);

        System.out.println("p1 : " + p1);
        System.out.println("p2 : " + p2);
        System.out.println(" d : " + d);

    }
}
