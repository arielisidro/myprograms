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
public class Student {
    
    static String  school="TIPQC";
    
    private String name;
    private String address;
    private int age;
    
    public void setName(String name){
        this.name=name;
    }
    
    public void setAddress(String address){
        this.address=address;
    }
    public void setAge(int age){
        this.age=age;
    }

    public String getName(){
        return this.name;
    }
    
    public String getAddress(){
        return this.address;
    }
    public int getAge(){
        return this.age;
    }

    public String getSchool(){
        return this.school;
    }
    
    public void displayStudentProfile(){
        System.out.println("Name: "+this.name);
        System.out.println("Address: "+this.address);
        System.out.println("Age: "+this.age);
    }
}
