---
keywords:
    - esp32
    - powerfeather
    - sdk
    - api
    - mainboard
    - power management
    - power monitoring
sidebar_position: 2
---

# Result

## enum class Result

- `Ok` Operation succeeded.
- `Failure` Operation unspecified failure.
- `InvalidState` Operation is not allowed given current internal state.
- `Timeout` Operation took longer than expected.
- `InvalidArg` Operation argument out of range or invalid.
- `NotReady` Unable to complete operation at this time.
- `LockFailed` Exclusive resource lock acquisition by operation failed.
