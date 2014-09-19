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
public class Person {
    private String first,last;
    
    
    public Person(){
        first=null;
        last=null;
    }
    public Person(String first,String last){
        this.first=first;
        this.last=last;
    }
    
    public void setName(String first,String last){
        this.first=first;
        this.last=last;
        
    }
    
    public String getName(){
        return first+" "+last;
    }
    
}
