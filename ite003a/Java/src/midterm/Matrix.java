/*
 * Get and 
 * display the inverse of a matrix
 * in a grid as JButtons
 */
package ite003a.Java.src.midterm;

/**
 *
 * @author ariel
 */

public class Matrix {
    final static int MATRIX_SIZE=3;
    
    void displayMatrix(int[][] matrix) {
    }

    void getTranspose(int[][] matrix, int[][] matrixTranspose) {

    }

    public static void main(String[] args) {

        Matrix m = new Matrix();

        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12}
        };
        int[][] matrixTranspose = new int[4][3];

        m.displayMatrix(matrix);
        m.getTranspose(matrix, matrixTranspose);
        m.displayMatrix(matrixTranspose);

    }

}
