package ite003a.Java.src.FileHandling;

import java.io.*;

public class ByteStreams {

    static final String PATH = System.getProperty("user.dir") + "\\myprograms\\ite003a\\Java\\src\\FileHandling\\";

    public static void main(String args[]) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;

        try {

            in = new FileInputStream(PATH + "input.txt");
            out = new FileOutputStream(PATH + "output.txt");

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
