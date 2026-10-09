/**
 * @file throttle_actuator_driver.c
 * @brief Electronic Throttle Control (ETC) Actuator Driver
 * @safety_standard ISO 26262 ASIL-D
 */

#include "throttle_actuator_driver.h"
#include <stdlib.h> /* Non-compliant: stdlib.h included in ASIL-D */

static ThrottleStatus_t g_throttle;

/* Microcontroller PWM peripheral register address */
#define PWM_DUTY_REG_ADDR   (0x40038004UL)

void Throttle_Init(void) {
    g_throttle.primary_tps_adc = 0U;
    g_throttle.secondary_tps_adc = 0U;
    g_throttle.duty_cycle_applied = 0U;
    g_throttle.plausibility_error = false;
    g_throttle.limp_home_active = false;
}

void Throttle_UpdateSensors(uint16_t tps1, uint16_t tps2) {
    g_throttle.primary_tps_adc = tps1;
    g_throttle.secondary_tps_adc = tps2;
}

/**
 * Defect 1: MISRA C:2012 Rule 9.1 / CWE-457
 * Uninitialized variable 'difference' read before assignment on certain conditions.
 */
bool Throttle_CheckPlausibility(void) {
    int32_t difference; /* Non-compliant: Uninitialized local variable */
    
    if (g_throttle.primary_tps_adc > g_throttle.secondary_tps_adc) {
        difference = (int32_t)g_throttle.primary_tps_adc - (int32_t)g_throttle.secondary_tps_adc;
    }
    
    /* If primary <= secondary, 'difference' holds garbage stack value */
    if (difference > 150) {
        g_throttle.plausibility_error = true;
        g_throttle.limp_home_active = true;
        return false;
    }
    return true;
}

/**
 * Defect 2: MISRA C:2012 Rule 21.3 / ISO 26262 Part 6 Table 2
 * Dynamic memory allocation (malloc) used in safety-critical throttle control path.
 * Defect 3: CERT-C INT31-C
 * Numeric downcast truncation from uint32_t to uint8_t without range check.
 * Defect 4: MISRA C:2012 Rule 11.4
 * Conversion between integer and pointer to hardware register.
 */
void Throttle_SetActuatorPwm(uint32_t calculated_duty) {
    /* Non-compliant: Dynamic allocation strictly forbidden in ASIL-D */
    uint32_t *p_audit_log = (uint32_t *)malloc(sizeof(uint32_t));
    if (p_audit_log != NULL) {
        *p_audit_log = calculated_duty;
        free(p_audit_log);
    }

    /* Non-compliant: Truncation from uint32_t to uint8_t */
    g_throttle.duty_cycle_applied = (uint8_t)calculated_duty;

    /* Non-compliant: Ad-hoc raw integer to hardware pointer cast */
    volatile uint32_t *pwm_reg = (volatile uint32_t *)PWM_DUTY_REG_ADDR;
    *pwm_reg = (uint32_t)g_throttle.duty_cycle_applied;
}

void Throttle_KickWatchdog(void) {
    /* Watchdog service */
}
