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
import java.util.Scanner;
public class ControlFlow {
    public double inputNumber(String msg){
        Scanner sc= new Scanner(System.in);
        System.out.print(msg);
        double number=sc.nextDouble();
        return number;
    }
    public void ifElse(double grade){
        if (grade<75){
            System.out.println("failed");
        }else {
            System.out.println("passed");
        }
        
    }
    
    public void switchDemo(double grade){
        int g=(int)(grade);
        switch(g){
            case 100:
                System.out.println("Excellent");
                break;
            case 90:
                System.out.println("Very Satisfactory");
                break;
            case 80:
                System.out.println("Satisfactory");
                break;
            case 75:
                System.out.println("Good");
                break;
            default:
                System.out.println("Failed");
                break;
                
        }
        
        
    
    }
    
    public void ifElseIf(double grade){
        if (grade<75){
            System.out.println("failed");
        }else if (grade<78){
            System.out.println("passing");
        }else if (grade<81){
            System.out.println("fair");
        }else if (grade<84){
            System.out.println("satisfactory");
        }else if (grade<87){
            System.out.println("very satisfactory");
        }else if (grade<90){
            System.out.println("good");
        }else if (grade<93){
            System.out.println("very good");
        }else if (grade<96){
            System.out.println("meritorious");
        }else if (grade<99){
            System.out.println("superior");
        }else{
            System.out.println("excellent");
        }
        
    }
    
    public static void main(String[] args){
        ControlFlow cf=new ControlFlow();
        double grade=cf.inputNumber("Ano'ng grade mo:");
        cf.ifElse(grade);
        cf.ifElseIf(grade);
        cf.switchDemo(grade);
        
    }
    
}
