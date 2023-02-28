/*
 * i2c_master.h
 *
 *  Created on: Oct 23, 2022
 *      Author: daniel
 */

#ifndef INC_I2C_MASTER_H_
#define INC_I2C_MASTER_H_

#include "stm32f7xx_hal.h"

void I2C_readData(I2C_HandleTypeDef hi2c, uint8_t reg, uint8_t *data, uint8_t len);
void I2C_receiveData(I2C_HandleTypeDef hi2c, uint8_t reg, uint8_t *data, uint8_t len);
void I2C_transmitData(I2C_HandleTypeDef hi2c, uint8_t reg, uint8_t data);

#endif /* INC_I2C_MASTER_H_ */
