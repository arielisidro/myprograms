package ite003a.Java.src.exception;

/**
 *
 * @author ariel
 */
public class BasicExceptionHandling  {
    
    public int divide(int dividend, int divisor){
        int quotient;
        
        if (divisor==0){
            quotient=0;
            throw new ArithmeticException();
        }else{
            quotient=dividend/divisor;
        }
        
        return quotient;
    }

    public static void main(String[] args) {
        
        try {
            System.out.println(1 / 0);
        } catch (ArithmeticException ae) {
            System.out.println("Exception: "+ae);
        }
        
        BasicExceptionHandling eh=new BasicExceptionHandling();
        eh.divide(3,0);
        
    }
}
