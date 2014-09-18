/*
 * Get and 
 * display the inverse of a matrix
 * in a 3x3 grid as JButtons
 */
package ite003a.Java.src.midterm;

/**
 *
 * @author ariel
 */
import javax.swing.JTextField;
import javax.swing.JFrame;
import java.awt.GridLayout;

public class MatrixAnswer extends JFrame {


    final static int MATRIX_SIZE = 3;

    void displayMatrix(int[][] matrix) {

    JFrame jf = new JFrame();
        jf.setLayout(new GridLayout(MATRIX_SIZE, MATRIX_SIZE));
        JTextField tf;//= new JButton();
        for (int i = 0; i < MATRIX_SIZE; i++) {
            for (int j = 0; j < MATRIX_SIZE; j++) {
                tf=new JTextField();
                //btn[i][j].setText(String.valueOf(matrix[i][j]));
                tf.setText(String.valueOf(matrix[i][j]));
                jf.add(tf);

            }
        }
        jf.setSize(300, 300);
        jf.setVisible(true);

    }

    void getTranspose(int[][] matrix, int[][] matrixTranspose) {

        for (int i = 0; i < MATRIX_SIZE; i++) {
            for (int j = 0; j < MATRIX_SIZE; j++) {
                matrixTranspose[j][i]=matrix[i][j];
            }
        }
    }

    public static void main(String[] args) {

        MatrixAnswer m = new MatrixAnswer();

        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int[][] matrixTranspose = new int[MATRIX_SIZE][MATRIX_SIZE];

        m.displayMatrix(matrix);
        m.getTranspose(matrix, matrixTranspose);
        m.displayMatrix(matrixTranspose);

    }

}
