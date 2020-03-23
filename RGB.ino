const int blue=4;
const int red=5;
const int green=6;
String data;
void setup() {
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  Serial.begin(9600);
  analogWrite(red,0);
  analogWrite(green,0);
  analogWrite(blue,0);

}

void loop() {
 
}

void serialEvent()
{
  data=Serial.readString();
  analogWrite(red,parseRed(data));
  analogWrite(green,parseGreen(data));
  analogWrite(blue,parseBlue(data));
}
int parseRed(String a)
{
    a.remove(a.indexOf('-'));
    return a.toInt();
}
int parseGreen(String a)
{
    a.remove(0,a.indexOf('-')+1);
    a.remove(a.indexOf('*'));
    return a.toInt();
}
int parseBlue(String a)
{
    a.remove(0,a.indexOf('*')+1);
    return a.toInt();
}
