// FizzBuzz code using Arduino 
// Author: @InputBlackBoxOutput
// Written on 20 Oct 2020

// No additional components & connections required. 
// Just connect your Arduino to your PC

#define BAUDRATE 9600
#define LOOP_DELAY 700

void setup() {
 Serial.begin(BAUDRATE);
 delay(10);
}

void loop() {
  for (int i=1; i<=100; i++) {
    if(i%3 == 0 && i%5==0)
      Serial.println("FizzBuzz");
    else if(i%5==0)
      Serial.println("Buzz");
    else if(i%3 == 0)
      Serial.println("Fizz");
    else
      Serial.println(i);

    delay(LOOP_DELAY);
  }
  
}
