# Path-Weighted Atom Vectors and ChemBERTa Fusion for Predicting Physicochemical Properties

This repository provides datasets and reproducible workflows associated with the paper:  

**Path-Weighted Atom Vectors and ChemBERTa Fusion for Predicting Physicochemical Properties**

---

## 📂 Repository Structure

### `Data Files/`

- **Zang_Data.xlsx**  
  Source dataset taken from:  
  > Zang, Q., Mansouri, K., Williams, A. J., Judson, R. S., Allen, D. G., Casey, W. M., & Kleinstreuer, N. C. (2017).  
  > *In silico prediction of physicochemical properties of environmental chemicals using molecular fingerprints and machine learning.*  
  > *Journal of Chemical Information and Modeling, 57*(1), 36–49.  

  The file contains six sheets with SMILES strings, experimental data, model predictions, and training/test splits.  
  It includes six physicochemical properties:

  - **Log VP** – Logarithm of vapor pressure (volatility measure)  
  - **MP** – Melting Point  
  - **BP** – Boiling Point  
  - **Log BCF** – Bioconcentration Factor (chemical accumulation in organisms)  
  - **Log S** – Aqueous Solubility  
  - **Log P** – Lipophilicity (partition coefficient between *n*-octanol and water).  
    In chemistry, *logP* quantifies how well a neutral compound dissolves in a nonpolar solvent (like octanol) compared to water.

- **Other folders**  
  - `Data Statistics/` – Exploratory data analysis and summary statistics  
  - `Descriptor Generators/` – Colab notebooks to generate molecular descriptors  
  - `Models/` – Colab notebooks for training and evaluating machine learning models  

---

## 🚀 Running the Workflows

All experiments are implemented as **Google Colab notebooks**.  
You can open any notebook in Colab and execute the cells sequentially to reproduce the results.  

Example:  
```text
Data Files/Descriptor Generators/GenerateDescriptorsData.ipynb

## ⚡ GPU Requirements

* Data Files/Models/ChemBERTaFiLMFusion.ipynb

* Relies on deep neural networks and is GPU-intensive.

* Running on a CPU is extremely slow and not recommended.

* Best run on Kaggle (GPU runtime) or Google Colab with GPU enabled.

## Other models

* Can be run efficiently on CPU-only systems without any issue.

* GPU is required only for neural-network–based models.

## 🔗 Data Availability (OSF)

To ensure reproducibility, some intermediate datasets generated during experiments are hosted on Open Science Framework (OSF).

* Each Colab notebook (usually in the second cell) contains the code required to fetch the relevant dataset directly from OSF.

* This means any dataset used or generated in the paper can be retrieved automatically when running the notebooks.

## 📖 Citation

If you use this repository or dataset, please cite the original data source:
'''
Zang, Q., Mansouri, K., Williams, A. J., Judson, R. S., Allen, D. G., Casey, W. M., & Kleinstreuer, N. C. (2017).
In silico prediction of physicochemical properties of environmental chemicals using molecular fingerprints and machine learning.
Journal of Chemical Information and Modeling, 57(1), 36–49.
'''
