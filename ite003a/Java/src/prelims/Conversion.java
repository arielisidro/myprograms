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
public class Conversion {
    
    static final double multiplier=5./9.;
    
    double F2C(double F){
        return multiplier*(F-32.);
    }
    
    double C2F(double C){
        return C/multiplier+32.;
    }
    
}
