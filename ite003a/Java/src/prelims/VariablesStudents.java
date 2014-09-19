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
public class VariablesStudents {
    
    public static void main(String[] args){
        EngineeringStudent es=new EngineeringStudent();
        EngineeringStudent es2=new EngineeringStudent();
        es2.setName("Kiko");
        es2.school="up";
        es2.setName("es2");
        es.setName("es");
        es.school="pup";
        System.out.println(es.getName()+" studies at "+es.getSchool());
        System.out.println(es2.getName()+" studies at "+es2.getSchool());
        
    }
}
