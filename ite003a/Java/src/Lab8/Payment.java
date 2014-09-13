/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Lab8;

/**
 *
 * @author EDSA
 */
import javax.swing.*;
import java.awt.*;

public class Payment extends JPanel {

    JLabel lblTuitionFee,
            lblMiscellaneousFee,
            lblOtherFees,
            lblModeOfPayment,
            lblDownPayment,
            lblScholarship,
            lblDiscount;
    JTextField txtTuitionFee,
            txtMiscellaneousFee,
            txtOtherFees,
            txtDownPayment,
            txtScholarship,
            txtDiscount;
    JRadioButton rbCash, rbInstallment;
    JButton btnRegister, btnCancel;

    public Payment() {
        lblTuitionFee = new JLabel("Tuition Fee");
        txtTuitionFee = new JTextField(20);
        lblMiscellaneousFee = new JLabel("Miscellaneous Fee");
        txtMiscellaneousFee = new JTextField(20);
        lblOtherFees = new JLabel("Other Fees");
        txtOtherFees = new JTextField(20);
        lblModeOfPayment = new JLabel("Mode of Payment");
        rbCash = new JRadioButton("Cash");
        rbInstallment = new JRadioButton("Installment");
        ButtonGroup rbModeOfPayment = new ButtonGroup();
        rbModeOfPayment.add(rbCash);
        rbModeOfPayment.add(rbInstallment);

        lblDownPayment = new JLabel("DownPayment");
        txtDownPayment = new JTextField(20);
        lblScholarship = new JLabel("Scholarship");
        txtScholarship = new JTextField(20);
        lblDiscount = new JLabel("Discount");
        txtDiscount = new JTextField(20);

    }

    public static void createAndShowGUI(){
        JFrame frame = new JFrame("Payment");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(250,150);
        
        Payment PaymentPane = new Payment();
        PaymentPane.setOpaque(true);
        PaymentPane.setLayout(new FlowLayout());
        frame.setContentPane(PaymentPane);
        frame.setVisible(true);
    }
    
    public static void main(String[] args){
        javax.swing.SwingUtilities.invokeLater(new Runnable(){
            public void run(){
                createAndShowGUI();
            }
        }
        );
    }
    
}
