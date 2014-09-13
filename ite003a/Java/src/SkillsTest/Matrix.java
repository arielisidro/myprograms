/*
 * display a grid of textFields
 */

package SkillsTest;

/**
 *
 * @author EDSA
 */
public class Matrix {
    
    void displayMatrix(int[][] matrix){
        
    }
    
    void transposeMatrix(int[][] matrix,int[][] matrixTranspose){
        
    }
    
    public static void main(String[] args){
        Matrix m=new Matrix();
        int[][] matrix={
            {1,2,3},
            {4,5,6},
            {7,8,9},
            {10,11,12}
        };
        int[][] matrixTranspose=new int[4][3];
        
        m.displayMatrix(matrix);
        m.transposeMatrix(matrix, matrixTranspose);
        m.displayMatrix(matrixTranspose);
    }
    
}
