---
layout: default
title: Research
permalink: /research/
description: "Research areas of the Kreitz Research Group at Georgia Tech"
---

# Research

The Kreitz group develops computational methods for heterogeneous catalysis. We combine quantum chemistry, automated mechanism generation, microkinetic modeling, and machine learning to build predictive models of catalytic reactions — from elementary surface steps to reactor-scale behavior.

---

## Automated Mechanism Generation

<figure class="research-figure">
  <img src="{{ '/assets/images/research/mechanism-generation.png' | relative_url }}" alt="Schematic of automated mechanism generation workflow">
  <figcaption>Caption goes here — short description of what the figure shows.</figcaption>
</figure>

Heterogeneous catalytic reactions involve hundreds of elementary steps on structurally complex surfaces. Assembling reaction mechanisms by hand is slow, hard to reproduce, and easy to get wrong. We build automated workflows that construct microkinetic models directly from first-principles data, contributing to the open-source **Reaction Mechanism Generator (RMG)** and extending it to larger and more complex adsorbates.

A persistent issue in first-principles microkinetics is that DFT energies carry meaningful uncertainty, and the errors propagate in correlated ways through large networks. We generate **ensembles of mechanisms** that sample this uncertainty space, identifying parameter sets consistent with experimental data without ad hoc fitting — making the link between DFT and observables explicit rather than absorbed into tuning.

**Representative work:**
- Automated mechanism generation for CO₂ methanation on Ni(111) with correlated uncertainty quantification ([JACS Au 2021](https://doi.org/10.1021/jacsau.1c00276))
- Automated microkinetics for exhaust gas oxidation over Pt with DFT-constrained optimization ([ACS Catalysis 2022](https://doi.org/10.1021/acscatal.2c03378); [Angewandte Chemie 2023](https://doi.org/10.1002/anie.202306514))
- Bidentate adsorbates in RMG for larger molecules ([Digital Discovery 2024](https://doi.org/10.1039/D3DD00184A))

---

## Multiscale Modeling & Machine Learning for Catalysis

<figure class="research-figure">
  <img src="{{ '/assets/images/research/multiscale-ml.png' | relative_url }}" alt="Multiscale modeling and machine learning for catalysis">
  <figcaption>Caption goes here — short description of what the figure shows.</figcaption>
</figure>

Real catalysts are not single crystals, and bridging atomistic detail to reactor performance is one of the central modeling challenges in the field. We develop **structure-sensitive, multi-faceted nanoparticle models** that account for contributions from different surface facets and the surface diffusion of adsorbates between them, implemented as open-source capabilities in **Cantera**.

At larger scales, embedding detailed surface chemistry in reactor CFD is usually prohibitively expensive. We work on **multilevel sparse-grid methods** that couple coarse-grained and high-fidelity models self-consistently, making it tractable to retain detailed microkinetics in reactor simulations instead of collapsing them into lumped kinetics.

We also use **machine learning** to accelerate the modeling pipeline — surrogate models that replace expensive microkinetic evaluations, and AI-assisted approaches to mechanism generation and uncertainty quantification. A motivating problem is the **many-to-one challenge** in catalysis: many different surface structures and mechanisms can reproduce the same macroscopic observables, which limits what can be learned from experiment alone. We are interested in how generative and agentic AI can help integrate multimodal experimental data with theory to produce interpretable, transferable models.

**Representative work:**
- Structure-dependent microkinetics with surface diffusion in Cantera ([Journal of Catalysis 2025](https://doi.org/10.1016/j.jcat.2025.116407))
- Multilevel on-the-fly sparse grids for coupling microkinetics with reactor CFD ([Computers & Chemical Engineering 2025](https://doi.org/10.1016/j.compchemeng.2024.108922))
- Prospects for AI in understanding intrinsic kinetics of heterogeneous catalysis ([Current Opinion in Chemical Engineering 2026](https://doi.org/10.1016/j.coche.2026.101232))

---

## Thermochemistry of Adsorbates

<figure class="research-figure">
  <img src="{{ '/assets/images/research/thermochemistry.png' | relative_url }}" alt="Thermochemistry of adsorbates">
  <figcaption>Caption goes here — short description of what the figure shows.</figcaption>
</figure>

Microkinetic models are only as predictive as the thermophysical properties that define the underlying free energy landscape. Adsorbate enthalpies usually come from DFT, which carries systematic exchange–correlation errors that limit quantitative accuracy.

We develop **error-cancellation methods** built on the connectivity-based hierarchy (CBH), which constructs isodesmic reactions that conserve the bonding environment of adsorbates. Balancing electronic configurations between the reactant and reference species cancels systematic DFT errors and lets us tie ab initio results to experimental surface science data and gas-phase thermochemistry within a unified thermochemical network.

Adsorbate–adsorbate interactions at high coverage also shift enthalpies, entropies, and heat capacities in ways that matter for both surface science and reactor modeling. We extend Cantera with **coverage-dependent thermophysical properties** to capture these effects. Alongside the methods, we work to standardize the terminology and referencing conventions for thermochemical data in computational catalysis, so ab initio results are easier to reproduce and reuse across the field.

**Representative work:**
- Generalized thermochemical hierarchy linking experimental and ab initio adsorbate enthalpies ([JCTC 2023](https://doi.org/10.1021/acs.jctc.3c00112))
- Unified framework for thermochemistry concepts in computational heterogeneous catalysis ([Chemical Society Reviews 2025](https://doi.org/10.1039/D4CS00768A))
- Coverage-dependent thermophysical properties in Cantera ([JCIM 2025](https://doi.org/10.1021/acs.jcim.4c02167))
- CBH-based enthalpies on Pt(111), Ni(111), and MgO(100) ([Faraday Discussions 2026](https://doi.org/10.1039/D5FD00144G))

---

*For a full list of publications see the [Publications](/publications/) page.*
