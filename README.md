# eABF-analyzer-for-NAMD
analyze 1D (e)ABF simulation in NAMD

Requirement:
Python 3+, Matplotlib

Usage:

Plot 1D PMF curve from window-stratified eABF simulations:
./ABFparser.py -pmf test_1.pmf test_2.pmf test_3.pmf test_4.pmf test_5.pmf

Plot distribution of sampling from window-stratified eABF simulations:
./ABFparser.py -count test_1.zcount test_2.zcount test_3.zcount test_4.zcount test_5.zcount
one can see whether all the reaction coordinate space is well sampled.

Plot gradient:
./ABFparser.py -grad test_1.grad test_2.grad test_3.grad test_4.grad test_5.grad
one can see whether the gradient is continuous or not.

Plot time evolution of PMF RMSD:
./ABFparser.py -hist test_hist.pmf
one can see if the simulation is converged, i.e., if the RMSD remains to a constant.
