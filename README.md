# ORB-Mono-KITTI-Evaluation
A brief python code to evaluate KeyFrameTrajectory.txt with the provided ground truth.

Change the following PATH's to correspond to your particular folder-structure:
    args.ground_time = '../Datasets/KITTI/dataset/sequences/{}/times.txt'.format(seq)  
    args.ground_data = '../Datasets/KITTI/dataset/poses/{}.txt'.format(seq)    
    args.res_time = '../ORB_SLAM3/outputs/Mono/mono-{}-KeyFrameTrajectory.txt'.format(seq)  
	args.eval_data = 'Evaluation-results/{}_eval'.format(seq)
        
 and then run: 
    python eval_kitti.py <Sequence#>.

