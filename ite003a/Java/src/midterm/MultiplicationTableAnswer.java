/*
 * Input start and end of row
 * Input start and end of column
 * Display multiplication as a grid of text boxes

 */
package ite003a.Java.src.midterm;

import java.util.Scanner;

/**
 *
 * @author ariel
 */
public class MultiplicationTableAnswer {

    private double inputNumber(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int t = sc.nextInt();
        return t;

    }

    public static void main(String[] args) {

    }

}
