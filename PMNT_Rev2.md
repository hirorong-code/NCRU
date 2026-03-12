# Phase Mapping Network Theory (PMNT) Rev.2.0
## A Relational Reformulation: Edges as First Principles

---

## Abstract

We present a fundamental revision of Phase Mapping Network Theory (PMNT).
The central postulate is shifted from node-centric to edge-centric:
**relations (φ_{ij}) are primary; points (φ_i) are derived.**

This resolves three open problems in Rev.1.12:
1. The undefined scale σ in C_{ij}
2. The circular use of geometry in deriving geometry
3. The disconnect between C_{ij} and quantum entanglement

Spacetime, gravity, and conservation laws emerge from the dynamics
of a relational network of **Narrowest Computational Resource Units (NCRU_{ij})**,
where each unit is an edge, not a node.
The metric is derived — not assumed.
Singularities are forbidden by construction.

---

## 1. Motivation: Why Relations Must Be Primary

### 1.1 The Problem with Node-Centric Formulation (Rev.1.12)

Rev.1.12 defined the fundamental unit as:

$$NCRU_i = \{\phi_i, \mathcal{N}_i, R_i\}$$

This contains a hidden assumption: **nodes exist before relations.**

But in network theory, a graph is defined by its edges.
Nodes are simply where edges meet.
To define φ_i before φ_{ij} is to smuggle in geometry
before deriving it.

### 1.2 The Physical Argument

Three facts motivate the relational shift:

**Fact 1 — Quantum mechanics:**
The entangled state |ψ_D⟩ = (|eg⟩ - |ge⟩)/√2
cannot be assigned individual phases φ_1, φ_2.
The phase φ_{12} = arg(ρ_{eg,ge}) belongs to the *pair*, not to either node.

**Fact 2 — No isolated nodes:**
PMNT's No-Erasure Lemma states f_min > 0.
A node with zero connections has no clock, no updates, no existence.
Nodes only exist by virtue of their relations.

**Fact 3 — Concurrence as C_{ij}:**
Simulations (L27–L29) confirm that C_{ij} corresponds to
quantum concurrence — a property of pairs, not of individuals.

### 1.3 The Postulate

> **The universe is a network of relations.**
> Points are intersections of relations.
> Relations are not between points — points emerge from relations.

---

## 2. Revised Definitions

### Definition 1: Relational NCRU

The fundamental unit of the universe is a relation:

$$NCRU_{ij} = \{\phi_{ij},\; R_{ij}\}$$

- **φ_{ij} ∈ [0, 2π)**: Relational phase — the entanglement phase between nodes i and j
  - Physical realization: φ_{ij} = arg(ρ_{eg,ge})
  - This is the off-diagonal phase of the two-node density matrix
- **R_{ij} ∈ (0, 1)**: Relational resource — the concurrence (entanglement capacity)
  - R_{ij} = C(i,j) = 2|ρ_{eg,ge}|
  - Bounded: R_{ij} < 1 (No-Erasure), R_{ij} > 0 (no complete separability)

**Note:** Both bounds are strict open intervals.
This is the edge-level expression of "physics has no zeros."

### Definition 2: Derived Node

A node i is defined as the intersection of its relations:

$$\phi_i \equiv \frac{\sum_j R_{ij}\, \phi_{ij}}{\sum_j R_{ij}}$$

This is a weighted average — a derived quantity, not a primary one.

### Definition 3: Correlation Measure (Revised)

The mutual information potential is:

$$C_{ij} \equiv R_{ij} = \text{concurrence}(i,j)$$

No σ parameter. No distance assumption. No circularity.
The correlation *is* the relational resource.

### Definition 4: Effective Degree

The effective connectivity of node i:

$$\deg_{\text{eff}}(i) \equiv \sum_j C_{ij} = \sum_j R_{ij}$$

This is bounded above by the monogamy of entanglement (CKW inequality):

$$\sum_j R_{ij}^2 \leq 1$$

---

## 3. First Principle: Minimal Relational Action

### Theorem 1: Minimal Relational Load Principle

System evolution selects the configuration that minimizes
the total relational action:

$$I = \sum_{(i,j)} R_{ij} \cdot \mathcal{L}(\phi_{ij},\, \nabla\phi_{ij})$$

