/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ite003a.Java.src.prelims;

/**
 *
 * @author ariel
 */
public class EngineeringStudent extends Student{
    
    private String planType,planOwner,planLocation;
    
    public void setPlan(String planType,String planOwner,String planLocation){
        setPlanType(planType);
        setPlanOwner(planOwner);
        setPlanLocation(planLocation);
        
    }

    public void setPlanType(String planType){
        this.planType=planType;
    }
    
    public void setPlanOwner(String planOwner){
        this.planOwner=planOwner;
    }
    
    public void setPlanLocation(String planLocation){
        this.planLocation=planLocation;
    }
    
    public String getPlanType(){
        return this.planType;
    }
    
    public String getPlanOwner(){
        return this.planOwner;
    }
    
    public String getPlanLocation(){
        return this.planLocation;
    }
    
    public void displayEngineeringProfile(){
        System.out.println("-----------"
                +"\nType of Plan : "+this.planType
                +"\nOwner: "+planOwner
                +"\nLocation: "+planLocation
                +"\n----------"
                );
        
    }
    
    
}
