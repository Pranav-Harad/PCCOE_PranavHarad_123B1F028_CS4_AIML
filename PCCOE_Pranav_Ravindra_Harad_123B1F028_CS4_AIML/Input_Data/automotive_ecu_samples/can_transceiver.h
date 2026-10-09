/**
 * @file can_transceiver.h
 * @brief Automotive CAN Transceiver Low-Level Driver & Ring Buffer
 */

#ifndef CAN_TRANSCEIVER_H
#define CAN_TRANSCEIVER_H

#include <stdint.h>
#include <stdbool.h>

#define CAN_RING_BUFFER_SIZE  (32U)

typedef struct {
    uint32_t id;
    uint8_t  dlc;
    uint8_t  data[8];
} CanMsg_t;

void Can_Driver_Init(void);
void Can_Rx_ISR_Handler(void);
bool Can_PopMessage(CanMsg_t *out_msg);
uint16_t Can_GetQueueDepth(void);

#endif /* CAN_TRANSCEIVER_H */
