# Tapeless Ruler — One-Pager

**Pillar:** Measured World

## One-sentence purpose

The Tapeless Ruler uses ultrasonic or time-of-flight sensing to measure distance without a physical tape, making spatial measurement, calibration, uncertainty, and geometry visible.

## Who it serves

- Students learning distance, scale, and error.
- Teachers who want a simple instrument that turns a room into a measurement field.
- Robot EDU work that needs distance sensing before navigation.
- UMA instrument builders connecting sensors, dashboards, and physical meaning.

## Where it happens

Classroom, hallway, kitchen, workshop, robot arena, or any space with clear targets and known reference distances.

## What it measures

| Measurement | Meaning |
|---|---|
| Distance | Estimated range to a target or surface. |
| Repeatability | How stable the reading is across trials. |
| Calibration error | Difference from known reference distance. |
| Target dependence | How surface, angle, and reflectivity affect readings. |
| Field geometry | Space as measurable structure. |

## Hardware candidates

- HC-SR04 ultrasonic sensor.
- VL53L0X / VL53L1X time-of-flight sensor.
- Pico W, Arduino Nano, ESP32, or micro:bit v2.
- Optional OLED or browser dashboard.

## Learning loop

```text
estimate distance → measure with sensor → compare to physical ruler/tape → calibrate → repeat → graph error
```

## Why it matters

The Tapeless Ruler bridges Measured World and Robot EDU. The same act of measuring distance across a table can become robot mapping, hallway navigation, and spatial reasoning.

## Current status

Prototype / flagship concept. Needs a clean comparison lab between physical ruler, ultrasonic sensing, and ToF sensing.

## Next action

Create a first lab packet: `known_distance_calibration/` with a 0.25 m to 2.0 m reference table and graphing activity.
