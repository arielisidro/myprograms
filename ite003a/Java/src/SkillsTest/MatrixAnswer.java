/*
 * display a grid of textFields
 */

package SkillsTest;

/**
 *
 * @author EDSA
 */
import javax.swing.JFrame;
import javax.swing.JTextField;
import java.awt.GridLayout;

public class MatrixAnswer {
    
    final static int MATRIX_SIZE=3;
    void displayMatrix(int[][] matrix){
        JFrame jf=new JFrame();
        jf.setLayout(new GridLayout(MATRIX_SIZE,MATRIX_SIZE));
        
        JTextField tf;
        
        for (int i=0;i<MATRIX_SIZE;i++){
            for (int j=0;j<MATRIX_SIZE;j++){
                tf=new JTextField();
                tf.setText(String.valueOf(matrix[i][j]));
                jf.add(tf);
            }
            
        }
        
        jf.setSize(300,300);
        jf.setVisible(true);
    }
    
    void transposeMatrix(int[][] matrix,int[][] matrixTranspose){
        
        for (int i=0;i<MATRIX_SIZE;i++){
            for (int j=0;j<MATRIX_SIZE;j++){
                matrixTranspose[i][j]=matrix[j][i];
            }
            
        }
    }
    
    public static void main(String[] args){
        MatrixAnswer m=new MatrixAnswer();
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
