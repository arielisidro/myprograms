/*
 * display a grid of all TextFields
 */
package SkillsTest;

import midterm.*;

/**
 *
 * @author EDSA
 */
import java.util.Scanner;

import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.GridLayout;

public class MultiplicationTable extends JFrame {

    int startx, starty, endx, endy;

    private MultiplicationTable() {
        startx = inputNumber("Start Row:");
        endx = inputNumber("End Row:");
        starty = inputNumber("Start Column:");
        endy = inputNumber("End Column:");
    }

    private int inputNumber(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int number = sc.nextInt();
        return number;
    }

    private void displayMultiplicationTable() {

        System.out.print("X");
        for (int k = starty; k <= endy; k++) {
            System.out.print("\t" + k);
        }
        System.out.println();
        for (int i = startx; i <= endx; i++) {
            System.out.print(i);
            for (int j = starty; j <= endy; j++) {
                System.out.print("\t" + i * j);
            }
            System.out.println();
        }
    }

    private void displayMultiplicationTableGrid() {

        JFrame jf = new JFrame();
        jf.setLayout(new GridLayout(endx - startx + 1+1, endy - starty + 1 + 1));

        JButton jb;

        jb = new JButton();
        jb.setText("X");
        jf.add(jb);

        for (int k = starty; k <= endy; k++) {
            jb = new JButton();
            jb.setText(String.valueOf(k));
            jf.add(jb);
        }
        for (int i = startx; i <= endx; i++) {
            jb = new JButton();
            jb.setText(String.valueOf(i));
            jf.add(jb);
            for (int j = starty; j <= endy; j++) {
                jb = new JButton();
                jb.setText(String.valueOf(i * j));
                jf.add(jb);
            }
        }

        jf.setSize(400, 400);
        jf.setVisible(true);

    }

    public static void main(String[] args) {

        MultiplicationTable mt = new MultiplicationTable();

        mt.displayMultiplicationTable();
        mt.displayMultiplicationTableGrid();

    }

}
