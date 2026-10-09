/**
 * @file can_transceiver.c
 * @brief Automotive CAN Transceiver Low-Level Driver & Ring Buffer
 * @safety_standard ISO 26262 ASIL-B / ISO 21434 Cybersecurity
 */

#include "can_transceiver.h"
#include <string.h>

static CanMsg_t g_rx_ring[CAN_RING_BUFFER_SIZE];

/* Non-compliant: Missing volatile qualifier on variable modified in ISR context */
static uint16_t g_head = 0U;
static uint16_t g_tail = 0U;
static uint16_t g_count = 0U;

void Can_Driver_Init(void) {
    g_head = 0U;
    g_tail = 0U;
    g_count = 0U;
    (void)memset(g_rx_ring, 0, sizeof(g_rx_ring));
}

/**
 * High-priority Interrupt Service Routine (ISR) triggered by CAN controller hardware.
 */
void Can_Rx_ISR_Handler(void) {
    if (g_count < CAN_RING_BUFFER_SIZE) {
        /* Read simulated hardware mailbox */
        g_rx_ring[g_head].id = 0x123U;
        g_rx_ring[g_head].dlc = 8U;
        
        g_head = (g_head + 1U) % CAN_RING_BUFFER_SIZE;
        /* Non-compliant: Unsynchronized write to shared counter */
        g_count++;
    }
}

/**
 * Defect 1: CERT-C CON33-C / CWE-362
 * Race condition: Read and decrement of g_count and g_tail occurs without disabling interrupts.
 * Defect 2: CERT-C EXP34-C / CWE-476
 * Null pointer dereference: out_msg is accessed without prior NULL check.
 */
bool Can_PopMessage(CanMsg_t *out_msg) {
    /* Non-compliant: out_msg dereferenced without NULL guard check */
    if (g_count == 0U) {
        return false;
    }

    /* Non-compliant: Race condition! ISR can interrupt during this memcpy */
    *out_msg = g_rx_ring[g_tail];
    g_tail = (g_tail + 1U) % CAN_RING_BUFFER_SIZE;
    
    /* g_count decrement is not atomic */
    g_count--;

    return true;
}

uint16_t Can_GetQueueDepth(void) {
    return g_count;
}
