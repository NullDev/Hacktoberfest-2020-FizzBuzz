//FizzBuzz code using Arduino 
/* Components needed 
 *  LCD 16*2
 *  RGB LED
Circuit Diagram Simulation: https://www.tinkercad.com/things/7o4HRSi5BxU
*/

// Author: @rafitc  | Visit https://rafirasheed.co

#include<LiquidCrystal.h> //library for LCD

int red_light_pin = 6;
int green_light_pin = 7;
int blue_light_pin = 9;

int flag = 0;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); //lcd pin intialisation
void setup()
{
  pinMode(red_light_pin, OUTPUT); //set RGB Pins
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
  
  lcd.begin(16, 2); 
  lcd.setCursor(1,0);
  lcd.print("Welcome to ");
  lcd.setCursor(0,1);
  lcd.print(" FizzBuzz");
  delay(1500);
  lcd.clear();
}

void loop()
{
  for(int i=1; i<=100; i++){
    if((i%3 == 0)&&(i%5 == 0)){ //for multiple of 3 and 5
      lcd.setCursor(5,1);
      lcd.print("FizzBuzz");
      digitalWrite(blue_light_pin,HIGH);
      flag = 1;
    }
    if(i%3 == 0){ //for multiple of 3
      lcd.setCursor(5,1);
      lcd.print("Fizz"); 
      digitalWrite(red_light_pin,HIGH);
      flag = 1;
    }
    if(i%5 == 0){  ////for multiple of 5
      lcd.setCursor(9,1); 
      lcd.print("Buzz");
      digitalWrite(green_light_pin,HIGH);
      flag = 1;
    }

    if(!flag){
      lcd.setCursor(5,0);
      lcd.print(i);
    }
    delay(1000);
    lcd.clear();
    clearAllPin();
    flag=0;
  }
  }
  void clearAllPin(){ //funciton to turn of all digital Pins
    digitalWrite(blue_light_pin,LOW);
    digitalWrite(red_light_pin,LOW);
    digitalWrite(green_light_pin,LOW);
  }
