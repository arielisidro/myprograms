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

public class Login extends JPanel{
    JLabel lblUsername, lblPassword;
    JTextField txtUsername;
    JPasswordField txtPassword;
    JButton btnLogin, btnCancel;
    
    public Login(){
        lblUsername = new JLabel("Username");
        txtUsername = new JTextField(20);
        lblPassword = new JLabel("Password");
        txtPassword = new JPasswordField(20);
        btnLogin = new JButton("Login");
        btnCancel = new JButton("Cancel");
        add(lblUsername);
        add(txtUsername);
        add(lblPassword);
        add(txtPassword);
        add(btnLogin);
        add(btnCancel);
    }

    public static void createAndShowGUI(){
        JFrame frame = new JFrame("Login");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(250,150);
        
        Login LoginPane = new Login();
        LoginPane.setOpaque(true);
        LoginPane.setLayout(new GridLayout(3,2));
        frame.setContentPane(LoginPane);
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
