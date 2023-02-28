/*
 * i2c_master.c
 *
 *  Created on: Oct 23, 2022
 *      Author: daniel
 */

#include "i2c_master.h"


#define I2C_ADDR_ACC 0x28

void I2C_readData(I2C_HandleTypeDef hi2c, uint8_t reg, uint8_t *data, uint8_t len){

	HAL_I2C_Mem_Read(&hi2c, I2C_ADDR_ACC << 1, reg, I2C_MEMADD_SIZE_8BIT, data, len, 100);

}

void I2C_receiveData(I2C_HandleTypeDef hi2c,uint8_t reg, uint8_t *data, uint8_t len){

	HAL_I2C_Master_Transmit(&hi2c, I2C_ADDR_ACC << 1, &reg, 1, HAL_MAX_DELAY);
	HAL_Delay(100);

	HAL_I2C_Master_Receive(&hi2c, I2C_ADDR_ACC << 1, data, len, HAL_MAX_DELAY);
	HAL_Delay(100);

}

void I2C_transmitData(I2C_HandleTypeDef hi2c, uint8_t reg, uint8_t data){

	uint8_t txdata[2] = {reg, data};
	HAL_StatusTypeDef status;

	status = HAL_I2C_Master_Transmit(&hi2c, I2C_ADDR_ACC << 1, txdata, sizeof(txdata), 10);
	HAL_Delay(10);

	if(status == HAL_OK){
		int z = 0;
		z = z + 1;
	}

}
