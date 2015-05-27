import java.util.Scanner;
import java.lang.Math;

public class calculator
{
    public static void main(Double[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("Hello");
        System.out.println("What type of math do you want to do, +(addition), -(subtraction), *(multi   plication), /(divition), ^(exponent), or sqrt(square root)?");
        String math_type = scan.next();

        if(math_type.equals("+"))
        {
            System.out.println("Input the first number you want to use");
            double num_1 = scan.nextDouble();
            System.out.println("Input the number you want to add to the first number");
            double num_2 = scan.nextDouble();
            System.out.println(num_1 + num_2);
        }
        if(math_type.equals("-"))
        {
            System.out.println("Input the first number you want to use");
            double num_1 = scan.nextDouble();
            System.out.println("Input the number you want to subtract from the first number");
            double num_2 = scan.nextDouble();
            System.out.println(num_1 - num_2);
        }
        if(math_type.equals("*"))
        {
            System.out.println("Input the first number you want to use");
            double num_1 = scan.nextDouble();
            System.out.println("Input the number you want to multiply the first number by");
            double num_2 = scan.nextDouble();
            System.out.println(num_1 * num_2);
        }
        if(math_type.equals("/"))
        {
            System.out.println("Input the first number you want to use");
            double num_1 = scan.nextDouble();
            System.out.println("Input the number you want to devide the first number by");
            double num_2 = scan.nextDouble();
            System.out.println(num_1 / num_2);
        }
        if(math_type.equals("^"))
        {
            System.out.println("Input the first number you want to use");
            double num_1 = scan.nextDouble();
            System.out.println("Input the number you want raise the first number to the power to");
            double num_2 = scan.nextDouble();
            System.out.println(Math.pow(num_1, num_2));
        }
        if(math_type.equals("sqrt"))
        {
            System.out.println("Input the number you want to square root");
            double num_1 = scan.nextDouble();
            System.out.println(Math.pow(num_1, 0.5));
        }
    }
}