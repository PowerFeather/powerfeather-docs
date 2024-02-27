---
sidebar_position: 2
---


# Result

:::info
Work in progress.
:::

## enum class Result

### Ok = 0

Operation succeeded.

### Failure = -1

Operation failed due to unspecified failure.

### InvalidState = -2

Unable to perform operation due to invalid state.

### Timeout = -3

Operation failed due to timeout.

### InvalidArg = -4

Unable to perform operation due to invalid argument (ex. out of range, wrong value).

### Unsupported = -5

Operation not supported.
