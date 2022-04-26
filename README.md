# Solar cell EL image defect detection

# News
[2022-04-26]：We will provide a val set of PVELAD dataset.

[2022-04-13]：Box annotations for vertical_dislocation and horizontal_dislocation will be added into PVELAD dataset.

[2021-12-14]: Training data augmentation via horizontal_flipping.py. Evaluation: first, converting ground truth xml to txt by get_gt_txt.py; Second, appling AP50-5-95.py to evaluate the detection results.

[2021-11-23]: A kaggle competition platform is built, then you can submit you result in https://www.kaggle.com/c/pvelad, and evaluate your algorithm.

**Dataset application website:** http://aihebut.com/col.jsp?id=118 or https://github.com/binyisu/PVEL-AD

**2021 Dataset Access Instructions:**

We build a Photovoltaic Electroluminescence Anomaly Detection dataset (PVEL-AD ) for solar cells, which contains 36,543 near-infrared images with various internal defects and heterogeneous backgrounds. This dataset contains 1 class of anomaly-free images and anomalous images with **12** different categories such as crack (line and star), finger interruption, black core, thick line, scratch, fragment, corner, printing_error, horizontal_dislocation, vertical_dislocation, and short_circuit defects. Moreover, 40358 ground truth bounding boxes are provided for **12** types of defects. This is a **long-tail object detection task**, which is challenging and significant for smart manufacturing.

The **PVELAD-2021 Datasets Request Form** is available here. 

All researchers need to follow the instructions below to access the datasets.


* Download and fill the **Industrial Datasets Request Form** (MUST be hand signed with date). Please use institutional email address(es). Commercial emails such as Gmail and QQmail are NOT allowed. 

* Email the signed **Industrial Datasets Request Form** to Subinyi@buaa.edu.cn
* The dataset is jointly released by **Hebei University of Technology** and **Beihang University**.

![image](https://github.com/binyisu/PVEL-AD/blob/main/pvel.jpg)

[1] Binyi Su, Zhong Zhou, Haiyong Chen, “PVEL-AD: A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection,” *IEEE Trans. Ind. Inform.*, DOI (identifier) :10.1109/TII.2022.3162846

[2] B. Su, H. Chen, Y. Zhu, W. Liu and K. Liu, ``Classification of Manufacturing Defects in Multicrystalline Solar Cells With Novel Feature Descriptor,'' *IEEE Trans. Instrum. Meas.*, vol. 68, no. 12, pp. 4675--4688, Dec. 2019.

[3] B. Su, H. Chen, and P. Chen, ``Deep Learning-Based Solar-Cell Manufacturing Defect Detection With Complementary Attention Network,'' *IEEE Trans. Ind. Inform.*, vol. 17, no. 6, pp. 4084--4095, Jun. 2021.

[4] B. Su, H. Chen, and Z. Zhou, ``BAF-Detector: An Efficient CNN-Based Detector for Photovoltaic Cell Defect Detection,'' *IEEE Trans. Ind. Electron.*,  vol. 69, no. 3, pp. 3161-3171, Mar. 2022.
