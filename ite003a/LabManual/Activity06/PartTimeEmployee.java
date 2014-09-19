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
public class PartTimeEmployee extends Person {
    
    private double payRate,hoursWorked;
   
    public PartTimeEmployee(){
        super();
        payRate=0;
        hoursWorked=0;
    }
    
    public PartTimeEmployee(String first,String last,double rate,double hours){
        super(first,last);
        payRate=rate;
        hoursWorked=hours;
    }
    
    public double calculatePay(){
        return (payRate * hoursWorked);
    }
    
    public void setNameRateHours(String first,String last,double rate,double hours){
        setName(first,last);
        payRate=rate;
        hoursWorked=hours;
    }
    
    public double getPayRate(){
        return payRate;
    }
    
    public double getHoursWorked(){
        return hoursWorked;
    }
}
