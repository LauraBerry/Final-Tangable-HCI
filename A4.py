#https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
#https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
#https://computers.tutsplus.com/tutorials/how-to-use-a-breadboard-and-build-a-led-circuit--mac-54746
#http://www.instructables.com/id/Easiest-Raspberry-Pi-GPIO-LED-Project-Ever/step3/Software-Code/
#https://www.youtube.com/watch?v=HhfzRn2WcDQ&list=PLFA4eZ_bEubl_zVY-Dikk7Rpttk2xeWFv&index=4

import RPi.GPIO as GPIO;
import time;
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);


servoPin=11;
GPIO.setwarnings(False);
GPIO.setup(servoPin, GPIO.OUT);
pwm=GPIO.PWM(servoPin, 50);
pwm.start(6);

servoPin2=13;
GPIO.setwarnings(False);
GPIO.setup(servoPin2, GPIO.OUT);
rwm=GPIO.PWM(servoPin2, 50);
rwm.start(6);
# Software SPI configuration:
CLK  = 18;
MISO = 23;
MOSI = 24;
CS   = 25;
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI);

while True:
	    # Read all the ADC channel values in a list.
    values = [0]*2;
    for i in range(2):
    # The read_adc function will get the value of the specified channel (0-1).
	values[i] = mcp.read_adc(i);
    # Print the ADC values.
    if (values[0] >20):
		#start lifting seat
		pwm.ChangeDutyCycle(3);							#lift front of seat
		time.sleep(1.5);
		rwm.ChangeDutyCycle(3);							#lift back of seat 
		time.sleep(1.5);
		#lift back of seat in increments
		pwm.ChangeDutyCycle(4);
		time.sleep(1.5);
		pwm.ChangeDutyCycle(5);
		time.sleep(1.5);
		pwm.ChangeDutyCycle(6);
		#wait 9.5 seconds to give user time to get ont heir feet 
		time.sleep(1.5);
		time.sleep(8);
		
		#lower seat back to original hight
		pwm.ChangeDutyCycle(2);
		time.sleep(1.5);
		rwm.ChangeDutyCycle(2);
		time.sleep(1.5);
		#flush here?
	else:
		
			
	