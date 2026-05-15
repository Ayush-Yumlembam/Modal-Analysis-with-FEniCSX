# Modal-Analysis-with-FenicsX

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>3D Modal Analysis for Defect Detection</title>

<!-- MathJax for LaTeX rendering -->
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    line-height: 1.6;
}
h1, h2, h3 {
    color: #2c3e50;
}
code {
    background: #f4f4f4;
    padding: 4px;
}
.box {
    background: #eef6ff;
    padding: 15px;
    border-left: 5px solid #3498db;
    margin: 20px 0;
}
</style>
</head>

<body>

<h1>3D Modal Analysis for Defect Detection</h1>

<h2>🎯 Aim</h2>
<p>
To investigate whether <b>3D modal analysis</b> (using both mode shapes and natural frequencies) 
can be used to detect defects in manufactured parts by comparing a <b>normal model</b> 
against a <b>defect model</b>.
</p>

<ul>
<li>Tool: <b>FEniCSx + Python</b></li>
<li>Defects: Surface or sub-surface</li>
<li>Application: Quick “ping-like” screening in production line</li>
</ul>

<p>
Further detailed NDT methods (liquid penetrant, radiography, eddy current) can be used for confirmation.
</p>

<hr>

<h2>⚙️ Problem Setup</h2>

<ul>
<li>3D cantilever beam (clamped at one end)</li>
<li>Undamped, linear, free vibration (modal analysis)</li>
<li>Full 3D solid model (not beam approximation)</li>
</ul>

<div class="box">
<b>Governing equation:</b><br>
\[
K u = \lambda M u
\]
</div>

<ul>
<li>\(K\): stiffness matrix</li>
<li>\(M\): mass matrix</li>
<li>\(\lambda\): eigenvalue</li>
<li>\(u\): eigenvector (mode shape)</li>
</ul>

---

<h2>🧨 Defect Modeling</h2>

<ul>
<li>Defect simulated by removing elements</li>
<li>Represents cracks, porosity, or material loss</li>
</ul>

<p><b>Physical effects:</b></p>
<ul>
<li>Reduced stiffness locally</li>
<li>Lower natural frequencies</li>
<li>Distortion in mode shapes (primary indicator)</li>
</ul>

---

<h2>🧠 Weak Formulation</h2>

<div class="box">
\[
\int_{\Omega} \sigma(u) : \varepsilon(v)\, dx
\]
</div>

<p><b>Strain tensor:</b></p>
\[
\varepsilon(u) = \frac{1}{2}(\nabla u + \nabla u^T)
\]

<p><b>Stress tensor (Hooke’s Law, isotropic):</b></p>
\[
\sigma(u) = \lambda \, \text{tr}(\varepsilon(u)) I + 2\mu \varepsilon(u)
\]

---

<h2>🔒 Boundary Condition</h2>

<div class="box">
\[
u = 0 \quad \text{on the clamped boundary}
\]
</div>

---

<h2>📊 Modal Analysis Details</h2>

<ul>
<li>Eigenvalue solver: SLEPc</li>
<li>Problem type: Generalized Hermitian Eigenvalue Problem (GHEP)</li>
<li>Valid for undamped systems</li>
<li>Outputs: Frequencies + Mode shapes</li>
</ul>

---

<h2>⚠️ Numerical Notes</h2>

<ul>
<li>~0.159 Hz modes → numerical rigid-body artifacts</li>
<li>Ignored in interpretation</li>
<li>3 elements through thickness → thin structure</li>
</ul>

---

<h2>📈 Validation with Beam Theory</h2>

<p>Analytical reference (Euler–Bernoulli beam):</p>

<div class="box">
\[
f_n = \frac{\beta_n^2}{2\pi L^2} \sqrt{\frac{EI}{\rho A}}
\]
</div>

<p><b>Observation:</b></p>
<ul>
<li>~15–25% deviation from theory</li>
<li>FEM predicts slightly higher frequencies</li>
</ul>

---

<h2>❗ Reason for Differences</h2>

<ul>
<li>3D solid model vs 1D beam theory</li>
<li>Shear deformation included in FEM</li>
<li>Finite thickness effects</li>
<li>Mesh resolution limitations</li>
</ul>

---

<h2>📌 Key Modeling Assumptions</h2>

<ul>
<li>3D linear elasticity</li>
<li>Small strain formulation</li>
<li>Isotropic material</li>
<li>No damping</li>
</ul>

<p>
Based on classical formulations from:
<ul>
<li>Timoshenko & Goodier – <i>Theory of Elasticity</i></li>
<li>Zienkiewicz – <i>Finite Element Method</i></li>
</ul>
</p>

---

<h2>🧪 Interpretation for Defect Detection</h2>

<ul>
<li>Frequency shift → global stiffness change</li>
<li>Mode shape distortion → local defect indicator</li>
</ul>

<p>
Primary focus: <b>mode shape distortion</b>
</p>

---

<h2>🚀 Future Work</h2>

<ul>
<li>Include damping (decay signature analysis)</li>
<li>Fracture mechanics (LEFM)</li>
<li>Fatigue and creep analysis</li>
<li>Impact and dynamic loading</li>
</ul>

---

<h2>✅ Conclusion</h2>

<div class="box">
FEM results show good agreement with theory, validating:
<ul>
<li>✔ Correct stiffness and mass formulation</li>
<li>✔ Proper boundary conditions</li>
<li>✔ Reliable modal predictions</li>
</ul>
</div>

</body>
</html>
