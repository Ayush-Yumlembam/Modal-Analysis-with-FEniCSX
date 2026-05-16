# 3D Modal Analysis for Defect Detection

## Aim

To investigate whether **3D modal analysis** (using both mode shapes and natural frequencies) can be used to detect defects in manufactured parts by comparing a **normal model** against a **defect model**.

- **Tool:** FEniCSx + Python  
- **Defects:** Surface or sub-surface  
- **Application:** Quick "ping-like" screening in production line  

Further detailed NDT methods (liquid penetrant, radiography, eddy current) can be used for confirmation.

### Scope and Current Status

This work represents a **simple initial exploration**:

- The current model is a **first iteration** and requires refinement  
- Further work is needed to:
  - Determine the **smallest detectable defect size**  
  - Establish **sensitivity limits**  
  - Improve robustness for real-world use  

**Goal:** Evaluate whether modal analysis can serve as a fast global screening tool.

---

## Problem Setup

- 3D cantilever beam (clamped at one end)  
- Undamped, linear, free vibration (modal analysis)  
- Full 3D solid model (not a beam approximation)  

### Governing Equation
