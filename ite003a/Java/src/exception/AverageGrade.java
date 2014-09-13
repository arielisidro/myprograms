/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package exception;

/**
 *
 * @author Ariel
 */
import java.util.Scanner;

public class AverageGrade {
    
    int grades[]=new int[5];
    
    int inputGrade(String msg){
        Scanner sc=new Scanner(System.in);
        System.out.print(msg);
        int grade=sc.nextInt();
        return grade;
        
    }
    
    int computeAverage(){
        int average,sum=0;
        int k;
        for (k=0;k<100;k++){
            
            sum+=grades[k];
            
        }
        
        average=sum/k;
        
        return average;
    }
    
    public static void main(String[] args){
        AverageGrade ag=new AverageGrade();
        int g;
        
        for(int k=0;k<5;k++){
            
            ag.grades[k]=ag.inputGrade("Please input grade #"+(k+1)+": ");
            
        }
        
        System.out.println("Average grade: "+ag.computeAverage());
        
    }
    
    
}
