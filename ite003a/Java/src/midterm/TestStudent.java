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
public class TestStudent {
    
    public static void main(String args[]){
        Student student1=new Student();
        student1.setStudID(100111);
        student1.setName("Rose Mary","Reyes");
        System.out.println("Student ID: "+student1.getStudID());
        System.out.println("Student ID: "+student1.getName());

        Student student2=new Student(1234,"first name","last name");
        System.out.println("Student ID: "+student2.getStudID());
        System.out.println("Student ID: "+student2.getName());

    }
    
}
