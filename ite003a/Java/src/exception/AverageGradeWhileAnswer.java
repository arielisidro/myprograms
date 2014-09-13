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

public class AverageGradeWhileAnswer {

    int grades[] = new int[5];

    int inputGrade(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int grade = sc.nextInt();
        return grade;

    }

    int computeAverage() {
        
        int average=0, sum = 0;
        int k = 0;
        try{
        while (grades[k] != -1) {

            sum += grades[k++];

        }
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
            System.out.println("Maximum is 5");
        }
        
        try{
            

            average = sum / k;
            
        }catch(ArithmeticException e){
            System.out.println("Must enter at least one grade");
        }
            
        return average;

    }

    void getGrades() {

        int k = 0;
        try {

            do {
                grades[k] = inputGrade("Please input grade #" + (k + 1) + ": ");
            } while (grades[k++] != -1);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Maximum number of entries is : " + 5);
            System.out.println("Now processing entries ...");
        }

    }

    public static void main(String[] args) {

        AverageGradeWhileAnswer ag = new AverageGradeWhileAnswer();

        ag.getGrades();
        System.out.println("Average grade: " + ag.computeAverage());

    }

}
