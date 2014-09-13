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
public class Student {
    private int studID;
    private String studFname;
    private String studLname;
    
    public Student(){
        studID=0;
        studFname="";
        studLname="";
    }
    
    public Student(int studID,String studFname,String studLname){
        this.studID=studID;
        this.studFname=studFname;
        this.studLname=studLname;
        
    }
    
    public void setStudID(int studID){
        this.studID=studID;
    }
    
    public int getStudID(){
        return studID;
    }
    
    public void setName(String studFname,String studLname){
        this.studFname=studFname;
        this.studLname=studLname;
    }
    
    public String getName(){
        return studFname + " " + studLname;
    }
    
}
