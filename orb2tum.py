import numpy as np
import argparse

def orbslamRes2TUM(fname, out_fname):
   pose_data = np.genfromtxt(fname, dtype=float, delimiter=" ")
   pose_data[:, 0] /= 1e9
   np.savetxt(out_fname, pose_data)

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("result_fname", type=str,
                       help="ORB-SLAM3 output result file name, please input absolute path")
   parser.add_argument("output_fname", type=str,
                       help="converted TUM format file name, please input absolute path")
   args = parser.parse_args()
   orbslamRes2TUM(args.result_fname, args.output_fname)
