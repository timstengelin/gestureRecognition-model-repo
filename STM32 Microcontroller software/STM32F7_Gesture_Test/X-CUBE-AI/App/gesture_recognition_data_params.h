/**
  ******************************************************************************
  * @file    gesture_recognition_data_params.h
  * @author  AST Embedded Analytics Research Platform
  * @date    Sun Feb 26 13:25:50 2023
  * @brief   AI Tool Automatic Code Generator for Embedded NN computing
  ******************************************************************************
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  ******************************************************************************
  */

#ifndef GESTURE_RECOGNITION_DATA_PARAMS_H
#define GESTURE_RECOGNITION_DATA_PARAMS_H
#pragma once

#include "ai_platform.h"

/*
#define AI_GESTURE_RECOGNITION_DATA_WEIGHTS_PARAMS \
  (AI_HANDLE_PTR(&ai_gesture_recognition_data_weights_params[1]))
*/

#define AI_GESTURE_RECOGNITION_DATA_CONFIG               (NULL)


#define AI_GESTURE_RECOGNITION_DATA_ACTIVATIONS_SIZES \
  { 6280, }
#define AI_GESTURE_RECOGNITION_DATA_ACTIVATIONS_SIZE     (6280)
#define AI_GESTURE_RECOGNITION_DATA_ACTIVATIONS_COUNT    (1)
#define AI_GESTURE_RECOGNITION_DATA_ACTIVATION_1_SIZE    (6280)



#define AI_GESTURE_RECOGNITION_DATA_WEIGHTS_SIZES \
  { 405032, }
#define AI_GESTURE_RECOGNITION_DATA_WEIGHTS_SIZE         (405032)
#define AI_GESTURE_RECOGNITION_DATA_WEIGHTS_COUNT        (1)
#define AI_GESTURE_RECOGNITION_DATA_WEIGHT_1_SIZE        (405032)



#define AI_GESTURE_RECOGNITION_DATA_ACTIVATIONS_TABLE_GET() \
  (&g_gesture_recognition_activations_table[1])

extern ai_handle g_gesture_recognition_activations_table[1 + 2];



#define AI_GESTURE_RECOGNITION_DATA_WEIGHTS_TABLE_GET() \
  (&g_gesture_recognition_weights_table[1])

extern ai_handle g_gesture_recognition_weights_table[1 + 2];


#endif    /* GESTURE_RECOGNITION_DATA_PARAMS_H */
