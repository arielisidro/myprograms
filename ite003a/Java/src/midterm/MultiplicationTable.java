/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package midterm;

import java.util.Scanner;

/**
 *
 * @author EDSA
 */
import java.util.Scanner;

public class MultiplicationTable {
    
    int startx,starty,endx,endy;
    
    private MultiplicationTable(){
        startx=inputNumber("Start Row:");
        endx=inputNumber("End Row:");
        starty=inputNumber("Start Column:");
        endy=inputNumber("End Column:");
    }
    private int inputNumber(String msg){
        Scanner sc= new Scanner(System.in);
        System.out.print(msg);
        int number=sc.nextInt();
        return number;
    }
    
    private void displayMultiplicationTable(){
        
        System.out.print("X");
        for (int k=starty;k<=endy;k++){
            System.out.print("\t"+k);
        }
        System.out.println();
        for (int i=startx;i<=endx;i++){
            System.out.print(i);
            for (int j=starty;j<=endy;j++){
                System.out.print("\t"+i*j);
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args){
        
        MultiplicationTable mt=new MultiplicationTable();
        
        mt.displayMultiplicationTable();
        
    }
    
    
}
