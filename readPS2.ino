void setup() {
	// put your setup code here, to run once:
	Serial.begin(9600);
	while(!Serial);
}
void loop(){
	// put your main code here, to run repeatedly:
	if(Serial.read()=='s'){
		Serial.print(analogRead(0));
		Serial.print('x');
		Serial.print(analogRead(1));
		Serial.print('y');
	}
}
