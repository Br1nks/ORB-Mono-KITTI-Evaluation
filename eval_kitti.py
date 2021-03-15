from mono_eva2 import exec_main
import numpy as np
import matplotlib.pyplot as plt

import argparse



class Eval_Kitti(object):
    def __init__(self):
        return 
    def run(self):
        parser = argparse.ArgumentParser(description='''
        This script computes the absolute trajectory error from the ground truth trajectory and the estimated trajectory. 
        ''')
        parser.add_argument('seq', help='sequence number of kitti dataset, like 04')
        args = parser.parse_args()
        
        seq = args.seq
        args.ground_time = '../Datasets/KITTI/dataset/sequences/{}/times.txt'.format(seq)  
        args.ground_data = '../Datasets/KITTI/dataset/poses/{}.txt'.format(seq)    
        args.res_time = '../ORB_SLAM3/outputs/mono-{}-KeyFrameTrajectory.txt'.format(seq)  
	args.eval_data = 'evaluation/{}_eval'.format(seq)
        args.verbose = True
        exec_main(args)
        return



if __name__ == '__main__':
    obj = Eval_Kitti()
    obj.run()
    
    
