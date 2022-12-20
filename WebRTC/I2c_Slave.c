#include <Wire.h>
#include <Servo.h>

#define address 0x09
char c = '\0';
int flag = 0;
Servo servos[6];
byte data_to_echo = 0x07;

void Open_PWM(char c);
void Close_PWM(char c);
void Stop_PWM(char c);
void sendData(void);
void All_PWM(char i);

void setting_PWM_PIN() {

    servos[0].attach(2);
    servos[1].attach(3);
    servos[2].attach(4);
    servos[3].attach(5);
    servos[4].attach(6);
    servos[5].attach(7);

}

void All_PWM(char i) {
    
    Open_PWM(i);
    delay(1000); //1s

    Stop_PWM(i);
    delay(3000);

    Close_PWM(i);
    delay(1000);

    Stop_PWM(i);

    Serial.print('\n');

}

void Event(int incomebyte) {

   char c_tmp;
    
    while(Wire.available()){

        c = Wire.read();
        c_tmp = c;

        Serial.print("Data Recieving..");
       

        if (c_tmp == '1' || c_tmp == '2' || c_tmp == '3' || c_tmp =='4' || c_tmp == '5' || c_tmp =='6') {
          flag = 1;
          break; 
        }
    }

    Serial.println(c_tmp);

}

void setup() {
  // put your setup code here, to run once:
    c = '\0';
    flag = 0;
    setting_PWM_PIN();

    Wire.begin(address);
    Wire.onReceive(Event);
    Wire.onRequest(sendData);

    Serial.begin(9600);
    //Serial.print("\nStart test PWM\n");
    All_PWM('1');
}

void loop() {

  if (flag) {

    All_PWM(c);
    flag = 0;
    
  }

}

void Open_PWM(char c){

    int num = int(c);
    
    if (num > 54 or num < 49) return;

    Serial.print("Opening servo..");

    switch (num)
    {
      case 49:
        servos[0].write(0);
        break;
      case 50:
        servos[1].write(180);
        break;
      case 51:
        servos[2].write(180);
        break;
      case 52:
        servos[3].write(180);
        break;
      case 53:
        servos[4].write(180);
        break;
      case 54:
        servos[5].write(180);
        break;
      
      default:
        Serial.print("Error\n");
        break;
    }

}

void Stop_PWM(char c){

    int num = int(c);

    if (num > 54 or num < 49) return;

    Serial.print("Stop servo..");


    switch (num)
    {
      case 49:
        servos[0].write(90);
        break;
      case 50:
        servos[1].write(90);
        break;
      case 51:
        servos[2].write(90);
        break;
      case 52:
        servos[3].write(90);
        break;
      case 53:
        servos[4].write(90);
        break;
      case 54:
        servos[5].write(90);
        break;
      
      default:
        Serial.print("Error\n");
        break;
    }

}

void Close_PWM(char c){

    int num = int(c);

    if (num > 54 or num < 49) return;

    Serial.print("Closing servo..");

    switch (num)
    {
      case 49:
        servos[0].write(180);
        break;
      case 50:
        servos[1].write(0);
        break;
      case 51:
        servos[2].write(0);
        break;
      case 52:
        servos[3].write(0);
        break;
      case 53:
        servos[4].write(0);
        break;
      case 54:
        servos[5].write(0);
        break;
      
      default:
        Serial.print("Error\n");
        break;
    }

}

void sendData(){

  Wire.write(data_to_echo);

}