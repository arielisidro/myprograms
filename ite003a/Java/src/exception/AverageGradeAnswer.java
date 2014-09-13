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

public class AverageGradeAnswer {

    int grades[] = new int[5];

    int inputGrade(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int grade = sc.nextInt();
        return grade;

    }

    int computeAverage() {
        int average = 0, sum = 0;
        int k = 0;
        try {
            for (k = 0; k < 100; k++) {

                sum += grades[k];

            }
        } catch (ArrayIndexOutOfBoundsException e) {
            
            System.out.println("Ignoring array out of bounds");

        }finally{
            average = sum /k;
        }


        return average;
    }

    public static void main(String[] args) {
        AverageGradeAnswer ag = new AverageGradeAnswer();
        int g;

        for (int k = 0; k < 5; k++) {
            ag.grades[k] = ag.inputGrade("Please input grade #" + (k + 1) + ": ");

        }

        System.out.println("Average grade: " + ag.computeAverage());

    }

}
