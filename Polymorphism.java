class Animal{
    public void animalSound(){
        System.out.println("The animal makes a sound");
    }
}
class Dog extends Animal{
    public void animalSound(){
        System.out.println("The dog says woo:woo");
    }
}
class Cow extends Animal{
    public void animalSound(){
        System.out.println("The cow says mooo:mooo");
    }
}
public class Polymorphism{
    public static void main(String[] args){
        Animal myAnimal=new Animal(); //create a animal object
        Animal myDog=new Dog(); //create a dog object
        Animal myCow=new Cow(); //create a cow object

        myAnimal.animalSound();
        myDog.animalSound();
        myCow.animalSound();
    }
}