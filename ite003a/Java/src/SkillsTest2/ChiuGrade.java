/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//Average Grade

import java.util.Scanner;

public class ChiuGrade {

double grades[] = new double[5];
double unit[] = new double[5];

double inputGrade(String msg) {
Scanner sc = new Scanner(System.in);
System.out.print(msg);
double grade = sc.nextDouble();
return grade;
}

double inputUnit(String msg) {
Scanner sc = new Scanner(System.in);
System.out.print(msg);
double unit = sc.nextDouble();
return unit;
}

public class Arithmetic extends Exception{
int sum;
public Arithmetic(int sum){
this.sum=sum;
}
public int getAmount(){
return sum;
}
}

public double computeAverage() {

double sum = 0, average = 0;
int sum2=0;
int k = 0,
j = 0;

try {
for (k = 0, j = 0; j < 5; k++, j++) {
sum += grades[k] * unit[j];
sum2 += unit[j];
}
} catch (ArrayIndexOutOfBoundsException ae) {
System.out.println("Error 2: " + ae.getMessage());
}



try{
if(sum==0.0){
int i = (int)sum;
average = i / sum2;
}
else{
average = sum / sum2;
}
}catch(ArithmeticException ae){
System.out.println("Error Average: "+ae.getMessage());
}

return average;

}

void getGrades(){
int k=0, j=0;
try{
do{
if(k<5){
grades[k] = inputGrade("Please input grade #"+(k+1)+" : ");
if(grades[k]==-1){
break;
}
unit[j]=inputUnit("Please input number of unit: ");

}
j++;
}while(grades[k++]!=-1);
}catch(ArrayIndexOutOfBoundsException e){
System.out.println("Error 1: "+e.getMessage());
}
}

public static void main(String[] args){
AverageGrade ag=new AverageGrade();

ag.getGrades();

System.out.println("Average: "+ag.computeAverage());
}
}


// Voting

