/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package javaapplication1;

/**
 *
 * @author Pia
 */
import java.util.Scanner;

public class RazonGrade {
    double grade[] = new double [5];
    int unit[] = new int [5];
    
    double inputGrade(String msg){
        Scanner sc = new Scanner(System.in);
        System.out.println(msg);
        double grade = sc.nextDouble();
        return grade;
         
    }
    int inputUnit(String msg){
        Scanner sc = new Scanner(System.in);
        System.out.println(msg);
        int unit = sc.nextInt();
        return unit;
    }
    double computeGrade(){
        double totalg;
        double sum =0;
        int k=0;
        int j=0;
        
        while(grade[k] != -1){
            sum+=grade[k]*unit[j];
            k++;
            j++;
            
        }
        totalg = sum;
        return totalg;
    }
    int computeUnit(){
        int totalu;
        int un = 0;
        int j = 0;
        int k=0;
        while((grade[j] != -1)&&(unit[j] != -1)){
            un+=unit[j];
            j++;
        }
        totalu = un;
        return totalu;
    }
    void getGrade(){
        int k=0;
        int j=0;
        try{
            do{
                grade[k]=inputGrade("Please input grade "+(k+1)+":");
                unit[j]=inputUnit("No of units: ");
            }while ((grade[k++] != -1)&&(unit[j++] != -1));
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Error "+e.getMessage());
        }
        
    }
    /*void getUnit(){
        int j=0;
        try{
            do{
              //unit[j]=inputUnit("No of units "+(j+1)+":");
            }while (unit[j++] != -1);
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Error "+e.getMessage());
        }
    }*/
    public static void main (String[] args){
        Grade g = new Grade();
        //int k=0;
            //for(k=0;k<100;k++){
               // g.grade[k] = g.inputGrade("Please input grade "+(k+1)+": ");
               // g.unit[k] = g.inputUnit("No. of units "+(k+1)+": ");
        //  
            g.getGrade();
            //g.getUnit();
            System.out.println("Total units: "+g.computeUnit());
            System.out.println("Weighted Grade: "+g.computeGrade());
            System.out.println("Weighted Average: "+g.computeGrade()/g.computeUnit());
    }
}

