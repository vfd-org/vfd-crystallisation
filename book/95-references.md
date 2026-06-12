# Further Reading

This book is the plain-language telling of a body of technical work, and it leans throughout on mathematics that is centuries old and owes nothing to the framework. This is where to go if you want to go deeper, in either direction: outward to the settled classical results, or inward to the programme's own derivations and their honest verification.

## The classical mathematics

All of the following is standard, can be found in textbooks or the original papers, and would be true if this framework were wrong. I have tried throughout the book to flag it as common property.

The five Platonic solids and the proof that there are exactly five go back to Euclid's *Elements*, Book XIII. The six regular four-dimensional shapes, the 600-cell among them, were found by Ludwig Schläfli in the 1850s; the modern reference is H. S. M. Coxeter, *Regular Polytopes*, which remains the most readable way in.

The quaternions are Hamilton's, from 1843; the octonions were found shortly after by Graves and Cayley. For a genuinely enjoyable tour of both and of why the ladder of number systems stops where it does, John Baez's survey article *The Octonions* (2002) is hard to beat, and Conway and Smith's *On Quaternions and Octonions* is the book-length treatment. The theorems that close the ladder are Hurwitz's (on which dimensions admit a division algebra) and Adams's (on which spheres can be combed).

The question of hearing a drum's shape is Mark Kac's, from his 1966 article *Can One Hear the Shape of a Drum?* The law connecting a spectrum to a dimension is Hermann Weyl's, from 1911. The even spreading of points that stand in for a sphere is the theory of spherical designs, introduced by Delsarte, Goethals, and Seidel in 1977. The correspondence between the crystal's symmetry and the E8 diagram is John McKay's, from 1980.

On the gravity side, the uniqueness of the weak-field law is the Fierz–Pauli result, from 1939. The argument that such a law must complete itself into Einstein's general relativity by coupling to its own energy is due to Gupta, Kraichnan, Feynman, Deser, and others through the 1950s to the 1970s; Deser's 1970 paper *Self-Interaction and Gauge Invariance* is the cleanest single source, and Robert Wald's 1986 uniqueness theorem is the one the book cites as still standing in for the last step.

## The framework's own work

These are the technical documents this book retells, with their full derivations, their proofs, their open problems, and the code that checks them. They live in the project repository.

The gravity chain, the derivation of Einstein's equations from the substrate, is Paper LIII, *Einstein's Equations from Substrate Closure*, with the remaining continuum-geometry programme in Paper XL. The cascade of rungs and the mass ladder are in the cascade papers, including the muon-to-Newton's-constant result of Paper LII. The cosmology side, the dark-energy fraction and the expansion rate, is the *Hypersphere Cosmology* release. The reading of the 600-cell as the substrate, the construction of looking, the rendering kernel, and the derivation of wave-like time are set out in the rendering-layer and rung-dimension-ladder notes.

Every checkable claim in this book has code behind it, and the exact list, with the command to run each test and the number it should print, is the project's verification manifest. The consolidated grading of every claim, from theorem down to open problem, is the claim–status ledger, which the Honest Ledger at the back of this book is drawn from. Both are the place to start if your instinct, like mine, is to trust a result only once you have watched it run.
