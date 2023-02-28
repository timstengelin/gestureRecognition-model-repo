/*
 * bno055_acc.h
 *
 *  Created on: Oct 23, 2022
 *      Author: daniel
 */

#ifndef INC_BNO055_ACC_H_
#define INC_BNO055_ACC_H_

// The Register Map Page 0 is on PAGE 50!

#include "stm32f7xx_hal.h"

#define I2C_ADDR_ACC 0x28

#define CHIP_ID 		0x00	// BNO055 CHIP ID; default value: 0xA0
#define ACC_ID 			0x01	// ACC CHIP ID; default value: 0xFB
#define MAG_ID			0x02	// MAG CHIP ID; default value: 0x32
#define GYR_ID			0x03	// GYRO CHIP ID; default value: 0x0F

#define PAGE_ID			0x07	// Page ID of the register map

#define ST_RESULT		0x36	// Result of the self test

// Operation mode register and possible register values
#define OPERATION_MODE	0x3D
// CONFIG MODE
#define CONFIGMODE		0b0000
// Non-Fusion Mode
#define ACCONLY			0b0001
#define MAGONLY			0b0010
#define GYROONLY		0b0011
#define ACCMAG			0b0100
#define ACCGYRO			0b0101
#define MAGGYRO			0b0110
#define AMG				0b0111
#define IMU				0b1000
// Fusion Mode
#define COMPASS			0b1001
#define M4G				0b1010
#define NDOF_FMC_OFF	0b1011
#define NDOF			0b1100

// Data Register
#define ACC_DATA_X_LSB	0x08
#define ACC_DATA_Y_LSB	0x0A
#define ACC_DATA_Z_LSB	0x0C

#define GYR_DATA_X_LSB	0x14
#define GYR_DATA_Y_LSB	0x16
#define GYR_DATA_Z_LSB	0x18

// Calibration
#define CALIB_STAT 0x35

#define UNIT_SEL 0x3B

// ACC division factor for m/s^2 (MSQ)
#define ACC_DIV_MSQ 100.0
// GYR division factor for Deg./Sec (DPS)
#define GYR_DIV_DPS 16.0


void bno055_assignHandel(I2C_HandleTypeDef hi2c_device);
void bno055_setPageID(uint8_t pageID);
void bno055_setOperationMode(uint8_t mode);

uint8_t bno055_readUnit();
uint8_t bno055_setUnit();

uint16_t bno055_getRegValue(uint8_t reg);
void bno055_getAccData(uint16_t * x, uint16_t * y, uint16_t * z);
void bno055_getGyrData(uint16_t * x, uint16_t * y, uint16_t * z);
void readSensorValues(uint8_t* dataBuffer);

#endif /* INC_BNO055_ACC_H_ */
