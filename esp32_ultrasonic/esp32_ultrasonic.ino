const int trigPin = 5;
const int echoPin = 18;

const long baudRate = 115200; 

void setup() {
  Serial.begin(baudRate);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long duration = pulseIn(echoPin, HIGH);
  
  int distance = duration * 0.034 / 2;
  
  Serial.println(distance);
  
  delay(100); 
}