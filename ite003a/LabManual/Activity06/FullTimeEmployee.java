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
public class FullTimeEmployee extends Person {
    double payRate,noDays;
    
    public FullTimeEmployee(){
        
    }
    
    public FullTimeEmployee(String first,String last,double rate,double days){
        
    }
    
    public void setNameRateDays(String first,String last,double rate,double days){
            setName(first,last);
    }
    
    public double getPayRate(){
        return payRate;
    }
    
    public double getDaysWorked(){
        return noDays;
    }
}
