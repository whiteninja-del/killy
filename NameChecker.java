class NameChecker{
    static void checkName(String name){
        if (name.equals("Caleb")){
            System.out.println("Welcome Onboard");
        }
        else{
            System.out.println("Access Denied");
        }
    }
    public static void main(String[] args){
        NameChecker.checkName("Caleb");
        NameChecker.checkName("Vaga");
    }
}