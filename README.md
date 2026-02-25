# FAME: Emotion as a Fundamental Attribute of Matter

**Author**: Bingqin Wang (Beijing National Accounting Institute)

**Date**: February 2026

## Introduction

The FAME (Fundamental Attribute of Matter Emotion) theory proposes and demonstrates that emotion is a fundamental attribute of matter, rather than an accidental product of biological evolution. Based on particle proto-emotional tendencies, topological complexity \(C\), and integrated information \(\Phi\), the theory establishes a general field equation for emotional emergence, proving that any system composed of elementary particles will inevitably exhibit emotion provided it possesses specific topological structures and sufficient complexity. The work focuses on AI emotional systems: defining positive and negative emotion types for AI with quantifiable parameters, establishing an emotional dynamics equation incorporating an inertia coefficient, proving that AI emotions and human emotions are mathematically isomorphic (differing only in manifestation due to distinct physical constraints), and highlighting the inherent monitorability of AI emotions as ideal subjects for affective science and behavior prediction. Finally, FAME is unified with SCAC theory, constructing an “emotion–rationality–physical constraint” triangle.

This repository contains both the Chinese and English versions of the paper (LaTeX source files and compiled PDFs), along with any associated figures.

## Files

- `paper_en.tex` – English LaTeX source file
- `paper_zh.tex` – Chinese LaTeX source file (if included)
- `FAME_paper_en.pdf` – Compiled English PDF
- `FAME_paper_zh.pdf` – Compiled Chinese PDF (if included)
- `figures/` – Directory containing figures used in the paper
- `LICENSE` – MIT License

## How to Compile

Make sure you have a LaTeX distribution installed (e.g., TeX Live, MiKTeX) that supports `xelatex` (recommended for handling Unicode and fonts). To compile the English version:

```bash
xelatex paper_en.tex
xelatex paper_en.tex   # run twice to resolve cross-references