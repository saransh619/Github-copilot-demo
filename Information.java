import java.util.Scanner;

// guessing number in java 

public class Information {
    public static void main(String[] args) {
        int number = (int) (Math.random() * 100);
        System.out.println("Guessing number in java");
        System.out.println("Guess the number");
        int guess = 0;
        do {
            System.out.println("Enter your guess: ");
            System.out.println("Enter a number between 1 to 100");
            Scanner sc = new Scanner(System.in);
            guess = sc.nextInt();
            if (guess < number) {
                System.out.println("Guess is too low");
            } else if (guess > number) {
                System.out.println("Guess is too high");
            } else {
                System.out.println("You guessed it right");
                System.out.println("The number is " + number);
                break;
            }
        } while (true);
    }
}
