# SBOX
SBOX-COST is a version of the BBOB suite for single-objective, continuous, noiseless optimization (minimization). It consists of the same 24 base functions, but with changed instance generation mechanism. This allows the optimum of most problems to be located anywhere in the domain ([-5,5]^n), instead of [-4,4]^n as done in the original BBOB. In addition, points outside the domain are considered infeasible, and therefore given function value of infinity. 

The suite can be accessed using COCO (see branch suite-sbox on https://github.com/sbox-cost/coco) in the same way as the regular BBOB suite, or using IOHprofiler. 

# Examples
This repository contains some examples of using the SBOX-COST suite in IOHexperimenter. 

The file "Example.ipnb" provides a getting-started guide on using the suite, while the "data_collection_SBOX_cma.py" contains code for a full-scale experiment using several versions of the CMA-ES algorithm.

# Instructions for submission
To submit a short paper to the SBOX-COST workshop, you should submit the pdf of the paper in the gecco system using the gecco format. Additionally, you should upload the full benchmark data (either IOHprofiler or COCO format) to a zenodo repository, which you link in the paper. It is highly encouraged to also include your algorith code and the script used to collect the data in this same repository. 

In terms of data collection, you should run your algorithm on all 24 functions of both the BBOB and SBOX-COST suites. You should use at least dimensions 5 and 20 ([2,3,5,10,20,40] is recommended), 15 instances (instance numbers 1-5 and 101-110), at least 1 run each. 

To visualize your data for the paper, you can make use of COCO's post-processing module, or of IOHanalyzer (https://iohanalyzer.liacs.nl). On IOHanalyzer, several baseline algorithms are provided (they can be loaded by selecting 'SBOX-COST' as the source). For more information on using IOHanalyzer, please see https://iohprofiler.github.io/IOHanalyzer/GUI/

