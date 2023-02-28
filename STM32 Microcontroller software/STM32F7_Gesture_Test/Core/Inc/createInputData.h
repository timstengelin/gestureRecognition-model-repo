/*
 * createInputData.h
 *
 *  Created on: Feb 23, 2023
 *      Author: daniel
 */

#ifndef INC_CREATEINPUTDATA_H_
#define INC_CREATEINPUTDATA_H_

void acquire_and_process_data(float* input_data);
void min_max_normalize(float data[], int length,float * normalize_data);

#endif /* INC_CREATEINPUTDATA_H_ */
