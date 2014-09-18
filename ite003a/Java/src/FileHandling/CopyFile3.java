package ite003a.Java.src.FileHandling;

import java.io.*;

public class CopyFile3 {

    static final String PATH = System.getProperty("user.dir")+"\\myprograms\\ite003a\\Java\\src\\FileHandling\\";

    public static void main(String args[]) throws IOException {
        FileReader in = null;
        BufferedReader inline = null;
        FileWriter out = null;
        System.out.println("*** "+PATH);

        try {
            in = new FileReader(PATH + "\\CopyFile.java");
            inline = new BufferedReader(in);
            out = new FileWriter(PATH + "\\output1.txt");
            PrintWriter outline = new PrintWriter(out);

            String line;
            while ((line = inline.readLine()) != null) {

                System.out.println(line);
                outline.println(line);
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
