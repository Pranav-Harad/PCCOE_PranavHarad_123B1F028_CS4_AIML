/**
 * @file bms_cell_monitor.c
 * @brief Automotive Battery Management System (BMS) Cell Voltage Monitoring
 * @safety_standard ISO 26262 ASIL-C
 */

#include "bms_cell_monitor.h"
#include <string.h>

/* Global pack telemetry */
static BmsPackStatus_t g_bms_pack;

/* External mock CAN send function */
extern int Can_TransmitFrame(uint32_t msg_id, const uint8_t *data, uint8_t dlc);

void Bms_Init(void) {
    (void)memset(&g_bms_pack, 0, sizeof(BmsPackStatus_t));
    g_bms_pack.state = BMS_STATE_INIT;
}

/**
 * Defect 1: MISRA C:2012 Rule 12.1 / CWE-783
 * Operator precedence ambiguity without parentheses in CAN payload decoding.
 */
void Bms_ProcessCanPayload(const uint8_t *payload, uint8_t length) {
    if (payload != NULL && length >= 4U) {
        uint8_t cell_id = payload[0];
        
        /* Non-compliant: '<<' and '|' without explicit grouping */
        uint16_t decoded_voltage = payload[1] << 8 | payload[2];
        
        Bms_UpdateCellVoltage(cell_id, decoded_voltage);
    }
}

/**
 * Defect 2: MISRA C:2012 Rule 18.1 / CERT-C ARR30-C
 * Missing upper bound check on cell_index array subscript.
 */
void Bms_UpdateCellVoltage(uint8_t cell_index, uint16_t voltage_mv) {
    /* Non-compliant: cell_index is not verified against BMS_MAX_CELLS (96U) */
    g_bms_pack.cell_voltages[cell_index] = voltage_mv;
    
    if (voltage_mv > BMS_OVERVOLTAGE_MV) {
        g_bms_pack.contactor_open_req = true;
        g_bms_pack.state = BMS_STATE_FAULT;
    }
}

/**
 * Defect 3: MISRA C:2012 Rule 16.4
 * Switch statement missing mandatory default label.
 * Defect 4: MISRA C:2012 Rule 17.7
 * Non-void return value from Can_TransmitFrame is not checked or handled.
 */
void Bms_StepStateMachine(void) {
    uint8_t status_pdu[8] = {0};
    status_pdu[0] = (uint8_t)g_bms_pack.state;

    switch (g_bms_pack.state) {
        case BMS_STATE_INIT:
            g_bms_pack.state = BMS_STATE_NORMAL;
            break;
            
        case BMS_STATE_NORMAL:
            if (g_bms_pack.contactor_open_req) {
                g_bms_pack.state = BMS_STATE_FAULT;
            }
            break;
            
        case BMS_STATE_BALANCING:
            /* Balance execution */
            break;
            
        case BMS_STATE_FAULT:
            g_bms_pack.contactor_open_req = true;
            break;
        /* Non-compliant: Missing default label */
    }

    /* Non-compliant: Return value of Can_TransmitFrame ignored */
    Can_TransmitFrame(0x18F00100U, status_pdu, 8U);
}

BmsPackStatus_t* Bms_GetPackStatus(void) {
    return &g_bms_pack;
}
