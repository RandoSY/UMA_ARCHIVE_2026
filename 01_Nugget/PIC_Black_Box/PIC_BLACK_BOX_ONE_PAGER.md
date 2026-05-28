# PIC Black Box — One-Pager

**Pillar:** Measured Machine / Nugget

## One-sentence purpose

PIC Black Box uses a small, low-cost PIC microcontroller as an inspectable programmable black box for timing, sensing, serial reporting, and machine-literacy learning.

## Who it serves

- Beginning embedded learners who need a small, understandable target.
- Teachers introducing machine behavior without overwhelming hardware.
- Makers who want close-to-the-metal control with a low-cost DIP part.
- Nugget / REDBoard Revival work that needs a small edge processor.

## Where it happens

Breadboard, Gooligum-style low-pin-count board, REDBoard/Nano bridge bench, MPLAB X / VS Code workstation, or classroom hardware station.

## Hardware focus

- PIC16F18424 / PIC16F18426 / related enhanced mid-range PICs.
- 14–18 pin DIP devices preferred for manageability.
- SNAP debugger/programmer path.
- External 5 V target power where appropriate.
- LVP and reset behavior documented.

## Toolchain focus

- Great Cow BASIC for readable source.
- Generated assembly as an educational artifact.
- MPLAB X / VS Code for build and debug.
- PIC-AS / XC8 awareness for modern Microchip workflows.
- UART output as the first honest instrument.

## Core teaching move

The PIC can be taught as a **programmable 555**:

```text
timing + thresholds + events + code + serial messages
```

## Why it matters

PIC Black Box gives Nugget a real machine-level core. Students can start with readable BASIC, see generated assembly, debug on real hardware, and learn that a black box can be opened.

## Current status

Working hardware/software path. SNAP and PIC16F18424-class hardware have been validated in the broader project work.

## Next action

Create a first reproducible project: blink / UART hello / simple sensor report, with source, generated assembly note, build steps, and wiring diagram.
