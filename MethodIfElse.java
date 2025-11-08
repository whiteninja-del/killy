class MethodIfElse {
    static void checkAge(int age){
        if (age<18){
            System.out.println("Too Young To Vote.");
        }
        else
        {
            System.out.println("Eligible To Vote");
        }
    }
    public static void main(String[] args){
        checkAge(20);
    }
}
