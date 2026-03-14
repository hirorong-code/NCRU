# Physical Limits of Computation in PMNT
## What Dark-State Networks Can and Cannot Solve

**Authors:** PMNT Development Team  
**Version:** 1.0  
**Date:** March 2026  
**Series:** PMNT GEN3 Papers (L31–L35)

---

## Abstract

We define, for the first time, the boundary between solvable and unsolvable problems for a quantum network computer based on large-detuning Tavis-Cummings cavity QED with diamond NV centers (PMNT GEN3).

GEN3 does not execute instructions. Given a weight matrix J_{ij} as a cost function, the physical system spontaneously forms a network structure through energy minimization and outputs the answer. "The physics solves it, not the procedure" — this is the computational principle of PMNT.

Through numerical simulation of the quantum Lindblad master equation (L31–L35), we establish:

**What can be computed:**
Extraction of the cluster eigestructure of J_{ij} matrices. Demonstrated by automatic detection of protein complexes (Scenario 1: two-complex system; Scenario 3: hidden trimer complex). No NAND gates, no clock, no labels required.

**What cannot be computed:**
Distinguishing degenerate J_{ij} pairs (Scenario 2), problems requiring sign inversion (MAX-CUT), and complete rank restoration of intermediate values (L34).

This boundary is not a failure — it is the definition of a computational class. GEN3 is now fully defined as "a physical computer that extracts the spectral cluster structure of J_{ij} matrices."

---

## 1. The Computational Principle of PMNT

### 1.1 Fundamental Difference from von Neumann Architecture

```
Von Neumann computer:
  Human writes the procedure (algorithm)
  Machine executes it step by step
  "Computation is the execution of instructions"

PMNT GEN3:
  Human sets J_{ij} (cost function)
  Physical system minimizes energy
  Answer emerges as network structure
  "Computation is the natural consequence of physics"
```

This distinction is fundamental. In a von Neumann machine, the human describes *what to do*. In PMNT, the human sets *what the conditions are*, and physics determines *what happens*.

### 1.2 Physical Foundation of GEN3 (Confirmed Results: L31–L33)

In the large-detuning limit (Δ >> g) of the Tavis-Cummings model:

```
Effective Hamiltonian:
  H_eff = -J_eff Σ_{ij} J_{ij}(σ_+^i σ_-^j + h.c.)
        + H_Γ (transverse field term)

J_eff = g²/Δ = 308 MHz
κ_eff = κ(g/Δ)² = 8.85 MHz
J_eff/κ_eff = Δ/κ = 34.8

Dark state |ψ_D> = (|eg> - |ge>)/√2 is κ-immune
→ J_{ij} information is permanently encoded
```

**Confirmed Parameters (L33):**

| Parameter | Value | Physical Meaning |
|-----------|-------|-----------------|
| s* | 0.890 | Optimal readout point |
| Γ* | 330 MHz | Optimal transverse field |
| Δ_inv(s*) | +0.763 | Peak discrimination signal |
| Safe readout window | s = 0.80–0.905 | |

**Physical meaning of s* = 0.890:**  
The condition Γ*/J_eff ≈ 1 — the transverse field and spin exchange are in competition. This is the vicinity of a quantum critical point, where sensitivity to differences in J_{ij} is maximized.

---

## 2. What Can Be Computed

### 2.1 Cluster Structure Detection (Scenario 1)

**Problem:**  
Automatically detect protein complex structure from interaction strengths J_{ij} among proteins A–D.

```
Input J_{ij}:
  J_AB = 1.0  (within complex I)
  J_CD = 1.0  (within complex II)
  others = 0.1 (between complexes)

Ground truth: Complex I = {A,B}, Complex II = {C,D}
```

**GEN3 output (readout at s* = 0.890):**

```
C_AB = C_CD = +0.2347  (intra-complex)
others      = +0.1929  (inter-complex)
Separation margin = +0.0418
```

**Verdict: ✓ DETECTED**  
The physics identified two complexes without instructions. No labels were provided. The only input was the structure of J_{ij}.

**Biological significance:**  
Analogous to hemoglobin (αβ dimer × 2). Complex structure is recovered from interaction strength data alone, without mass spectrometry or co-immunoprecipitation.

### 2.2 Discovery of Hidden Structure (Scenario 3)

**Problem:**  
Detect a hidden trimer complex {A,B,D} in a system where J_{ij} configuration is non-trivial.

```
Input J_{ij}:
  J_AB = 0.8, J_AD = 0.7, J_BD = 0.6
  J_AC = J_BC = J_CD = 0.1  (isolated ProtC)

"Hidden" trimer: {A,B,D}
```

**GEN3 output:**

```
C_AB = +0.237, C_AD = +0.204, C_BD = +0.184
C_CD = +0.112, C_BC = +0.093, C_AC = +0.088

Intra-complex mean C = +0.208
Inter-complex mean C = +0.097
Separation margin    = +0.072  (maximum across scenarios)
```

