import numpy as np
import ioh
from itertools import product
from functools import partial
from multiprocessing import Pool, cpu_count

import sys
import argparse
import warnings
import os

from tqdm import tqdm

import nevergrad as ng


def runParallelFunction(runFunction, arguments):
    """
        Return the output of runFunction for each set of arguments,
        making use of as much parallelization as possible on this system

        :param runFunction: The function that can be executed in parallel
        :param arguments:   List of tuples, where each tuple are the arguments
                            to pass to the function
        :return:
    """
    

    arguments = list(arguments)
    p = Pool(min(96, len(arguments)))
    results = p.map(runFunction, arguments)
    p.close()
    return results

class Algorithm_Evaluator():
    def __init__(self, optimizer):
        self.alg = optimizer

    def __call__(self, func, seed):
        np.random.seed(int(seed))
        if self.alg == 'EMNA':
            c = ng.optimizers.EMNA()(parametrization=func.meta_data.n_variables, budget=int(10000*func.meta_data.n_variables))
            c.minimize(func)
        elif self.alg == 'PSO':
            c = ng.optimizers.PSO(parametrization=func.meta_data.n_variables, budget=int(10000*func.meta_data.n_variables))
            c.minimize(func)
        elif self.alg == 'DE':
            c = ng.optimizers.DE(parametrization=func.meta_data.n_variables, budget=int(10000*func.meta_data.n_variables))
            c.minimize(func)
        elif self.alg == 'Cobyla':
            c = ng.optimizers.Cobyla(parametrization=func.meta_data.n_variables, budget=int(10000*func.meta_data.n_variables))
            c.minimize(func)
        else: 
            print(f"{self.alg} Does not exist! ________")
        
def run_optimizer(temp):
    
    algname, fid, dim, type_ = temp

    # print(algname, fid)
    
    algorithm = Algorithm_Evaluator(algname)


    logger = ioh.logger.Analyzer(root="/scratch/share/nwmthkideads/projects/sbox", folder_name=f"{algname}_F{fid}_{dim}D_{type_.name}", algorithm_name=f"{algname}_{type_.name}", )

    for iid in tqdm(list(range(1,6)) + list(range(101,111))):
        func = ioh.get_problem(fid, dimension=dim, instance=iid, problem_class=type_) #in ioh < 0.3.9, problem_class -> problem_type
        # func.enforce_bounds(np.inf)
        func.attach_logger(logger)
        try:
            algorithm(func, iid)
        except:
            print(f"Failed run on {fid} {iid}")
        func.reset()
    logger.close()

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=RuntimeWarning) 
    warnings.filterwarnings("ignore", category=FutureWarning)

    fids = range(1,25)
    
    algnames = ['EMNA', 'PSO', 'DE', 'Cobyla']
    iids = list(range(1,6)) + list(range(101,111))
    dims = [3, 5, 10, 20, 40]
    tpyes = [ioh.ProblemClass.SBOX, ioh.ProblemClass.BBOB]#in ioh < 0.3.9, problemClass -> problemType
    
    args = product(algnames, fids, dims, tpyes)

    runParallelFunction(run_optimizer, args)
