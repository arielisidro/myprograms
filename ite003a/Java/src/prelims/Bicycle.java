/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package prelims;

/**
 *
 * @author TIPQC
 */
public class Bicycle {
    
    int speed;
    int gear;
    int cadence;
    
    void setSpeed(int newSpeed){
        speed=newSpeed;
    }

    void increaseSpeed(int s){
        speed+=s;
    }
    
    void decreaseSpeed(int s){
        speed-=s;
    }
    
    void changeGear(int newGear){
        gear=newGear;
    }
    void changeCadence(int newCadence){
        cadence=newCadence;
    }
    
    void displayStatus(){
        System.out.println("Speed: "+speed);
        System.out.println("Gear: "+gear);
        System.out.println("Cadence: "+cadence);
    }

}
