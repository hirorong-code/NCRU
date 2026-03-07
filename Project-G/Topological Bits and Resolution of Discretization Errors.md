## 2. 英語版 (English Version)

```markdown
# Physical Implementation of Topological Bits and Resolution of Discretization Errors in PMNT L15.7
**― Quantization of $Q$-value via Structural Pinning and Comparison with State-of-the-Art Research ―**

## 1. Introduction: Requirements for a Practical Topological Computer
PMNT L15.7 successfully observed a topological charge of $Q \approx -1.24$ in a spin field utilizing NV center anisotropy. However, for a "bit" as an information element, strict digitality (integer value $Q \in \mathbb{Z}$) is essential to ensure noise robustness and computational reproducibility. This paper discusses methods for defining bits based on physical structures rather than mere numerical adjustments.

## 2. Physical Examination of Observation Results
The current lack of convergence of $Q$ to an integer suggests the following physical conditions:

* **Floating Information State**: While spin vortices (skyrmions) are generated, they maintain "translational symmetry" allowing them to exist anywhere on the grid, making them susceptible to thermal fluctuations and discretization errors.
* **Incomplete Relaxation**: The dissipation constant $alpha = 0.05$ is suitable for write speed (responsiveness) but may be insufficient to fully lock the structure into a ground state.

## 3. Discussion: Introduction of Constraints and Physical Necessity

### 3.1 Dynamic Significance of the Dissipation Constant (alpha)
Re-adjusting energy dissipation is not an accounting fix for calculations but a design of the device's "operating mode." Logic dictates a "write cycle" where low $alpha$ increases sensitivity during high-speed operations, while effective $alpha$ is increased (or constrained by potential) during information latching.

### 3.2 Integer Quantization of $Q$ via Structural Pinning
Constraints to force $Q$ to an integer correspond to the **"introduction of defects"** in real-world devices. By placing local magnetic anisotropy inhomogeneities or geometric nanostructures, skyrmions are "pinned" to specific coordinates, causing the topological charge to converge to an integer bit.



## 4. Comparison with State-of-the-Art Research: Positioning of PMNT L15.7

| Evaluation Item | Contemporary SOTA Research (e.g., Skyrmionics) | PMNT L15.7 |
| :--- | :--- | :--- |
| **Information Carrier** | Magnetic Skyrmions | NV Spin Skyrmion Texture |
| **Topological Protection** | Intrinsic DMI (Dzyaloshinskii-Moriya Interaction) | Multi-axial Anisotropy via NV Axes |
| **Bit Determination** | Nano-dot Structures via Microfabrication | Local Potential Pinning (Planned L16) |
| **Observation Method** | MFM / Synchrotron XMCD | FFT-based Structure Factor & $Q$ Calculation |

## 5. Conclusion
PMNT L15.7 has transitioned from the discovery of information "seeds" to the design of their "vessels." By defining potential fields that physically drive $Q$ toward a single point, the skyrmion as a physical phenomenon is sublimated into a digital bit for logical elements.