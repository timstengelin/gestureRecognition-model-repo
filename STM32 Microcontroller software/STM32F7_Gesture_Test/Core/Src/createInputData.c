/*
 * createInputData.c
 *
 *  Created on: Feb 23, 2023
 *      Author: daniel
 */

#include "createInputData.h"
#include "uart.h"
#include <stdio.h>
#include <string.h>
#include "bno055_acc.h"

void acquire_and_process_data(float* input_data){
	uint8_t	reg_readings[18];
	int16_t raw_acc_data[3];
	int16_t raw_gyr_data[3];

	float accX, accY, accZ;
	float gyrX, gyrY, gyrZ;

	float aX[251];
	float aY[251];
	float aZ[251];

	float gX[251];
	float gY[251];
	float gZ[251];

	char str[300];

	uint16_t counter = 0;

	float normalize_data_buffer[251];

	GPIO_PinState userButton;

	// Gather 251 Sensor data samples of a motion for a gesture when the Button B1 was pressed
	userButton = HAL_GPIO_ReadPin(GPIOI, GPIO_PIN_11);

	if(userButton == GPIO_PIN_SET){

		while(counter != 251){

		// Read in the raw sensor values out of the acceleration and gyroscope sensor registers
		readSensorValues((uint8_t*)reg_readings);

		// Convert the 8 bit values of the acceleration register to a 16 bit value
		raw_acc_data[0] = (((int16_t)((uint8_t *)(reg_readings))[1] << 8) | ((uint8_t *)(reg_readings))[0]);
		raw_acc_data[1] = (((int16_t)((uint8_t *)(reg_readings))[3] << 8) | ((uint8_t *)(reg_readings))[2]);
		raw_acc_data[2] = (((int16_t)((uint8_t *)(reg_readings))[5] << 8) | ((uint8_t *)(reg_readings))[4]);

		// Convert the raw sensor values to a real acceleration value of the unit m/s^2
		accX = (float)(raw_acc_data[0] / ACC_DIV_MSQ);
		accY = (float)(raw_acc_data[1] / ACC_DIV_MSQ);
		accZ = (float)(raw_acc_data[2] / ACC_DIV_MSQ);

		// Convert the 8 bit values of the gyroscope register to a 16 bit value
		raw_gyr_data[0] = (((int16_t)((uint8_t *)(reg_readings))[13] << 8) | ((uint8_t *)(reg_readings))[12]);
		raw_gyr_data[1] = (((int16_t)((uint8_t *)(reg_readings))[15] << 8) | ((uint8_t *)(reg_readings))[14]);
		raw_gyr_data[2] = (((int16_t)((uint8_t *)(reg_readings))[17] << 8) | ((uint8_t *)(reg_readings))[16]);

		// Convert the raw sensor values to Deg./s
		gyrX = (float)(raw_gyr_data[0] / GYR_DIV_DPS);
		gyrY = (float)(raw_gyr_data[1] / GYR_DIV_DPS);
		gyrZ = (float)(raw_gyr_data[2] / GYR_DIV_DPS);

		sprintf(str,"%d, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f",counter , accX, accY, accZ, gyrX, gyrY, gyrZ);
		UARTprintln(str);

		// Store all sensor values to create later on the input data of the NN
		aX[counter] = accX;
		aY[counter] = accY;
		aZ[counter] = accZ;

		gX[counter] = gyrX;
		gY[counter] = gyrY;
		gZ[counter] = gyrZ;

		counter += 1;
		}

	}else{
		counter = 0;
	}

	// Further process of the sensor data ...
	// Create normalized input vector of the shape (1506, 1) for the NN

	if(counter == 251){
		// Normalization of aX
		min_max_normalize(aX, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i] = normalize_data_buffer[i];
		}

		// Normalization of aY
		min_max_normalize(aY, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i+251] = normalize_data_buffer[i];
		}

		// Normalization of aZ
		min_max_normalize(aZ, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i+502] = normalize_data_buffer[i];
		}

		// Normalization of gX
		min_max_normalize(gX, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i+753] = normalize_data_buffer[i];
		}

		// Normalization of gY
		min_max_normalize(gY, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i+1004] = normalize_data_buffer[i];
		}

		// Normalization of gZ
		min_max_normalize(gZ, 251, normalize_data_buffer);

		for(int i = 0; i < 251; i++){
			input_data[i+1255] = normalize_data_buffer[i];
		}
	}
}

void min_max_normalize(float data[], int length, float* normalize_data){
	float min = data[0];
	float max = data[0];

	for(int i = 0; i < length; i++){
		if(data[i] < min){
			min = data[i];
		}

		if(data[i] > max){
			max = data[i];
		}
	}

	for(int i = 0; i < length; i++){
		normalize_data[i] = (data[i]-min) / (max-min);
	}
}