$$\delta I = 0$$

The variational object is the **relational network structure**,
not the trajectory of a point particle.

**Lemma 1.1:** In the macroscopic limit (deg_eff → ∞),
this reduces to the geodesic equation of General Relativity.

---

## 4. Emergent Metric from Relations

### Definition 5: Relational Distance

Distance is derived from relational resources:

$$d(i,j) \equiv -\log C_{ij} = -\log R_{ij}$$

- C_{ij} = 1 (maximal entanglement) → d = 0 (same point)
- C_{ij} → 0 (no entanglement) → d → ∞ (infinite separation)

**No metric tensor is assumed. Distance emerges from entanglement structure.**

### Theorem 2: Emergent Metric Tensor

In the continuum limit, the line element:

$$ds^2 = \sum_{(i,j)} (-\log C_{ij})\; d\phi_{ij}^2$$

defines an effective metric tensor g_μν as the Hessian of
the relational cost functional.

**Corollary 2.1 (Gravitational Redshift):**
$$f_{\text{obs}} = f_{\text{emit}} \sqrt{g_{00}}$$
Clock rates reflect local deg_eff:
high deg_eff (dense relations) → slow clock → gravitational time dilation.

---

## 5. No-Erasure and No-Zero: The Symmetric Bound

### Theorem 3: Symmetric Boundary Conditions

$$0 < R_{ij} < 1 \quad \forall (i,j)$$

- **Lower bound (No-Zero):** Complete separability R_{ij} = 0 is unreachable.
  A relation with zero resource carries zero information — but "zero information"
  is itself information (a boundary condition on the network).
  Therefore R_{ij} = 0 is forbidden, not absent.

- **Upper bound (No-Erasure):** Complete entanglement R_{ij} = 1 is unreachable.
  This is the edge-level statement of f_min > 0.

**Physical consequence:**
All probabilities p = R_{ij}² lie in the open interval (0,1).
The spectrum of the universe never touches its endpoints.

---

## 6. Minimum Resolvable Probability

### Definition 6: p_min

The minimum resolvable probability for node i:

$$p_{\min}(i) = \frac{\pi^2}{\deg_{\text{eff}}(i)^2}$$

This follows from the phase resolution:

$$\delta\phi_{\min} = \frac{2\pi}{\deg_{\text{eff}}(i)}$$

$$p_{\min} = \sin^2\!\left(\frac{\delta\phi_{\min}}{2}\right) \approx \left(\frac{\delta\phi_{\min}}{2}\right)^2 = \frac{\pi^2}{\deg_{\text{eff}}^2}$$

**The boundary between "tractable" and "intractable" regions
is set by deg_eff — which is itself determined by the network.**

### Corollary 6.1: Planck Scale as Minimum Degree

At the Planck scale, deg_eff → 1 (minimum connectivity):

$$p_{\min}^{\text{Planck}} = \pi^2 \approx 10$$

Below this scale, probability loses meaning.
The Planck length is not an external input — it is the scale
at which the network becomes too sparse for computation.

---

## 7. Gravity as Relational Density Gradient

### Theorem 4: Gravity = Gradient of φ_{ij} Density

Mass concentrations increase local relational density:

$$\rho_{\text{relation}}(x) = \sum_{j \in \mathcal{N}(x)} R_{xj}$$

Gravity is the gradient of this density:

$$\vec{g} \propto -\nabla \rho_{\text{relation}}$$

Objects move toward regions of higher relational density
because that is the path of minimal relational action (Theorem 1).

**Corollary 4.1 (Singularity Resolution):**
A singularity would require R_{ij} = 1 for all neighboring pairs.
But R_{ij} < 1 always (No-Erasure).
Therefore gravitational singularities do not exist in PMNT.

---

## 8. Conservation Laws

### Theorem 5: Conservation of Total Relational Resource

$$\frac{d}{dt}\sum_{(i,j)} R_{ij} = 0$$

Total concurrence is conserved under unitary evolution.
Energy conservation is the macroscopic limit of this constraint.

### Theorem 6: Recovery of Lorentz Invariance

Statistical isotropy of the relational network in the continuum limit
gives rise to effective Lorentz invariance.

