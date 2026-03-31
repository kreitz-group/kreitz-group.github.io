---
layout: default
title: Research
permalink: /research/
description: "Research areas of the Kreitz Research Group at Georgia Tech"
---

# Research

Our group develops **computational tools and theoretical frameworks** to understand and design heterogeneous catalysts from first principles. We combine quantum chemistry, microkinetic modeling, and data-driven methods to bridge the gap between atomistic simulations and reactor-scale predictions — with the goal of accelerating the discovery of catalysts for sustainable chemistry.

---

## Microkinetic Modeling & Mechanism Generation

Heterogeneous catalytic reactions involve hundreds of elementary steps across complex surfaces. Manually constructing reaction mechanisms is time-consuming, difficult to reproduce, and prone to missing important pathways. We develop automated workflows for generating microkinetic models directly from first-principles data, using tools like the open-source **Reaction Mechanism Generator (RMG)**.

A central challenge in first-principles microkinetics is that DFT energetics carry significant uncertainty, and these errors propagate in correlated ways through large mechanisms. We address this by generating **ensembles of mechanisms** that systematically sample the DFT uncertainty space, allowing us to identify feasible parameter sets that agree with experimental data without ad hoc fitting.

Our models account for structural complexity at the nanoscale — real catalysts are not single crystals. We develop **structure-sensitive, multi-faceted nanoparticle models** that include contributions from different surface facets and incorporate surface diffusion of adsorbates between them, enabled by new open-source capabilities in **Cantera**.

**Representative work:**
- Automated mechanism generation for CO₂ methanation on Ni(111) with correlated uncertainty quantification ([JACS Au 2021](https://doi.org/10.1021/jacsau.1c00276))
- Automated microkinetics for exhaust gas oxidation over Pt with DFT-constrained optimization ([ACS Catalysis 2022](https://doi.org/10.1021/acscatal.2c03378); [Angewandte Chemie 2023](https://doi.org/10.1002/anie.202306514))
- Bidentate adsorbates in RMG for modeling larger molecules ([Digital Discovery 2024](https://doi.org/10.1039/D3DD00184A))
- Structure-dependent microkinetics with surface diffusion in Cantera ([Journal of Catalysis 2025](https://doi.org/10.1016/j.jcat.2025.116407))

---

## Thermochemistry of Surface Species

Predictive microkinetic models are only as reliable as the thermophysical properties that define the free energy landscape. Enthalpies of adsorbates are typically derived from DFT, which suffers from systematic exchange–correlation errors that limit quantitative accuracy.

We develop **error-cancellation methods** based on the connectivity-based hierarchy (CBH) that construct isodesmic reactions conserving the bonding environment of adsorbates. By balancing electronic configurations between reactant and reference species, these reactions cancel systematic DFT errors — achieving **beyond-DFT accuracy at DFT cost**. The approach integrates experimental surface science data, gas-phase thermochemistry, and ab initio calculations into a unified thermochemical network.

We also address **coverage-dependent thermophysical properties**, since adsorbate–adsorbate interactions at high surface coverages significantly alter enthalpies, entropies, and heat capacities in ways that matter for both surface science and reactor modeling. These methods are implemented in Cantera.

More broadly, we work to standardize the terminology and referencing conventions for thermochemical data in computational catalysis — reducing barriers to reproducing and reusing ab initio results across the field.

**Representative work:**
- Generalized thermochemical hierarchy linking experimental and ab initio adsorbate enthalpies ([JCTC 2023](https://doi.org/10.1021/acs.jctc.3c00112))
- Unified framework for thermochemistry concepts in computational heterogeneous catalysis ([Chemical Society Reviews 2025](https://doi.org/10.1039/D4CS00768A))
- Coverage-dependent thermophysical properties in Cantera ([JCIM 2025](https://doi.org/10.1021/acs.jcim.4c02167))
- CBH-based enthalpies on Pt(111), Ni(111), and MgO(100) ([Faraday Discussions 2026](https://doi.org/10.1039/D5FD00144G))

---

## Machine Learning for Catalysis & Multiscale Modeling

Atomistic simulations of catalytic systems are increasingly bottlenecked by the cost of high-fidelity calculations. We develop and apply **machine-learning methods** to accelerate the modeling pipeline — from surrogate models that replace expensive microkinetic evaluations in reactor simulations, to AI-assisted mechanism generation and uncertainty quantification.

We are particularly interested in how AI can help address the **many-to-one challenge** in catalysis: many different surface structures and mechanisms can produce similar macroscopic observables, making it hard to extract mechanistic insight from experimental data alone. Generative and agentic AI approaches offer new tools for coupling theoretical predictions with multimodal experimental data to produce interpretable and transferable models.

We also develop **multilevel sparse-grid approaches** that couple coarse-grained and high-fidelity models in a self-consistent, computationally efficient way — drastically reducing the cost of integrating detailed surface chemistry into continuum reactor simulations.

**Representative work:**
- Multilevel on-the-fly sparse grids for coupling microkinetics with reactor CFD ([Computers & Chemical Engineering 2025](https://doi.org/10.1016/j.compchemeng.2024.108922))
- Prospects for AI in understanding intrinsic kinetics of heterogeneous catalysis ([Current Opinion in Chemical Engineering 2026](https://doi.org/10.1016/j.coche.2026.101232))

---

*For a full list of publications see the [Publications](/publications/) page.*
