/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ite003a.LabManual.Activity04;

/**
 *
 * @author ariel
 */
import java.util.Scanner;
public class ReverseString {

    public static void main(String[] args){
        String original,reverse="";
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a string: ");
        original=in.next();
        
        int length=original.length();
        
        for (int i=length-1;i>=0;i--){
            reverse=reverse+original.charAt(i);
        }
        
        System.out.println("The reverse of String: "+original+" is "+reverse);
    }
}
