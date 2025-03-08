# isaacsim-lio-sam
A modified version of LIO-SAM for Isaac Sim integration, with additional launch files. Based on Tixiao Shan's LIO-SAM (BSD 3-Clause).

### Purpose
- Provides asset and codes about using LIO-SAM at Isaac Sim

### Important
- lio-sam/src/mapOptimization.cpp
    - 1660 Line >> lidar_link to actual scan frame (base_scan)
- Modify isaac.yaml file based on your sensor (LiDAR)