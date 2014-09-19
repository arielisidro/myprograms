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
public class MedicalStudent extends Student{
    
    private String animalType;
    
    public void dissectAnimal(String animalType){
        this.animalType=animalType;
    }
    
    public String getAnimalType(){
        return this.animalType;
    }

}
