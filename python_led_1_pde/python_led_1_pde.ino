
int ledPin = 2;

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(5);
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, HIGH);
}

void loop() {
    switch (readData()) {
        case 0 :
            //set digital low
            digitalWrite(ledPin, LOW); break;
        case 1 :
            //set digital high
            digitalWrite(ledPin, HIGH); break;
    }
}

char readData() {
    Serial.println("read data");
    while(1) {
        if(Serial.available() > 0) {
            int val = Serial.parseInt();
            Serial.println(val);
            return val;
        }
    }
}
