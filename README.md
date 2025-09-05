# Path-Weighted Atom Vectors and ChemBERTa Fusion for Predicting Physicochemical Properties

This repository provides data and reproducible workflows associated with the paper:  

**Path-Weighted Atom Vectors and ChemBERTa Fusion for Predicting Physicochemical Properties**

---

## 📂 Repository Structure

### `Data Files/`
- **Zang_Data.xlsx**  
  Source dataset taken from:  
  > Zang, Q., Mansouri, K., Williams, A. J., Judson, R. S., Allen, D. G., Casey, W. M., & Kleinstreuer, N. C. (2017).  
  > *In silico prediction of physicochemical properties of environmental chemicals using molecular fingerprints and machine learning.*  
  > *Journal of Chemical Information and Modeling, 57*(1), 36–49.  

  This Excel file contains six sheets with SMILES, experimental measurements, model predictions, and train/test splits.  
  The following physicochemical properties are included:
  - `Log VP`  
  - `MP` (Melting Point)  
  - `BP` (Boiling Point)  
  - `LogBCF`  
  - `LogS` (Solubility)  
  - `LogP`  

- **Other folders**  
  - `Data Statistics/` – Exploratory analysis and summary statistics  
  - `Descriptor Generators/` – Colab notebooks to generate molecular descriptors  
  - `Models/` – Colab notebooks for training and evaluation  

---

## 🚀 Running the Workflows

All analysis and modeling are implemented in **Google Colab notebooks**.  
You can open any notebook directly in Colab and execute cells sequentially to reproduce the results.

Example:  
```text
Data Files/Descriptor Generators/GenerateDescriptorsData.ipynb
