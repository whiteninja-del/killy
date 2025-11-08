class ArthmeticDemo {
    public static void main(String[] args){

        int result=5+6;
        System.out.println("5+6: " + result);

        int original_result=result;

        result= result-1;
        System.out.println(original_result + "-1: " + result);

        result=result*2;
        System.out.println(original_result + "*2: " + result);

        result=result/2;
        System.out.println(original_result + "/2: " + result);

        result=result%2;
        System.out.println(original_result + "%2: " + result);
        
    }
}