public class MultiDimArrayDemo {
    public static void main(String[] args){
        String[][] names={
            {"Mr. ","Mrs.", "Ms."},
            {"Smith", "Jones"}
        };
        //mr smith
        System.out.println(names[0][0] +names[1][0]);
        //ms jones
        System.out.println(names[0][2] +names[1][1]);
    }
}
