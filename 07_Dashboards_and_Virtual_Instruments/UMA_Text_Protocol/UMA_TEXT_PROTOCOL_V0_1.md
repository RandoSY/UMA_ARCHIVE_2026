# UMA Text Protocol v0.1 — Draft

## Purpose

The UMA Text Protocol is a simple plain-text command and telemetry pattern for low-cost classroom instruments, robots, dashboards, and wearable prototypes.

It is intended to be readable by humans, easy to log, and simple enough for small microcontrollers.

## Design goals

- Human-readable.
- Easy to test with a serial terminal.
- Works over USB serial, WebSerial, BLE NUS, and simple socket bridges.
- Suitable for low-rate educational telemetry.
- Friendly to CSV, JSON, dashboards, and Python notebooks.

## Command verbs

| Command | Meaning |
|---|---|
| `HELLO` | Identify the device and protocol version. |
| `STATUS` | Report current state. |
| `START` | Begin a measurement or run. |
| `STOP` | Stop a measurement or run. |
| `STREAM` | Enable or configure streaming. |
| `TARE` | Zero a scale or baseline measurement. |
| `CAL` | Calibrate or enter calibration mode. |
| `DEMO` | Run a simulated/demo data mode. |
| `SET RATE` | Set sample or update rate. |

## Message classes

| Prefix | Meaning | Example |
|---|---|---|
| `DEVICE` | Identity information | `DEVICE,name=PicoScale,fw=0.1.0,proto=UMA-TEXT-0.1` |
| `STATUS` | Device status | `STATUS,state=idle,battery=3.91` |
| `DATA` | Measurement data | `DATA,t=1.25,temp_C=24.8,mass_g=102.3` |
| `ERROR` | Recoverable or fatal problem | `ERROR,code=SENSOR_MISSING,msg=No HX711 detected` |
| `EVENT` | Discrete event | `EVENT,type=button_press,t=3.42` |

## Minimal session

```text
> HELLO
DEVICE,name=ExampleNode,fw=0.1.0,proto=UMA-TEXT-0.1
STATUS,state=idle

> START
STATUS,state=running
DATA,t=0.00,value=12.3
DATA,t=1.00,value=12.5

> STOP
STATUS,state=idle
```

## Transport notes

### USB Serial / WebSerial

Send complete lines ending in newline. Keep data human-readable and terminal-friendly.

### BLE NUS

Keep notification chunks small. For conservative compatibility, design for short messages and split longer lines if needed.

### Wi-Fi / WebSocket

Use the same message format where possible so the dashboard logic can remain similar across transports.

## Current status

Draft. Use for prototypes and documentation, but expect refinements.

## Next action

Create one working example each for: scale, frequency meter, robot telemetry, and SQM+ mock data.
