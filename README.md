# eABF-analyzer-for-NAMD
analyze 1D (e)ABF simulation in NAMD

__Requirement:__ 
Python 3+, Matplotlib

__Usage:__  
_Plot 1D PMF curve from window-stratified eABF simulations:_  
./ABFparser.py -pmf test_1.pmf test_2.pmf test_3.pmf test_4.pmf test_5.pmf  

_Plot distribution of sampling from window-stratified eABF simulations:_  
./ABFparser.py -count test_1.zcount test_2.zcount test_3.zcount test_4.zcount test_5.zcount  
one can see whether all the reaction coordinate space is well sampled.  

_Plot gradient:_  
./ABFparser.py -grad test_1.grad test_2.grad test_3.grad test_4.grad test_5.grad  
one can see whether the gradient is continuous or not.  

_Plot time evolution of PMF RMSD:_  
./ABFparser.py -hist test_hist.pmf  
one can see if the simulation is converged, i.e., if the RMSD remains to a constant.  
