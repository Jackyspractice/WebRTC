#include <Wire.h>
#include <Servo.h>

#define address 0x09
char c = '\0';
Servo servos[6];
byte data_to_echo = 0x07;

void Open_PWM(char c);
void Close_PWM(char c);
void sendData(void);

void setting_PWM_PIN() {

    servos[0].attach(2);
    servos[1].attach(3);
    servos[2].attach(4);
    servos[3].attach(5);
    servos[4].attach(6);
    servos[5].attach(7);

}

void test_PWM() {

    for (char i = '1'; i < '7'; i++) {
      Open_PWM(i);
      delay(3000); //3s
      Close_PWM(i);
    }

}

void setup() {
  // put your setup code here, to run once:
    setting_PWM_PIN();

    Wire.begin(address);
    Wire.onReceive(Event);
    Wire.onRequest(sendData);

    Serial.begin(9600);
    Serial.print("Data Recieved:");
    //Serial.print("\nStart test PWM\n");
    //test_PWM();
}

void loop() {
  // put your main code here, to run repeatedly:
    delay(100);
}

void Open_PWM(char c){

    int num = int(c);

    if (num > 6 or num < 1) return;

    Serial.print("Opening servo on PIN:");
    Serial.print(c + "\n");

    switch (num)
    {
      case 1:
        servos[0].write(0);
        break;
      case 2:
        servos[1].write(0);
        break;
      case 3:
        servos[2].write(0);
        break;
      case 4:
        servos[3].write(0);
        break;
      case 5:
        servos[4].write(0);
        break;
      case 6:
        servos[5].write(0);
        break;
      
      default:
        Serial.print("Error\n");
        break;
    }

}

void Close_PWM(char c){

    int num = int(c);

    if (num > 6 or num < 1) return;

    Serial.print("Closing servo on PIN:");
    Serial.print(c + "\n");

    switch (num)
    {
      case 1:
        servos[0].write(180);
        break;
      case 2:
        servos[1].write(180);
        break;
      case 3:
        servos[2].write(180);
        break;
      case 4:
        servos[3].write(180);
        break;
      case 5:
        servos[4].write(180);
        break;
      case 6:
        servos[5].write(180);
        break;
      
      default:
        Serial.print("Error\n");
        break;
    }

}

void Event(int incomebyte) {
    
    while(Wire.available()){

        c = Wire.read();
        Serial.print(c);

        if (c <= '6' or c >= '0'){
          
          Open_PWM(c);
          delay(3000); //3s
          Close_PWM(c);
        
        }
        
    }
}


void sendData()
{
  Wire.write(data_to_echo);
}