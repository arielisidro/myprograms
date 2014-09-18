/*
 * Input the start and end Celsius Temperature
 * Display the conversion table, Celsius, Fahrenheit, Kelvin
 * as grid of labels in increments of 5
 */
package ite003a.Java.src.midterm;

import java.util.Scanner;

/**
 *
 * @author ariel
 */
public class ConversionTable {

    private double inputTemperture(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int t = sc.nextInt();
        return t;

    }
    
    private double computeFahrenheit(double celsius){
        return 0;
    }
    
    private double computeKelvin(double celsius){
        return 0;
    }
    
    private void displayConversionTable(double startCelsius,double endCelsius){
        
        
    }

    public static void main(String[] args) {
        double startCelsius, endCelsius;
        ConversionTable ct = new ConversionTable();
        startCelsius = ct.inputTemperture("Please input start Celsius: ");
        endCelsius = ct.inputTemperture("Please input end Celsius: ");
        ct.displayConversionTable(startCelsius,endCelsius);
    }

}
