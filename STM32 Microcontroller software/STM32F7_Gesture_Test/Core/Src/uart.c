/*
 * UART.c
 *
 *  Created on: Oct 23, 2022
 *      Author: danie
 */

#include "uart.h"
#include <string.h>

UART_HandleTypeDef uart_comPort;

void UART_assignHandel(UART_HandleTypeDef huart1_device){

	uart_comPort = huart1_device;

}

void UARTprintf(char pcString[]){

	HAL_UART_Transmit(&uart_comPort, (uint8_t *) pcString, strlen(pcString), 10);

}

void UARTprintln(char pcString[]){

	HAL_UART_Transmit(&uart_comPort, (uint8_t *) pcString, strlen(pcString), 10);

	char newline[2] = "\r\n";
	HAL_UART_Transmit(&uart_comPort, (uint8_t *) newline, 2, 10);

}
