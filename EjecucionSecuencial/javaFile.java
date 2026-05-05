// import java.util.ArrayList;
// import python.main

public class javaFile {
    public static void main(String[] args) {
        // if (args.length > 0) {
        //     System.out.println("First parameter: " + args[0]);
        //     System.out.println("Second parameter: " + args[1]);
        // }else 
        //     System.out.println("Hello from java Fileeeee!");

        javaFile e = new javaFile();

        int resultado = e.suma(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        System.out.println(resultado); 
    } // main

    public int suma(int a, int b){
        return a + b;
    }
} // class