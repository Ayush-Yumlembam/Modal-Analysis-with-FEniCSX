# 3D Modal Analysis for Defect Detection

## Aim

To investigate whether **3D modal analysis** (using both mode shapes and natural frequencies) can be used to detect defects in manufactured parts by comparing a **normal model** against a **defect model**.

The analysis results have to be compared with a real "ping-like" test done on a real workpiece with and without defect, for test data correlation. This part is not under the scope of this investigation.

- **Tool:** FEniCSx + Python + Viewing in Paraview + Jupyter Notebook
- **Defects:** Surface or sub-surface  
- **Application:** Quick "ping-like" screening in production line for gas turbine blades, aero fan blades, or any slender critical component

Further detailed NDT methods (liquid penetrant, radiography, eddy current) can be used for confirmation.

### Scope and Current Status

This work represents a **simple initial exploration**:

- The current model is a **first iteration** and requires refinement  
- Further work is needed to:
  - Determine the **smallest detectable defect size**  
  - Establish **sensitivity limits**  
  - Improve robustness for real-world use  

### Engineering Intent

The goal is **not a production-ready solution**, but to evaluate:
- Whether modal analysis can serve as a fast, global screening tool for defect detection.

---

## Software Versions

FEniCSX Container based on Windows 11 + Docker (installed in Windows 11) + WSL2-Ubuntu integration

- Windows 11 Pro 25H2 26200.8457
- WSL2
- Docker version 29.3.1, build c2be9cc
- Paraview 5.13.2
- FEniCSX
  - dolfinx: 0.10.0.post2
  - basix: 0.10.0
  - ufl: 2025.2.0.post0

---

## Problem Setup

- 3D cantilever beam (clamped at one end)  
- Undamped, linear, free vibration (modal analysis), but not free-free modal analysis  
- Full 3D solid model (not a beam approximation)  
- First order elements used
- Material is linear (modal analysis assumes linear elasticity)

### Governing Equation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**K u = λ M u**

Where:
- `K` = stiffness matrix  
- `M` = mass matrix  
- `λ` = eigenvalue (related to frequency)  
- `u` = eigenvector (mode shape)  

### Geometry and Mesh

![Geometry](images/3d-bar-end-fixed-mod-analy_mesh_markups.png)

*Structured 3D mesh. Thin geometry with clamped boundary at one end (end closer to origin).*
*Defect is simulated as material removed (elements removed). This is a very quick and simplistic methodology.*

---

## Defect Modeling

- Defect simulated by **removing elements**
- Represents local stiffness loss

### Physical Effect of Defect

- Reduction in stiffness  
- Lower natural frequencies  
- Distortion in mode shapes (**primary indicator**)  

---

## Weak Formulation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**∫_Ω σ(u) : ε(v) dx**

### Strain Tensor

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ε(u) = 1/2 (∇u + ∇uᵀ)**

### Stress Tensor (Hooke’s Law, isotropic)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**σ(u) = λ tr(ε(u)) I + 2μ ε(u)**

### Boundary Condition

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**u = 0 (on clamped boundary; Dirichlet Boundary Condition)**

---

## Modeling Assumptions

- 3D linear elasticity  
- Small strain formulation  
- Isotropic material  
- No damping  

Based on classical formulations from:
- Timoshenko & Goodier – *Theory of Elasticity*  
- Zienkiewicz – *Finite Element Method*  

---

## Modal Analysis and Results

- Solver: SLEPc eigenvalue solver  
- Problem type: **Generalized Hermitian Eigenvalue Problem (GHEP)**  
- System: **Undamped**  

Outputs:
- Natural frequencies  
- Mode shapes  

![Mode Shape](images/3d-bar-end-fixed-mod-analy_7th-mode-compare.png)

***Mode Shapes** used to detect distortion due to defects.*
*7th mode shape, bending, normal 96.04 Hz (above left), defect 90.64 Hz (above right).*

As expected, we can clearly see that the large defect causes significant frequency shifts (reductions), and distortions in mode shapes (note the fringe color plot changes). Note the bigger red or magenta band in the middle of the defect model on right (the band is exactly at the weaker defect region, as expected).

This indicates that the method, for now atleast, works for large defects. We need to further test the method on smaller defects, different orientations, sub-surface defects, etc. 

![Mode Shape](images/3d-bar-end-fixed-mod-analy_1st-mode-compare.png)
*1st mode shape, bending, normal 2.80 Hz (above left), defect 2.69 Hz (above right).*

![Mode Shape](images/3d-bar-end-fixed-mod-analy_3rd-mode-compare.png)
*3rd mode shape, bending, normal 22.95 Hz (above left), defect 22.68 Hz (above right).*

From the lower modes we can see that, it is not very helpful in differentiating the effects of the defect. The mode shape fringe plots for the lower modes are quite similar. Hence, we need mode shape plots of higher modes. Extract atleast first 10 modes.

![Mode Shape](images/3d-bar-end-fixed-mod-analy_4th-mode-compare-torsion.png)
*4th mode shape, torsion, normal 27.44 Hz (above left), defect 25.24 Hz (above right).*

This is the first torsion mode. This shows clearly the effect of the defect. Note the bigger blue band in the middle of the defect model on right.

![Mode Shape](images/orient-zoom-script_how-to-run.png)

*orient-zoom-script.py - How to run this Paraview script. Script is included in the uploaded Jupyter Notebook code files folders.*

This script will zoom and orient all Paraview viewports (RenderView) in the same manner for easy comparison; run the script, one by one in each viewport.
The scaling of the plots is not included in the script; scaling to be done manually. For easy comparison, keep the plot scales same.

Comparing result views in same zoom and orientation is Aviation industry standard for all reporting/documentations. This is absolutely necessary, hence the script is included. 
Plot scales, Color map/values/limits should also be the same.

---

## Defect Detection Insight

- Frequency shift -> global stiffness change  
- Mode shape distortion -> global and local defect indicator (**primary focus**)  

---

## Validation

Analytical reference (Euler–Bernoulli beam theory):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f_n = (β_n² / 2πL²) √(EI / ρA)**

### Observations

- ~15–25% deviation from analytical solution  
- FEM predicts slightly higher frequencies  

### Reason for Difference

- 3D solid model vs 1D beam theory  
- Shear deformation included in FEM  
- Finite thickness effects  
- Mesh resolution (3 elements through thickness; 5 elements can be tried too)  

### Numerical Notes

- ~0.159 Hz modes -> numerical artifacts (rigid-body-like)  
- These are ignored in interpretation  

---

## Conclusion

- FEM results show good agreement with theory  
- Correct stiffness and mass formulation  
- Proper boundary conditions  
- Reliable modal predictions  
- In defect model, frequency shifts (reduction) and mode shapes distortion observed, thereby showing that the method is capable of detecting large surface defects. Need to further test on smaller defects.

---

## Future Work

- Improve defect detection sensitivity; test the method on smaller defects
- Try with 2nd order elements (see if stiffness and frequency reduces and matches more with analytical values)
- Quantify minimum detectable defect size
- Extend work to strength, fatigue, fracture (LEFM), and creep (dwell effects), impact analyses 
- Introduce damping effects, to see how the vibration dies out over time. The vibration die out signature may be helpful in fine tuning the defect detection. This damping effect may help in increasing the detection sensitivity.

---






