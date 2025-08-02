public class Elseif{
    public static void main(String[] args){
        int age=13;

        if(age<=12){
            System.out.println("Underage");
        }
        else if(age>12 && age<=19){
            System.out.println("Teenager");
        }
        else{
            System.out.println("Adult");
        }
    }
}