**Note:** This is a stronger statement than Rev.1.12.
Isotropy is not assumed — it follows from the symmetry of
the entanglement monogamy constraint (CKW inequality).

---

## 9. Connection to PMNT Hardware (GEN1–GEN3)

The abstract relational structure has a direct physical implementation:

| PMNT Theory | Physical Realization |
|-------------|----------------------|
| NCRU_{ij} | NV center pair in diamond lattice |
| φ_{ij} | arg(ρ_{eg,ge}) — entanglement phase |
| R_{ij} | concurrence C(i,j) |
| deg_eff(i) | Σ_j C(i,j) from cavity QED |
| p_min(i) | π²/deg_eff² |
| d(i,j) | -log C(i,j) |

**GEN1 (ROM):**
Fixed network topology (vacancy placement).
R_{ij} determined by inter-NV distance.
deg_eff fixed at fabrication.

**GEN2 (Cavity QED, 77K):**
Dynamic φ_{ij} generation via Tavis-Cummings coupling.
Dark state |ψ_D⟩ confirmed: C(1,2) = 0.50 (L27).
φ_{12} = π/2, d(1,2) = log 2 = 0.693.

**GEN3 (Computational, target):**
Design condition J/κ > 13 (L29) ensures:

$$\deg_{\text{eff}} > \deg_{\text{eff}}^{\min} \implies p_{\min} < p_{\min}^{\text{threshold}}$$

This is the engineering condition for "tractable region" access —
the hardware condition that φ_{ij} survives long enough
to be read out as computation.

---

## 10. Summary: What Changed from Rev.1.12

| | Rev.1.12 | Rev.2.0 |
|--|----------|---------|
| Fundamental unit | Node (φ_i) | Edge (φ_{ij}) |
| C_{ij} definition | exp(-\|φ_i-φ_j\|²/σ²) | concurrence R_{ij} |
| σ parameter | Undefined | Eliminated |
| Metric origin | Assumed (g_μν) | Derived (-log C_{ij}) |
| Geometry role | Primary | Secondary (derived) |
| Singularities | Problematic | Forbidden (R_{ij}<1) |
| Lorentz invariance | Assumed (statistical) | Derived (CKW symmetry) |
| p_min | Not defined | π²/deg_eff² |
| Hardware connection | Indirect | Direct (L27–L29) |

---

## 11. Open Questions

```
1. φ_{ij} の動力学方程式
   dφ_{ij}/dt = ?
   Lindblad方程式との対応は？

2. CKW不等式の宇宙論的含意
   Σ_j R_{ij}² ≤ 1 が
   エネルギー保存と同値か？

3. プランク長の導出
   deg_eff = 1 が ℓ_P に対応する
   具体的な計算

4. 暗エネルギーの解釈
   宇宙膨張 = deg_eff の時間的減少？
   = R_{ij}の希薄化？
```

---

## Appendix A: Comparison with Existing Approaches

| Approach | Primary Entity | PMNT Difference |
|----------|---------------|-----------------|
| GR | Spacetime manifold | Relations precede geometry |
| Loop Quantum Gravity | Spin networks (nodes+edges) | Edges only; nodes derived |
| It from Bit (Wheeler) | Binary information | Continuous phase φ_{ij} |
| Holography | Boundary area | deg_eff as bulk-boundary map |
| Causal Sets | Partial order of events | Weighted relations (R_{ij}) |

---

## Appendix B: Hardware Validation Summary (L27–L29)

```
L27: 暗状態形成
  C(1,2) = 0.50（concurrence）
  φ_{12} = π/2
  → NCRU_{12}の物理的存在を確認

L28: J_{ij}の相関への刻印
  Δ_inv = +0.25 at s=0
  → φ_{ij}がH_costを瞬間的に反映
  → kT/J=1600で消滅（GEN2の限界）

L29: GEN3設計条件
  J/κ > 13 → Δ_inv(s=1) > 0.15
  → deg_eff > 閾値でp_min < p_threshold
  → 「取り扱える領域」の工学的確保
```

---

*PMNT Rev.2.0 — Relations First*
*GEN1–GEN3 hardware program: Physical implementation of φ_{ij}*
