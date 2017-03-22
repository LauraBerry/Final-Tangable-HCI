<<<<<<< HEAD


import RPi.GPIO as GPIO;
import time;
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);


servoPin=17;
GPIO.setwarnings(False);
GPIO.setup(servoPin, GPIO.OUT);
pwm=GPIO.PWM(servoPin, 50);
pwm.start(6);

servoPin2=27;
GPIO.setwarnings(False);
GPIO.setup(servoPin2, GPIO.OUT);
rwm=GPIO.PWM(servoPin2, 50);
rwm.start(6);

#third servo?

# Software SPI configuration:
CLK  = 18;
MISO = 23;
MOSI = 24;
CS   = 25;
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI);

state = 0;


while True:
	values = [0]*8
	values[0] = mcp.read_adc(0);
	values[1] = mcp.read_adc(1);

	if (values[0] > 100 and state == 0 and values[1]>100):
		values[0] = mcp.read_adc(0);
		print("sensor 1: "+ values[0]);
		values[1] = mcp.read_adc(1);
		print("sensor 2: " + values[1]);
		#start lifting seat
		pwm.ChangeDutyCycle(6);							#lift front of seat
		rwm.ChangeDutyCycle(6.5);		
		time.sleep(1);
		pwm.ChangeDutyCycle(6);							#lift front of seat
		rwm.ChangeDutyCycle(7);
		time.sleep(1);
		pwm.ChangeDutyCycle(6.5);							#lift front of seat
		rwm.ChangeDutyCycle(7.5);				
		time.sleep(1);
		pwm.ChangeDutyCycle(6.5);							#lift front of seat
		rwm.ChangeDutyCycle(8);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7);							#lift front of seat
		rwm.ChangeDutyCycle(8.5);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7);							#lift front of seat
		rwm.ChangeDutyCycle(9);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7.5);							#lift front of seat
		rwm.ChangeDutyCycle(9.5);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7.5);							#lift front of seat
		rwm.ChangeDutyCycle(10);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(8);							#lift front of seat
		rwm.ChangeDutyCycle(10.5);							#lift back of seat 
		time.sleep(1);
		#lift back of seat in increments
		pwm.ChangeDutyCycle(8);
		rwm.ChangeDutyCycle(11);
		time.sleep(1.5);
		state = 1;
		
	if(values[0] < 100 and state != 0):
		time.sleep(5);
		pwm.ChangeDutyCycle(7.5);
		rwm.ChangeDutyCycle(10);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(7);
		rwm.ChangeDutyCycle(9);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(6.5);
		rwm.ChangeDutyCycle(8);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(6);
		rwm.ChangeDutyCycle(7);
		time.sleep(0.5);
		rwm.ChangeDutyCycle(6);
		time.sleep(2);
		state = 0;
	


# while True:
	    # Read all the ADC channel values in a list.
    # The read_adc function will get the value of the specified channel (0-1).
	# values[0] = mcp.read_adc(0);
    # Print the ADC values.
    # while (values[0] >20):
		# values[0] = mcp.read_adc(0);
		#start lifting seat
		# pwm.ChangeDutyCycle(3);							#lift front of seat
		# time.sleep(1.5);
		# rwm.ChangeDutyCycle(3);							#lift back of seat 
		# time.sleep(1.5);
		#lift back of seat in increments
		# pwm.ChangeDutyCycle(4);
		# time.sleep(1.5);
		# pwm.ChangeDutyCycle(5);
		# time.sleep(1.5);
		# pwm.ChangeDutyCycle(6);
		# time.sleep(1.5);
	#no longer any pressure on force sensor so set back to original state
	#lower seat back to original hight
	# time.sleep(5);
	
	#flush here?	
			
=======


import RPi.GPIO as GPIO;
import time;
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);


servoPin=17;
GPIO.setwarnings(False);
GPIO.setup(servoPin, GPIO.OUT);
pwm=GPIO.PWM(servoPin, 50);
pwm.start(6);

servoPin2=27;
GPIO.setwarnings(False);
GPIO.setup(servoPin2, GPIO.OUT);
rwm=GPIO.PWM(servoPin2, 50);
rwm.start(6);

#third servo?

# Software SPI configuration:
CLK  = 18;
MISO = 23;
MOSI = 24;
CS   = 25;
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI);

state = 0;


while True:
	values = [0]*8
	values[0] = mcp.read_adc(0);

	if (values[0] > 100 and state == 0):
		values[0] = mcp.read_adc(0);
		print(values[0]);
		#start lifting seat
		pwm.ChangeDutyCycle(6);							#lift front of seat
		rwm.ChangeDutyCycle(6.5);		
		time.sleep(1);
		pwm.ChangeDutyCycle(6);							#lift front of seat
		rwm.ChangeDutyCycle(7);
		time.sleep(1);
		pwm.ChangeDutyCycle(6.5);							#lift front of seat
		rwm.ChangeDutyCycle(7.5);				
		time.sleep(1);
		pwm.ChangeDutyCycle(6.5);							#lift front of seat
		rwm.ChangeDutyCycle(8);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7);							#lift front of seat
		rwm.ChangeDutyCycle(8.5);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7);							#lift front of seat
		rwm.ChangeDutyCycle(9);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7.5);							#lift front of seat
		rwm.ChangeDutyCycle(9.5);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(7.5);							#lift front of seat
		rwm.ChangeDutyCycle(10);							#lift back of seat 
		time.sleep(1);
		pwm.ChangeDutyCycle(8);							#lift front of seat
		rwm.ChangeDutyCycle(10.5);							#lift back of seat 
		time.sleep(1);
		#lift back of seat in increments
		pwm.ChangeDutyCycle(8);
		rwm.ChangeDutyCycle(11);
		time.sleep(1.5);
		state = 1;
		
	if(values[0] < 100 and state != 0):
		time.sleep(5);
		pwm.ChangeDutyCycle(7.5);
		rwm.ChangeDutyCycle(10);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(7);
		rwm.ChangeDutyCycle(9);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(6.5);
		rwm.ChangeDutyCycle(8);
		time.sleep(0.5);
		pwm.ChangeDutyCycle(6);
		rwm.ChangeDutyCycle(7);
		time.sleep(0.5);
		rwm.ChangeDutyCycle(6);
		time.sleep(2);
		state = 0;
	


# while True:
	    # Read all the ADC channel values in a list.
    # The read_adc function will get the value of the specified channel (0-1).
	# values[0] = mcp.read_adc(0);
    # Print the ADC values.
    # while (values[0] >20):
		# values[0] = mcp.read_adc(0);
		#start lifting seat
		# pwm.ChangeDutyCycle(3);							#lift front of seat
		# time.sleep(1.5);
		# rwm.ChangeDutyCycle(3);							#lift back of seat 
		# time.sleep(1.5);
		#lift back of seat in increments
		# pwm.ChangeDutyCycle(4);
		# time.sleep(1.5);
		# pwm.ChangeDutyCycle(5);
		# time.sleep(1.5);
		# pwm.ChangeDutyCycle(6);
		# time.sleep(1.5);
	#no longer any pressure on force sensor so set back to original state
	#lower seat back to original hight
	# time.sleep(5);
	
	#flush here?	
			

>>>>>>> origin/master
