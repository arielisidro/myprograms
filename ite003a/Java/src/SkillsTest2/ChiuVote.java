package Java.src.SkillsTest2;

import java.util.Scanner;

public class ChiuVote {

    String candidate[] = {"1. Ms. CPE", "2. Ms. ME", "3. Ms. ECE", "4. MS. CE", "5. Ms. IE"};
    int votes[] = new int[100];
    int numberVotes[] = new int[5];
    int i;

    public int inputVote(String msg) {
        Scanner sc = new Scanner(System.in);
        System.out.print(msg);
        int vote = sc.nextInt();
        return vote;
    }

    public void getVote() {
        int k = 0;

        do {
            try {
                votes[k] = inputVote("Enter [-1] to display vote or choose the number you want to vote: ");
                if (votes[k] == 1) {
                    numberVotes[0]++;
                } else if (votes[k] == 2) {
                    numberVotes[1]++;
                } else if (votes[k] == 3) {
                    numberVotes[2]++;
                } else if (votes[k] == 4) {
                    numberVotes[3]++;
                } else if (votes[k] == 5) {
                    numberVotes[4]++;
                } else if (votes[k] == -1) {
                    break;
                } else {
                    numberVotes[5]++;
                }

            } catch (ArrayIndexOutOfBoundsException ae) {
                System.out.println("Must input from 1-5 or -1");
            }

        } while (votes[k++] != -1);

    }

    public static void main(String[] args) {
        Voting v = new Voting();
        int k = 0;
        try {
            for (k = 0; k < 5; k++) {
                System.out.println(v.candidate[k]);
            }
        } catch (ArrayIndexOutOfBoundsException ae) {
            System.out.println("Error 2 : " + ae.getMessage());
        }

        v.getVote();
        try {

            for (k = 0; k < 5; k++) {
                System.out.println(v.candidate[k] + "\t\t\t" + v.numberVotes[k]);
            }

        } catch (ArrayIndexOutOfBoundsException ae) {
            System.out.println("Error 3: " + ae.getMessage());
        }
    }
}
