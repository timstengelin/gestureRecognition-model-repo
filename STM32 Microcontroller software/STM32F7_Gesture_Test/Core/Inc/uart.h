/*
 * UART.h
 *
 *  Created on: Oct 23, 2022
 *      Author: daniel
 */

#ifndef INC_UART_H_
#define INC_UART_H_

#include "stm32f7xx_hal.h"

void UART_assignHandel(UART_HandleTypeDef huart1_device);
void UARTprintf(char pcString[]);
void UARTprintln(char pcString[]);

#endif /* INC_UART_H_ */
