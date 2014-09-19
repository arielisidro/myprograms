/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ite003a.LabManual.Activity06;

/**
 *
 * @author ariel
 */
public class TestPartTimeEmployee{
    
    public static void main(String[] args){
        PartTimeEmployee p1=new PartTimeEmployee();
        p1.setName("Glenda","Ramos");
        System.out.println(p1.getName());
        p1.setNameRateHours("Glenda","Ramos",500,60);
        System.out.println(p1.getName());
        System.out.println(p1.calculatePay());
    }
    
}
