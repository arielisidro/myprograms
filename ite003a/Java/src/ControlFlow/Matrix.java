/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ControlFlow;

/**
 *
 * @author EDSA
 */
public class Matrix {

    static int MAX_COLUMN = 2;
    static int MAX_ROW = 2;

    int[][] matrix = {
        {4, 6},
        {3, 8}};


    void printMatrix(int[][] m) {

        for (int i = 0; i < MAX_ROW; i++) {
            for (int j = 0; j < MAX_COLUMN; j++) {
                System.out.print(m[i][j]);
                if (j < MAX_COLUMN - 1) {
                    System.out.print(", ");
                }

            }
            System.out.println();
        }
        
    }

    int computeDeterminant2x2(int[][] m) {
        int determinant = 0;
        determinant=m[0][0] * m[1][1] - m[0][1]*m[1][0];

        return determinant;

    }

    public static void main(String[] args) {

        Matrix mx = new Matrix();
        mx.printMatrix(mx.matrix);
        System.out.println("Determinant="+mx.computeDeterminant2x2(mx.matrix));
        

    }

}
