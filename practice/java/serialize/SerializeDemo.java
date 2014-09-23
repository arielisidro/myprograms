package practice.java.serialize;

import java.io.*;

public class SerializeDemo {

    //static final String PATH = System.getProperty("user.dir") + "\\myprograms\\practice\\java\\serialize\\";
    static final String PATH = "D:\\ISIDRO\\ariel\\Dropbox\\aeidevs\\myprograms\\practice\\java\\serialize\\";

    public static void main(String[] args) {
        Employee e = new Employee();
        e.name = "Reyan Ali";
        e.address = "Phokka Kuan, Ambehta Peer";
        e.SSN = 11122333;
        e.number = 123;
        try {
            FileOutputStream fileOut
                    = new FileOutputStream(PATH+"employee.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(e);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in employee.ser");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }
}
