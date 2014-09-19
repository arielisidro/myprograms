/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ite003a.Java.src.prelims;

/**
 *
 * @author ariel
 */
import java.util.Scanner;

public class TestConversion extends Conversion{

    private double inputTemperature(){
        Scanner sc=new Scanner(System.in);
        System.out.print("Input temperature: ");
        double t=sc.nextDouble();
        return t;
        
    }
    public static void main(String[] args){
        TestConversion c=new TestConversion();
        double temp=c.inputTemperature();
        System.out.println(temp +"F="+c.F2C(temp)+"C");
        System.out.println(temp +"C="+c.C2F(temp)+"F");
        double datatype=3f;
        System.out.println(datatype);
        
    }
}
