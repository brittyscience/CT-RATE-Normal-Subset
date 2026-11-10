# CT- RATE Noraml Subset Analysis 

## Objective

Identify CT volumes from the CT-RATE dataset where all 18 abnormality labels equals to 0. 

Dataset is from CT-RATE: https://huggingface.co/datasets/ibrahimhamamci/CT-RATE

This analysis use training and validation abnormality label files from that dataset. 

## Method:

1. Load the CSV using pandas
2. Exclude the VolumeName identifier column
3. Check whether all 18 abnormality labels equals to 0 for each CT volume using boolean mask ( all 18 =0 --> true), If not, false. 
4. Count qualifying CT volumes separately ( training data and validation data separately) 

# Results:

## Datasets

Training: 5,226 normal CT Volumes
Validation: 346 normal CT Volumes 

Total: 5,572 Normal CT volumes

### Note on Data Availability

The CT-RATE dataset files are not redistributed in this repository. Please refer to the official dataset link above.

### Reference/ Citation 

Hamamci, I. E., et al. (2026). Generalist foundation models from a multimodal dataset for 3D computed tomography. Nature Biomedical Engineering.
