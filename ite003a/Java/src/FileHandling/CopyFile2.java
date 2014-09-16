
package ite003a.Java.src.FileHandling;

import java.io.*;

public class CopyFile2 {
   public static void main(String args[]) throws IOException
   {
      FileReader in = null;
      FileWriter out = null;

      try {
         String p = "D:\\ISIDRO\\ariel\\Dropbox\\java\\myprograms\\ite003a\\Java\\src\\FileHandling";
         in = new FileReader(p+"\\input.txt");
         out = new FileWriter(p+"\\output.txt");
         
         int c;
         while ((c = in.read()) != -1) {
             System.out.println((char)c);
            out.write(c);
         }
      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}
