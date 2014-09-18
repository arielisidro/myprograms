package ite003a.Java.src.FileHandling;

import java.io.*;
import java.util.Scanner;

public class ReadProfile {

    static final String PATH = System.getProperty("user.dir") + "\\myprograms\\ite003a\\Java\\src\\FileHandling\\";

    String lastName, firstName;

    String inputString(String msg) {
        System.out.print(msg);
        Scanner sc = new Scanner(System.in);
        String id = sc.next();

        return id;
    }

    boolean isProfileFound(String id) throws IOException {
        FileReader in = null;

        BufferedReader inline;

        String line = null;

        boolean found = false;

        try {
            in = new FileReader(PATH + "\\profile.dat");

            inline = new BufferedReader(in);

            while ((line = inline.readLine()) != null) {

                if (line.equals(id)) {

                    lastName = inline.readLine();
                    firstName = inline.readLine();
                    
                    found = true;
                    break;

                }
            }

        } finally {
            if (in != null) {
                in.close();
            }
        }

        return found;

    }

    public static void main(String args[]) {

        ReadProfile rp = new ReadProfile();
        String id = rp.inputString("Please input id: ");

        try{
            if (rp.isProfileFound(id)){
                System.out.println("Last Name : "+rp.lastName);
                System.out.println("First Name: "+rp.firstName);
                
            }else{
                System.out.println("Profile not found !!!");
            }
            
        }catch(IOException e){
            System.out.println(e);
        }

    }
}
