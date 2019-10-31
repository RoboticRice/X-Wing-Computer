#pragma config(ProgramType, NonCompetition)
#pragma config(Sensor, in1,    Clock,          sensorTouch)
#pragma config(Sensor, in2,    Counter,        sensorTouch)
#pragma config(Sensor, in3,    Auto,           sensorTouch)
#pragma config(Sensor, in4,    Latch,          sensorLEDtoVCC)
#pragma config(Motor,  port1,            ,             tmotorServoStandard, openLoop)
#pragma config(Motor,  port2,            ,             tmotorServoContinuousRotation, openLoop)
#pragma config(Motor,  port3,            ,             tmotorVex269, openLoop)
#pragma config(Motor,  port4,            ,             tmotorVex393, openLoop)
#pragma config(Motor,  port5,            ,             tmotorVex393HighSpeed, openLoop)
#pragma config(Motor,  port6,            ,             tmotorVexFlashlight, openLoop, reversed)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

/*************************************************************************
OxnardXWing - R2D2
Sam Rice - 20191027
https://github.com/RoboticRice/

Description: This is the interface to control the R2D2 head on the X-Wing via PWM.

Configuration:
Orange PBNO - Move clockwise
Blue Latch PBNO - Run auto
Orange PBNO - Move counter-clockwise
Motor - Victor - Moves R2's head

Additional Notes:
* The "bVexAutonomousMode = false;" is needed to open up communication so
  that the VEX can talk to the radio transmitter.
* Other notes.
*************************************************************************/

#define AMOUNT 20

task main()
{
	//Run Once on Init Code Block
	int speed = 0;
	/*debug*/
	int time = 0;
	bool auton = 0;
	/*end*/
	bVexAutonomousMode = true;//false;			//Activates Remote Control Mode
	while (true)									  //Creates and infinite loop
	{
		//Main Continuous Code Block
		motor[port2] = speed;
		time = time100[T2];
		if (SensorValue[in3] == false)
		{ //manual mode
			auton = false;

			if (time100[T2] >= 5)
			{
				time100[T2] = 0;
				if (SensorValue[in4] == false)
					SensorValue[in4] = true;
				else
					SensorValue[in4] = false;
			}

			if (SensorValue[in1] == true)
				speed = AMOUNT;
			else if (SensorValue[in2] == true)
				speed = -AMOUNT;
			else
				speed = 0;
		} else {
			//auto mode
			auton = true;
			SensorValue[in4] = false;
			if (time100[T1] >= 100)
			{
				speed = AMOUNT;
				motor[port2] = speed;
				wait10Msec(80);
				motor[port2] = 0;
				wait10Msec(10);
				motor[port2] = -speed;
				wait10Msec(80);
				speed = 0;
				time10[T1] = 0;
			}
		}
	}
}
