// Include MicroPython API.
#include "py/runtime.h"

// For the list stuff
#include "py/obj.h"

extern mp_obj_t trigger_readings(mp_obj_t read_for_time_ms);
extern mp_obj_t read_batch(mp_obj_t batch_size, mp_obj_t offset);