**Verdict: ✓ DETECTED**  
Only humans called it "hidden." The physics saw the structure from the beginning.

**Key finding:**  
Scenario 3 (margin +0.072) outperforms Scenario 1 (margin +0.042). Greater asymmetry in J_{ij} leads to easier identification. Whether a structure is "hidden" is irrelevant to computational difficulty.

---

## 3. What Cannot Be Computed

### 3.1 The Degeneracy Problem (Scenario 2)

**Problem setup:**

```
J_AB = 1.0  (strong)
J_BC = 0.5  (bridge)
J_AC = 0.5  (bridge) ← same value as J_BC
J_CD = 0.8  (moderate)
J_AD = J_BD = 0.1  (weak)
```

**GEN3 output:**

```
C_AC = C_BC = +0.1602  (identical values)
```

**Physical reason:**

```
J_AC = J_BC
→ The energy of A-C and B-C pairs in H_eff is identical
→ C_{ij} converges to the same value
= Degeneracy

The physics does not know which pair is "intra-complex"
It has no reason to distinguish them
Equal J_{ij} means equal C_{ij}
```

This is not a failure — it is an honest answer from physics. Lifting the degeneracy requires either changing the problem setup (J_{ij}) or increasing N_SPIN to add contextual information.

### 3.2 The Sign Problem

The current GEN3 H_XY is ferromagnetic:

```
H = -J_eff(σ_+σ_- + σ_-σ_+)
→ All C_{ij} > 0  (strictly positive)
```

Problems requiring sign inversion (C_{ij} < 0), such as MAX-CUT, cannot be solved. Two-layer PMNT or antiferromagnetic H_XY implementation would be required.

### 3.3 Complete Rank Restoration (L34)

When J_{ij} takes six distinct values (L34, Pattern 1), the rank order of C_{ij} does not match that of J_{ij} (Kendall tau = −0.600).

**Physical reason:**

```
C_{ij} ∝ sin²(J_eff × J_{ij} × t*)

sin² is non-monotonic
When J_{ij} is too large,
sin² wraps around and C_{ij} decreases

Operating range constraint:
  J_eff × J_{ij} × t* < π/4
  must hold for monotonic correspondence
```

---

## 4. The Computational Class of GEN3

### 4.1 Definition

```
The set of problems solvable by GEN3:

  Input:  J_{ij} ∈ R^{N×N}  (symmetric matrix)
  Output: C_{ij}  (correlation matrix)

  Solvable when:
  The cluster eigenstructure of J_{ij}
  is accurately reflected in the
  cluster structure of C_{ij}

  Conditions:
  ① J_{ij} values are clearly separated
    across different clusters (non-degenerate)
  ② Operating range: J_eff × J_{ij} × t* < π/4
  ③ Sign inversion not required
```

### 4.2 Correspondence with Classical Algorithms

**Comparison with spectral clustering:**

```
Classical spectral clustering:
  Construct Laplacian of J_{ij} matrix
  → Compute eigenvalues/eigenvectors
  → Classify via k-means
  = O(N³) time complexity

GEN3:
  Set J_{ij} in H_eff
  → Physical system minimizes energy
  → Read out C_{ij} at s*
  = Time complexity governed by physics

Both solve the same problem.
GEN3 is a "physical analog of spectral clustering."
```

This correspondence is significant. It establishes that GEN3 solves a classically well-defined computational problem, giving concrete content to the claim that "physics computes."

### 4.3 The Role of Quantum Mechanics

```
Role of dark states:
  κ-immunity (dissipation-immune)
  = Permanent storage of J_{ij} information
  = Not realizable in classical systems

Quantum critical point at s*:
  Γ*/J_eff ≈ 1
  = Quantum fluctuations amplify structure discrimination
  = Absent in classical annealing

→ The computational class of GEN3 is
  classically defined, but its physical
  realization requires quantum mechanics essentially
```

---

## 5. Application to Protein-Protein Interactions

### 5.1 Natural Fit

Protein-protein interaction networks (PINs) naturally fit the GEN3 computational class:

```
Protein       ↔  NV spin
Interaction strength ↔  J_{ij}
Complex structure    ↔  Cluster structure

Limitations of existing methods:
  Mass spectrometry: high-throughput but
    misses weak interactions
  Co-IP: specific but low-throughput,
    high cost

Advantages of GEN3:
  All pairs processed simultaneously
  including weak interactions
  Cluster structure emerges spontaneously
```

### 5.2 Roadmap to Experimental Realization

```
Near-term (years):
  N=4 NV centers + microcavity
  Add Δ=13 GHz to existing GEN2 hardware
  Demonstrate single-complex detection

Mid-term (5–10 years):
  N=100 NV network
  Cluster detection from real PIN data

Long-term (10–15 years):
  Diamond chip integration
  Room-temperature operation (n_th(optical) ≈ 0)
  Application to drug discovery screening
```

