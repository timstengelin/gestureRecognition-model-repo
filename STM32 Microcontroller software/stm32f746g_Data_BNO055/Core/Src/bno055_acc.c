/*
 * bno055_acc.c
 *
 *  Created on: Oct 23, 2022
 *      Author: daniel
 */

#include "bno055_acc.h"
#include "i2c_master.h"

I2C_HandleTypeDef  bno055_i2c_port;

void bno055_assignHandel(I2C_HandleTypeDef hi2c_device) {
  bno055_i2c_port = hi2c_device;
}

void bno055_setPageID(uint8_t pageID){

	I2C_transmitData(bno055_i2c_port, PAGE_ID, pageID);
}

void bno055_setOperationMode(uint8_t mode){

	bno055_setPageID(0);

	I2C_transmitData(bno055_i2c_port, OPERATION_MODE, mode);

	// Operating mode switching time
	if(mode == CONFIGMODE){
		HAL_Delay(19);
	}else{
		HAL_Delay(7);
	}
}

uint8_t bno055_readUnit(){
	uint8_t unit[1];
	I2C_readData(bno055_i2c_port, UNIT_SEL, unit, 1);
	return unit[0];
}

uint8_t bno055_setUnit(){
	I2C_transmitData(bno055_i2c_port, UNIT_SEL, 0x80);

	return 1;
}

//****************************************************************
// Read the register values once

uint16_t bno055_getRegValue(uint8_t reg){

	uint8_t RXBufferReg[2];

	// bno055_setPageID(0);

	I2C_receiveData(bno055_i2c_port, reg, RXBufferReg, 2);

	return (RXBufferReg[1]<<8) | (RXBufferReg[0] & 0xFF);
}

void bno055_getAccData(uint16_t * x, uint16_t * y, uint16_t * z){

	*x = bno055_getRegValue(ACC_DATA_X_LSB);
	*y = bno055_getRegValue(ACC_DATA_Y_LSB);
	*z = bno055_getRegValue(ACC_DATA_Z_LSB);
}

void bno055_getGyrData(uint16_t * x, uint16_t * y, uint16_t * z){

	*x = bno055_getRegValue(GYR_DATA_X_LSB);
	*y = bno055_getRegValue(GYR_DATA_Y_LSB);
	*z = bno055_getRegValue(GYR_DATA_Z_LSB);
}

void readSensorValues(uint8_t* dataBuffer){

	// Read all ACC and GYR register values
	I2C_readData(bno055_i2c_port, ACC_DATA_X_LSB, dataBuffer, 0x18);
}



