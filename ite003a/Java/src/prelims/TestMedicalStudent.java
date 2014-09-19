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
public class TestMedicalStudent{
    
    
    public static void main(String[] args){
        MedicalStudent ms=new MedicalStudent();
        ms.setName("Francis");
        ms.setAddress("Antipolo City");
        ms.setAge(23);
        ms.dissectAnimal("Frog");
        ms.displayStudentProfile();
        System.out.println("Animal Type: "+ms.getAnimalType());
    }
    
}
