/*
 * Exception not implemented within the program
 * Brute force on the voe computation
 */

package Java.src.SkillsTest2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class RazonVote implements ActionListener {

    JFrame frame;

    JButton vote, result;
    JRadioButton CPE, ME, EE, CE, ECE;

    int msCPE = 0, msME = 0, msEE = 0, msCE = 0, msECE = 0;

    public static void main(String args[]) {
        new RazonVote();

    }

    RazonVote() {

        frame = new JFrame("Voting for MS CEA 2014");

        JPanel panel = new JPanel(new GridLayout(5, 1));
        JPanel buttons = new JPanel(new FlowLayout());
        Container contentPane = frame.getContentPane();
        contentPane.setLayout(new BorderLayout());
        contentPane.add(panel, BorderLayout.PAGE_START);
        contentPane.add(buttons, BorderLayout.SOUTH);

        vote = new JButton("Vote");
        result = new JButton("Display Result");

        vote.addActionListener(this);
        result.addActionListener(this);

        CPE = new JRadioButton("Ms CPE");
        ME = new JRadioButton("Ms ME");
        EE = new JRadioButton("Ms EE");
        CE = new JRadioButton("Ms CE");
        ECE = new JRadioButton("Ms ECE");

        ButtonGroup bg = new ButtonGroup();
        bg.add(CPE);
        bg.add(ME);
        bg.add(EE);
        bg.add(CE);
        bg.add(ECE);

        panel.add(CPE);
        panel.add(ME);
        panel.add(EE);
        panel.add(CE);
        panel.add(ECE);
        buttons.add(vote);
        buttons.add(result);

        frame.setSize(350, 200);

        frame.setVisible(true);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == (vote)) {
            if (CPE.isSelected()) {
                msCPE++;
                JOptionPane.showMessageDialog(null, "You have voted successfully!", "Vote", JOptionPane.PLAIN_MESSAGE);
            } else if (ME.isSelected()) {
                msME++;
                JOptionPane.showMessageDialog(null, "You have voted successfully!", "Vote", JOptionPane.PLAIN_MESSAGE);
            } else if (EE.isSelected()) {
                msEE++;
                JOptionPane.showMessageDialog(null, "You have voted successfully!", "Vote", JOptionPane.PLAIN_MESSAGE);
            } else if (CE.isSelected()) {
                msCE++;
                JOptionPane.showMessageDialog(null, "You have voted successfully!", "Vote", JOptionPane.PLAIN_MESSAGE);
            } else if (ECE.isSelected()) {
                msECE++;
                JOptionPane.showMessageDialog(null, "You have voted successfully!", "Vote", JOptionPane.PLAIN_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(null, "You did not select any of the candidates!", "Vote", JOptionPane.ERROR_MESSAGE);
            }
        }
        if (e.getSource() == (vote)) {
            int a = msCPE;
            int b = msME;
            int c = msEE;
            int d = msCE;
            int f = msECE;
            JOptionPane.showMessageDialog(null, "Candidate          |           VOTES"
                    + "\nMs CPE               |            " + a
                    + "\nMs ME                 |           " + b
                    + "\nMs EE                  |           " + c
                    + "\nMs CE                  |           " + d
                    + "\nMs ECE                |           " + f, "Tally of  Votes", JOptionPane.PLAIN_MESSAGE);

        }

        if (e.getSource() == (result)) {

            int a = msCPE;
            int b = msME;
            int c = msEE;
            int d = msCE;
            int f = msECE;
            JOptionPane.showMessageDialog(null, "Candidate          |           VOTES"
                    + "\nMs CPE               |            " + a
                    + "\nMs ME                 |           " + b
                    + "\nMs EE                  |           " + c
                    + "\nMs CE                  |           " + d
                    + "\nMs ECE                |           " + f, "Tally of  Votes", JOptionPane.PLAIN_MESSAGE);

        }

    }

}
