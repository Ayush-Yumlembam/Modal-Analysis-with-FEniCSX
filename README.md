<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>3D Modal Analysis for Defect Detection</title>

<!-- MathJax Config -->
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$']]
  }
};
</script>

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
img {
    max-width: 100%;
    margin: 20px 0;
    border: 1px solid #ccc;
}
</style>
</head>

<body>

<h1>3D Modal Analysis for Defect Detection</h1>

<h2>Aim</h2>

<p>
To investigate whether <b>3D modal analysis</b> (using both mode shapes and natural frequencies)
can be used to detect defects in manufactured parts by comparing a <b>normal model</b>
against a <b>defect model</b>.
</p>

<ul>
<li>Tool: FEniCSx + Python</li>
<li>Defects: Surface or sub-surface</li>
<li>Application: Quick "ping-like" screening in production line</li>
</ul>

<p>
Further detailed NDT methods (liquid penetrant, radiography, eddy current) can be used for confirmation.
</p>

<h3>Scope and Current Status</h3>
<ul>
<li>This work represents a <b>simple, initial exploration</b> of the concept.</li>
<li>The current model is a <b>first iteration</b> and requires refinement.</li>
<li>Further work needed to:
  <ul>
    <li>Determine smallest detectable defect size</li>
    <li>Establish sensitivity limits</li>
    <li>Improve robustness</li>
  </ul>
</li>
</ul>

<hr>

<h3>Engineering Intent</h3>
<ul>
<li>The goal is <b>not a production-ready solution</b>, but to evaluate:</li>
  <ul>
    <li>Whether modal analysis can serve as a fast, global screening tool for defect detection.</li>
  </ul>
</li>
</ul>

<hr>

<h2>Problem Setup</h2>

<ul>
<li>3D cantilever beam (clamped at one end)</li>
<li>Undamped, linear, free vibration (modal analysis)</li>
<li>Full 3D solid model (not a beam approximation)</li>
</ul>

<div class="box">
<b>Governing equation:</b><br>
$$
K u = \lambda M u
$$
</div>

<ul>
<li>K: stiffness matrix</li>
<li>M: mass matrix</li>
<li>λ: eigenvalue (frequency)</li>
<li>u: eigenvector (mode shape)</li>
</ul>

<img src="images/geometry.png" alt="Geometry and mesh">

<p><b>Explanation:</b> Structured 3D mesh with a thin geometry. The beam is clamped at one end.</p>

<hr>

<h2>Defect Modeling</h2>

<ul>
<li>Defect simulated by removing elements</li>
<li>Represents local stiffness loss</li>
</ul>

<p><b>Effect of defect:</b></p>
<ul>
<li>Reduction in stiffness</li>
<li>Lower natural frequencies</li>
<li>Distortion in mode shapes (primary indicator)</li>
</ul>

<img src="images/defect.png" alt="Defect region">

<hr>

<h2>Weak Formulation</h2>

<div class="box">
$$
\int_{\Omega} \sigma(u) : \varepsilon(v)\, dx
$$
</div>

<p><b>Strain tensor:</b></p>
$$
\varepsilon(u) = \frac{1}{2}(\nabla u + \nabla u^T)
$$

<p><b>Stress tensor (Hooke's Law):</b></p>
$$
\sigma(u) = \lambda \, \text{tr}(\varepsilon(u)) I + 2\mu \varepsilon(u)
$$

<hr>

<h2>Boundary Condition</h2>

<div class="box">
$$
u = 0 \quad \text{on the clamped boundary}
$$
</div>

<hr>

<h2>Modal Analysis</h2>

<ul>
<li>Eigenvalue solver: SLEPc</li>
<li>Problem type: Generalized Hermitian Eigenvalue Problem (GHEP)</li>
<li>Undamped system</li>
<li>Outputs: Frequencies and mode shapes</li>
</ul>

<img src="images/mode_shape.png" alt="Mode shape">

<p><b>Explanation:</b> Mode shapes are used to identify distortions caused by defects.</p>

<hr>

<h2>Validation</h2>

<p>Analytical reference (Euler–Bernoulli beam):</p>

<div class="box">
$$
f_n = \frac{\beta_n^2}{2\pi L^2} \sqrt{\frac{EI}{\rho A}}
$$
</div>

<ul>
<li>Observed deviation: ~15–25%</li>
<li>FEM predicts slightly higher frequencies</li>
</ul>

<p><b>Reason:</b></p>
<ul>
<li>3D model vs 1D beam theory</li>
<li>Shear deformation included</li>
<li>Finite thickness effects</li>
<li>Mesh resolution</li>
</ul>

<hr>

<h2>Numerical Notes</h2>

<ul>
<li>~0.159 Hz modes are numerical artifacts</li>
<li>These are ignored in interpretation</li>
</ul>

<hr>

<h2>Conclusion</h2>

<div class="box">
<ul>
<li>FEM results agree reasonably with theory</li>
<li>Correct stiffness and mass formulation</li>
<li>Proper boundary conditions</li>
<li>Reliable modal predictions</li>
</ul>
</div>

<hr>

<h2>Future Work</h2>

<ul>
<li>Refine defect detection sensitivity</li>
<li>Introduce damping effects</li>
<li>Extend to fracture and fatigue analysis</li>
</ul>

</body>
</html>
