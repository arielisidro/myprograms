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
public class TestEngineeringStudent extends Student{
    
   
    public static void main(String[] args){
        EngineeringStudent es=new EngineeringStudent();
        es.setName("Francis");
        es.setAddress("Antipolo City");
        es.setAge(23);
        //es.school="mit";
        System.out.println("Name of school: "+es.school);
        es.setPlan("House Plan","Mr. & Mrs. Smith","Antipolo City");
        es.displayStudentProfile();
        es.displayEngineeringProfile();
        EngineeringStudent es2=new EngineeringStudent();
        es2.setName("Kiko");
        System.out.println("Name of student:"+es2.getName());
        System.out.println("Name of school: "+es2.school);
        System.out.println(es.school);
        //es2.school="up";
        es2.setName("es2");
        es.setName("es");
        //es.school="pup";
        System.out.println(es.getName());
        System.out.println(es.getSchool());
        System.out.println(es2.getName());
        System.out.println(es2.getSchool());
        
        
    }
    
}
