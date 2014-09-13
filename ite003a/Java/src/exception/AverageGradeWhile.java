/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package exception;

/**
 *
 * @author EDSA
 */
import java.util.Scanner;

public class AverageGradeWhile {
    
    int grades[]=new int[5];
    
    int inputGrade(String msg){
        Scanner sc=new Scanner(System.in);
        System.out.print(msg);
        int grade=sc.nextInt();
        return grade;
        
    }
    
    int computeAverage(){
        int average,sum=0;
        int k=0;
        while (grades[k] != -1){
            
            sum+=grades[k];
            
        }
        
        average=sum/k;
        
        return average;
        
    }
    
    void getGrades(){
        int k=0;
        do{
            grades[k]=inputGrade("Please input grade #"+(k+1)+": ");            
        }
        while (grades[k++] != -1);
            
        
    }
    public static void main(String[] args){
        
        AverageGradeWhile ag=new AverageGradeWhile();
        
        ag.getGrades();
        System.out.println("Average grade: "+ag.computeAverage());
        
    }
    
    
}
