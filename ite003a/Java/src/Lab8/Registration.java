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

public class Registration extends JPanel{
    
    JLabel lblStudentID, lblName, lblGener, lblProgram;
    JTextField txtStudentID, txtName;
    JRadioButton rbMale, rbFemale;
    JComboBox cmbProgram;
    JButton brnRegister, btnCancel;
    
    public Registration(){
        String[] programs={"CE", "CPE", "EE", "ECE", "ME", "IE"};
        lblStudentID = new JLabel("Student ID");
        txtStudentID = new JTextField(20);
    }
    
    
    
    
}
