/**
 * @file bms_cell_monitor.h
 * @brief Automotive Battery Management System (BMS) Cell Voltage Monitoring
 * @target High-Voltage Traction Battery Pack (ASIL-C)
 */

#ifndef BMS_CELL_MONITOR_H
#define BMS_CELL_MONITOR_H

#include <stdint.h>
#include <stdbool.h>

#define BMS_MAX_CELLS            (96U)
#define BMS_OVERVOLTAGE_MV       (4250U)
#define BMS_UNDERVOLTAGE_MV      (2800U)
#define BMS_OVERTEMP_DEGC        (60)

typedef enum {
    BMS_STATE_INIT = 0,
    BMS_STATE_NORMAL,
    BMS_STATE_BALANCING,
    BMS_STATE_FAULT
} BmsState_t;

typedef struct {
    uint16_t cell_voltages[BMS_MAX_CELLS];
    int16_t  cell_temperatures[16];
    uint16_t pack_voltage_v;
    BmsState_t state;
    bool     contactor_open_req;
} BmsPackStatus_t;

/* Public API declarations */
void Bms_Init(void);
void Bms_ProcessCanPayload(const uint8_t *payload, uint8_t length);
void Bms_UpdateCellVoltage(uint8_t cell_index, uint16_t voltage_mv);
void Bms_StepStateMachine(void);
BmsPackStatus_t* Bms_GetPackStatus(void);

#endif /* BMS_CELL_MONITOR_H */
