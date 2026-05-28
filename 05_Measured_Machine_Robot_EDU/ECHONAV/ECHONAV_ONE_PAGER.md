# ECHONAV — One-Pager

**Pillar:** Measured Machine

## One-sentence purpose

ECHONAV is a Robot EDU navigation framework where a robot learns its surroundings through sensing, echo/range, heading, and confidence.

## Who it serves

- Students learning navigation as measurable reasoning.
- Teachers looking for a robotics activity deeper than simple obstacle avoidance.
- Robot builders connecting sensors, dashboards, and decision logic.
- UMA architecture work that bridges Measured Machine and Measured World.

## Where it happens

A simple arena, hallway course, taped floor grid, tabletop box maze, or classroom navigation field.

## Core idea

```text
Sense → Echo → Heading → Confidence → Action
```

A robot should not merely move. It should report what it believes it sees, where it is pointed, how confident it is, and why it chooses the next motion.

## What it measures

| Measurement | Source | Purpose |
|---|---|---|
| Range / echo | ToF, ultrasonic, IR | Estimate distance to walls/objects. |
| Heading | magnetometer, gyro, compass comparison | Know orientation. |
| Motion state | motor command / encoder / timing | Know what the robot is trying to do. |
| Confidence | repeatability / sensor agreement | Know how much to trust the reading. |
| Events | obstacle, turn, stop, target found | Make the behavior reviewable. |

## Dashboard fields

```text
DATA,t=1.25,range_m=0.82,heading_deg=42,confidence=0.87,state=cruise
EVENT,t=1.92,type=obstacle,range_m=0.41,action=turn_left
```

## Why it matters

ECHONAV gives Robot EDU a serious intellectual center: navigation as measurement, uncertainty, validation, and responsible action.

## Current status

Draft framework. Strong candidate for a first Robot EDU dashboard pilot.

## Next action

Create `echonav_demo_001/` with a minimal arena, robot telemetry format, dashboard sketch, and student procedure.
