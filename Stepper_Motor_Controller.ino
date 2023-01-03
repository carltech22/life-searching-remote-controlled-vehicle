#include <AFMotor.h>
#define ledPin 12
int data = 0;
AF_Stepper Stepper2(200, 2);  // A 48-step-per-revolution motor on 
AF_Stepper Stepper1(200, 1);
void setup() {

  Serial1.begin(9600); //default baud rate for bt 38400
  Stepper2.setSpeed(10);  // 10 rpm
  Stepper1.setSpeed(10);
}
void loop() {
  if(Serial1.available() > 0){ // Checks whether data is comming from the serial port
    data = Serial1.read(); // Reads the data from the serial port
    
          if (data == '0') {
            //digitalWrite(ledPin, LOW); // Turn LED OFF
            Stepper2.step(10, BACKWARD, SINGLE);
            Stepper1.step(10, BACKWARD, SINGLE);  
            Serial1.println("LED: BACKWARD"); 
            }
              else if (data == '1') {
               // digitalWrite(ledPin, HIGH);
              Stepper2.step(10, FORWARD, SINGLE);
              Stepper1.step(10, FORWARD, SINGLE);  
                Serial1.println("LED: FORWARD");
               
              } 
  }
}
