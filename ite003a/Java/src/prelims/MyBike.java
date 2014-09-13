/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package prelims;

/*
 *
 * @author TIPQC
 */
public class MyBike {
    
    public static void main(String[] args){
        Bicycle mb=new Bicycle();
        mb.setSpeed(10);
        mb.increaseSpeed(10);
        mb.changeCadence(10);
        mb.changeGear(20);
        mb.displayStatus();
        Bicycle anotherBike=new Bicycle();
        anotherBike.setSpeed(100);
        anotherBike.decreaseSpeed(10);
        anotherBike.changeCadence(20);
        anotherBike.changeGear(30);
        anotherBike.displayStatus();
        
        
        
    }
    
}
