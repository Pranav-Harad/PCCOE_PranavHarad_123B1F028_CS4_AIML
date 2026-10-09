/**
 * @file throttle_actuator_driver.h
 * @brief Electronic Throttle Control (ETC) Actuator Driver
 * @safety_standard ISO 26262 ASIL-D
 */

#ifndef THROTTLE_ACTUATOR_DRIVER_H
#define THROTTLE_ACTUATOR_DRIVER_H

#include <stdint.h>
#include <stdbool.h>

#define THROTTLE_MIN_DUTY_PCT    (0U)
#define THROTTLE_MAX_DUTY_PCT    (100U)
#define THROTTLE_MAX_ADC_RAW     (4095U)

typedef struct {
    uint16_t primary_tps_adc;
    uint16_t secondary_tps_adc;
    uint8_t  duty_cycle_applied;
    bool     plausibility_error;
    bool     limp_home_active;
} ThrottleStatus_t;

void Throttle_Init(void);
void Throttle_UpdateSensors(uint16_t tps1, uint16_t tps2);
bool Throttle_CheckPlausibility(void);
void Throttle_SetActuatorPwm(uint32_t calculated_duty);
void Throttle_KickWatchdog(void);

#endif /* THROTTLE_ACTUATOR_DRIVER_H */
