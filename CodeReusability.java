class CodeReusability{
    private String brand;
    private String model;

    public CodeReusability(String brand, String model){
        this.brand=brand;
        this.model=model;
    }
    public void start(){
        System.out.println(brand+" "+ model+ " is starting...");
    }
}