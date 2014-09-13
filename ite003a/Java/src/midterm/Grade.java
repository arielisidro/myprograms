/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package midterm;

/**
 *
 * @author EDSA
 */
public class Grade {
    double pGrade,mGrade,fGrade;
    
    public Grade(double pGrade,double mGrade, double fGrade){
        this.pGrade=pGrade;
        this.mGrade=mGrade;
        this.fGrade=fGrade;
    }
    
    public double computeAverage(){
        return (pGrade+mGrade+fGrade);
    }
    
    public String displayRemarks(double average){
        if (average>=75){
            return "passed";
        }else{
            return "failed";
        }
    }
    
    public String displayGradeEquivalent(double average){
       return "x"; 
    }
            
    
}
