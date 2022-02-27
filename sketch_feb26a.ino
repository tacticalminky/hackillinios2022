#include <Servo.h>

Servo paper;
Servo plastic;
Servo garbage;
int pos = 0;
int bin = 0;
bool paper_open = false;
bool plastic_open = false;
bool garbage_open = false;

void setup() {
  paper.attach(A1);
  plastic.attach(A2);
  garbage.attach(A3);
  Serial.begin(9600);

}

void loop() {
    
}

void serialEvent(){
    if(Serial.available() > 1) {
    bin = Serial.parseInt();
    Serial.println(bin);
    if (bin == 0) {
      if (!paper_open){
        paper.write(103);
      } else {
        paper.write(93);
      }
      if (plastic_open) {
        plastic.write(83);
        plastic_open = false;
      } else {
        plastic.write(93);
      }
      if (garbage_open) {
        garbage.write(83);
        garbage_open = false;
      } else {
        garbage.write(93);
      }
      paper_open = true;
    }
    if (bin == 1) {
      if (paper_open){
        paper.write(83);
        paper_open = false;
      } else {
        paper.write(93);
      }
      if (!plastic_open) {
        plastic.write(103);
      } else {
        plastic.write(93);
      }
      if (garbage_open) {
        garbage.write(83);
        garbage_open = false;
      } else {
        garbage.write(93);
      }
      plastic_open = true;
    }
    if (bin == 2) {
      if (paper_open){
        paper.write(83);
        paper_open = false;
      } else {
        paper.write(93);
      }
      if (plastic_open) {
        plastic.write(83);
        plastic_open = false;
      } else {
        plastic.write(93);
      }
      if (!garbage_open) {
        garbage.write(103);
      } else {
        garbage.write(93);
      }
      garbage_open = true;
    }
  }
  delay(500);
  paper.write(93);
  plastic.write(93);
  garbage.write(93);
  Serial.flush();
}