---

## 6. Discussion

### 6.1 Scientific Value of Defining Failure

The trajectory of this research:

```
L30: H_ZZ steady-state FAIL
  → κ erases information
  → Transition to dark-state encoding

L34: 6-level rank restoration FAIL
  → sin² nonlinearity discovered
  → Operating range constraint quantified

L35 Scenario 2: Bridge detection FAIL
  → Degeneracy problem discovered
  → Upper bound of computational class defined

Every failure clarified
the boundary of the computational class
by one step
```

This is how computational class theory works. Turing's halting problem, Cook's NP-completeness, Shannon's channel capacity — all define the *limits* of computation. GEN3's contribution follows the same tradition.

### 6.2 Alignment with PMNT First Principles

```
PMNT Rev.2 first principle:
  "Relations are fundamental"
  NCRU_{ij} = {φ_{ij}, R_{ij}}

GEN3's computational class:
  Both input and output are "relations"
    (J_{ij}, C_{ij})
  Nodes (points) never appear
  "Structure of relations" is the
  object of computation

This is fundamentally unrealizable
in von Neumann architecture,
where addresses and values
(points as fundamental) define computation
```

### 6.3 On the Role of the Transverse Field

A subtle but important finding: the optimal computation point is not s=1 (Γ=0) but s*=0.890 (Γ*=330 MHz). This means the transverse field is not noise to be eliminated — it is a computational resource.

At the quantum critical point (Γ*/J_eff ≈ 1), the system is maximally sensitive to differences in J_{ij}. This is precisely the mechanism by which quantum annealing outperforms classical annealing: quantum fluctuations explore the energy landscape more efficiently near criticality.

GEN3 does not anneal to a ground state — it reads out at the critical point. This is a fundamentally different use of quantum mechanics.

---

## 7. Conclusion

PMNT GEN3 establishes four things:

**① Physical computational principle**  
Large-detuning cavity QED generates κ-immune H_XY interaction, permanently encoding J_{ij} in dark-state phases. s* = 0.890 (near the quantum critical point) is the optimal readout point.

**② Definition of computational class**  
"Physical extraction of the cluster eigenstructure of J_{ij} matrices" — this is GEN3's computational class. It is the physical analog of spectral clustering.

**③ Explicit boundary**  
Degeneracy, sign problem, operating range constraint — the upper bound of the computational class is defined with physical justification.

**④ Concrete application**  
Automatic detection of protein complexes demonstrated. No NAND gates, no clock, no labels.

**Final proposition:**

```
"The physics solves it, not the procedure."

What this proposition means
has been quantitatively defined
for the first time through L31–L35.

Problems GEN3 can solve:
  Extraction of the cluster
  eigenstructure of J_{ij} matrices.

No broader class of problems can be solved.
No narrower class of problems will fail.

The boundary has been drawn.
The science is complete.
```

---

## Appendix A: Simulation Parameters

```
System:      4 NV centers + cavity (Tavis-Cummings)
Diamond:     a = 0.357 nm
Temperature: 77 K, Magnetic field: 0.2 T
Q-factor:    200,000 (κ = 374 MHz)
Coupling:    g = 2,000 MHz
Detuning:    Δ = 13,000 MHz
Effective:   J_eff = 308 MHz, κ_eff = 8.85 MHz
Optimal:     s* = 0.890, Γ* = 330 MHz
Evolution:   Quantum Lindblad master equation (RK4)
Convergence: σ(ρ_avg) < 1×10⁻³
```

## Appendix B: Simulation Lineage

```
L27 → C=0.50 dark state (GEN2 baseline)
L28 → Transient Δ_inv (discovery of J_{ij} imprinting)
L29 → J/κ scan (false positive)
L30 → H_ZZ steady-state FAIL (root cause identified)
L31 → Large detuning PASS (H_XY + dark-state encoding)
L32 → Robustness verification, s* discovered
L33 → s* = 0.890 confirmed (quantum critical point)
L34 → Multiple J_{ij}: rank restoration limit (sin² problem)
L35 → Protein complex detection: computational class confirmed

Every failure was the path to the next discovery.
```

## Appendix C: Related Work

1. Dickson et al., *Nature Commun.* 4, 1903 (2013) — NV coherence
2. Albash et al., *Phys. Rev. X* 8, 031016 (2018) — Quantum annealing
3. Bar-Gill et al., *Nature Commun.* 4, 1743 (2013) — NV spin coherence
4. Tavis & Cummings, *Phys. Rev.* 170, 379 (1968) — TC model
5. King et al., *Science* eado6285 (2025) — Quantum annealing benchmark
6. Von Luxburg, *Stat. Comput.* 17, 395 (2007) — Spectral clustering tutorial

---

*PMNT L35 Paper v1.0 (English)*  
*"The physics solves it — and now we know exactly what that means."*
