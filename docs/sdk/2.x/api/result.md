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
parse_number_prefixes: false
---

import SdkApiVersionDropdown from '@site/src/components/SdkApiVersionDropdown';

# Result

<SdkApiVersionDropdown page="result" current="2.x" />

## enum class Result

- `Ok` Operation succeeded.
- `Failure` Unspecified operation failure.
- `InvalidState` Operation is not allowed given current internal state.
- `Timeout` Operation took longer than expected.
- `InvalidArg` Operation argument is out of range or invalid.
- `NotReady` Unable to complete operation at this time.
- `LockFailed` Operation failed to acquire an exclusive resource lock.
