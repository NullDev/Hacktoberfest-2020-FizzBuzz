/*
    [DESCRIPTION]
    I wrote it in a more non-standard way and used mostly char arrays, byte and hex values

    Author: @nimbl0
 */

public class Main {

    public static void main(String[] args) {
        byte mainCounter = 0b00000000;
        byte mainLength = 0b01100100;

        byte fizzLength = 0b00000100;
        byte buzzLength = 0b00000100;

        char[] fizz = new char[fizzLength];
        fizz[0] = 0x66;
        fizz[1] = 0x69;
        fizz[2] = 0x7a;
        fizz[3] = 0x7a;

        char[] buzz = new char[buzzLength];
        buzz[0] = 0x62;
        buzz[1] = 0x75;
        buzz[2] = 0x7a;
        buzz[3] = 0x7a;

        while(mainCounter < mainLength) {
            if(mainCounter % 0b00000011 == 0b00000000) {
                System.out.println(fizz);
            } else if(mainCounter % 0b00000101 == 0b00000000) {
                System.out.println(buzz);
            } else {
                System.out.println(mainCounter);
            }
            mainCounter += 0b00000001;
        }
    }

}
