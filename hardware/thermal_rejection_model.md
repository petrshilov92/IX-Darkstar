# IX-Darkstar Thermal Rejection Model

This document outlines the zero-convection, radiation-based thermal rejection system used in IX-Darkstar, allowing high-energy operation in the vacuum of space without reliance on traditional atmosphere-based cooling.

---

## 🌌 Environmental Context

- In vacuum, convection and conduction with surrounding air are impossible.
- All excess heat must be rejected via electromagnetic radiation (primarily infrared).
- Radiative cooling performance scales with the fourth power of temperature per Stefan–Boltzmann Law.

---

## 🔥 Heat Generation Profile

Estimated internal thermal output:

| Module                             | Peak Heat Load | Duration         |
|------------------------------------|----------------|------------------|
| Kinetic Impact Pulse Core          | 180 W          | Pulse bursts     |
| Levitation Coil Network            | 90 W           | Sustained        |
| Driver Feedback Controller (ESC)   | 60 W           | Variable         |
| Capacitor Array (losses)           | 40 W           | Brief spikes     |
| TOTAL                              | ~370 W         | Peak combined    |

---

## 🧊 Cooling Solution

### Primary Radiative Dissipation Layer

- Material: Black-anodized aluminum alloy (α > 0.95 emissivity)
- Geometry: Ribbed fin surface with expanded cross-section
- Total surface area: ~0.35 m² (top + side vanes)
- Placement: Bottom-facing passive plate with high thermal conductivity interface

### Radiation Calculation:

Using the Stefan–Boltzmann law:

P = εσA(T⁴ − T₀⁴)

Where:
- P = 370 W (waste heat)
- ε = 0.95 (emissivity of black anodized aluminum)
- σ = 5.67×10⁻⁸ W/m²·K⁴ (Stefan–Boltzmann constant)
- A = 0.35 m²
- T₀ = 3 K (cosmic background)
- Solve for T (radiator temp)

Derived radiator temperature ≈ 480–520 K (207–247°C)

This is within tolerance for space-grade electronics.

---

## 🌀 Optional Upgrades

- Add deployable petal radiators to expand area to 0.9–1.2 m²
- Use flexible graphene thermal straps for faster heat transport
- Integrate phase-change matrix (e.g., paraffin-wax capsule) for burst load absorption

---

## 💡 Tesla-Inspired Redundancy

- Multi-axis radiation pathing (modular panel placement)
- Zero-moving-parts design
- Vacuum-sealed graphite heat pipes (optionally passive loop)

---

## Summary

IX-Darkstar handles thermal rejection entirely via radiative means using high-emissivity passive layers and strategic heat-flow distribution. This design ensures safe long-term operation even during sustained kinetic activity in the vacuum of space—no moving fans, pumps, or liquid loops needed.

> Total system waste heat of ~370W is radiatively rejected via passive surf
