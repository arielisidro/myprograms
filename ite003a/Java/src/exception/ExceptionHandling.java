/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exception;

/**
 *
 * @author EDSA
 */
public class ExceptionHandling {

    public static void main(String[] args) {
        String name = "The Quick and the Dead";
        int i = 0;
        try {
            while (i < 100) {
                System.out.println(name.charAt(i++));
            }
        } catch (StringIndexOutOfBoundsException e) {
            System.out.println(e);
        }
        
        System.out.println("Did not abort program");
    }

}
