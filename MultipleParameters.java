class MultipleParameters{
    static void myCar(String brand, String model){
        System.out.println(brand + "-" + model + " Is A Great Car.");
    }
    public static void main(String[] args){
        myCar("BMW", "M8");
        myCar("Mercedes", "AMG-C63");
        myCar("Ford", "Mustang GT");
    }
}