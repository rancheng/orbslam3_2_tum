# orbslam3_2_tum

convert orb-slam3 pose.txt file to tum format.

Since the timestamp format of TUM and ORB-SLAM3 output result is different, so we need to convert the time-stamp to be consistent with TUM format.

The following python script is used to convert the ORB-SLAM3 result file to TUM format.

Run the python script to fix the ORB-SLAM3 result pose file:

```shell
python converter.py /path/to/kf_orbslam_result.txt /path/to/tum_result.tum
```
