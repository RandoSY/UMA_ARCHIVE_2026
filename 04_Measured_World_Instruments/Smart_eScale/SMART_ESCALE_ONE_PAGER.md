# Smart eScale — One-Pager

**Pillar:** Measured World

## One-sentence purpose

The Smart eScale uses a load cell and HX711-class amplifier/ADC to make mass, calibration, tare, uncertainty, and data logging visible in KitchenLab and UMA measurement work.

## Who it serves

- Students learning that mass is measured, calibrated, and uncertain.
- Teachers building low-cost KitchenLab instruments.
- Makers connecting strain gauges, ADCs, microcontrollers, and dashboards.
- UMA projects that need a practical mass/force measurement node.

## Where it happens

Kitchen counter, classroom table, maker bench, calibration station, or embedded-systems lab.

## What it measures

| Quantity | Meaning |
|---|---|
| Raw ADC count | Electrical output from the load-cell/HX711 path. |
| Tare offset | Baseline removed before measuring mass. |
| Calibrated mass | Estimated mass in grams or kilograms. |
| Drift / noise | Stability and repeatability over time. |
| Event data | Tare, calibration, sample, and logging events. |

## Hardware candidates

- Load cell.
- HX711 breakout or M5Stack Mini Scales Unit.
- Pico W, ESP32, Arduino Nano, or PIC/bridge route.
- Browser dashboard through USB serial, WebSerial, BLE NUS, or Wi-Fi.

## Command pattern

```text
HELLO
STATUS
TARE
CAL
START
STOP
DATA,t=0.00,mass_g=102.34,raw=8381200
```

## Why it matters

The Smart eScale is one of the most practical bridges between daily life and serious measurement. It turns food, water, objects, calibration weights, and classroom materials into quantitative evidence.

## Kitech connections

- Density: mass and volume.
- Calorimetry: water mass and temperature change.
- Food/energy studies: measured servings.
- Calibration and uncertainty: repeatability, drift, and tare.
- MKS foundation: grams, milliliters, cubic centimeters, and water.

## Current status

Working flagship concept. Multiple hardware paths are plausible; the archive should separate polished demo route from foundational raw-HX711 route.

## Next action

Create two starter tracks: `packaged_path_m5stack/` and `foundational_path_hx711_breakout/`.
