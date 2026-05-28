# 555 + 7400 Monte Carlo Duty-Cycle Lab — One-Pager

**Pillar:** Measured World / Measured Machine

## One-sentence purpose

This lab uses a 555 timer, a 7400 NAND latch, and repeated one-bit samples to show how statistics can reconstruct a hidden duty cycle.

## Core sentence

```text
The 555 makes time; the 7400 remembers a one-bit sample; statistics reconstruct the hidden pulse width.
```

## Who it serves

- Students meeting probability through a real physical signal.
- Teachers who want a concrete introduction to Bernoulli and binomial reasoning.
- Embedded learners connecting chips, logic, timing, data, and dashboards.
- Makers who want a serious lab from very simple parts.

## What it measures

The hidden quantity is duty cycle:

```text
D = high time / total period
```

A one-bit sample can only say whether the waveform was HIGH or LOW at the instant it was captured. Repeated random samples reveal the proportion of time the signal spends HIGH.

## Why binomial appears

Each sample has two outcomes:

```text
HIGH or LOW
```

If the sampling is random relative to the waveform, the count of HIGH samples out of `n` trials follows a binomial pattern. The estimated duty cycle is:

```text
p_hat = number_of_high_samples / n
```

## Learning ladder

1. Observe a 555 waveform.
2. Capture one-bit HIGH/LOW states with a latch.
3. Record repeated samples.
4. Count HIGH samples.
5. Estimate duty cycle.
6. Show uncertainty shrinking as sample size grows.
7. Connect hardware sampling to Monte Carlo reasoning.

## Why it matters

This lab turns old chips into a rigorous probability instrument. It gives students a physical reason for the binomial distribution instead of presenting it as a detached formula.

## Current status

Draft / high-value curriculum concept.

## Next action

Create three versions: console-only simulation, breadboard hardware lab, and browser dashboard lab.
