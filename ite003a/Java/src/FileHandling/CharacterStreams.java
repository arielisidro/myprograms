package ite003a.Java.src.FileHandling;

import java.io.*;

public class CharacterStreams {

    static final String PATH = System.getProperty("user.dir") + "\\myprograms\\ite003a\\Java\\src\\FileHandling\\";

    public static void main(String args[]) throws IOException {
        
        FileReader in = null;
        FileWriter out = null;

        try {

            in = new FileReader(PATH + "\\input.txt");
            out = new FileWriter(PATH + "\\output.txt");

            int c;
            while ((c = in.read()) != -1) {
                System.out.println((char) c);
                out.write(c);
            }
        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
}
