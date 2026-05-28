# Singing Ruler — One-Pager

**Pillar:** Measured World

## One-sentence purpose

The Singing Ruler turns a simple clamped ruler into an instrumented cantilever oscillator, making damping, frequency, ODE behavior, FFT, and the mathematical soul of motion visible.

## Who it serves

- Students beginning physics through visible motion.
- Teachers seeking a low-cost bridge from hands-on measurement to ODEs and signal analysis.
- Makers using IMUs and dashboards to expose hidden motion.
- Learners who need a concrete path from object, to waveform, to model.

## Where it happens

A desk, table, bench, classroom, or home lab. The physical setup can be simple: clamp one end of a ruler, attach or hold an IMU-bearing device near the free end, deflect, release, and record motion.

## What it measures

| Measurement | Meaning |
|---|---|
| Acceleration | Motion of the ruler tip over time. |
| Frequency | Dominant oscillation rate. |
| Damping | How the motion fades. |
| Phase / timing | When peaks occur. |
| FFT spectrum | Frequency content of the vibration. |

## Hardware candidates

- M5StickC Plus2 / M5StickC-class IMU device.
- Ruler or thin beam.
- Clamp or vise.
- BLE / USB / dashboard connection.
- Optional phone/camera for visual reference.

## Learning path

```text
see the ruler move → record acceleration → graph waveform → find peaks → estimate period → estimate damping → compare model
```

## Mathematical soul

The humble ruler reveals a deep structure: constrained motion that can be described, measured, modeled, and compared. The motion is simple enough to see and rich enough to lead toward differential equations and eigenmodes.

## Why it matters

The Singing Ruler is a premier UMA instrument because it shows how a familiar object can become a serious mathematical instrument when measurement is attached to it.

## Current status

Working flagship concept. Needs a clean first experiment packet with setup photos, sample CSV, waveform plot, FFT plot, and student questions.

## Next action

Create `experiment_001_basic_decay/` with procedure, data table, dashboard screenshot, and analysis notes.
