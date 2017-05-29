  /* 
   *  Demo Code for sending 5 sensors readings.. 
  */
  float a=10;
  float b=12;
  float c=15;
  float d=16;
  float e=20;
void setup() {
Serial.begin(115200);
}

void loop() {
a=a+1;
b=b+1;
c=c+1;
d=d+1;
e=e+1;

Serial.print(a);
Serial.print("  ");
Serial.print(b);
Serial.print("  ");
Serial.print(c);
Serial.print("  ");
Serial.print(d);
Serial.print("  ");
Serial.print(e);
Serial.print("  ");
Serial.println();
delay(500);

}
