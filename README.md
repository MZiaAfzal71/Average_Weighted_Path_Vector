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

  - **Log VP** – Logarithm of vapor pressure (VP), a measure of volatility  
  - **MP** – Melting Point  
  - **BP** – Boiling Point  
  - **Log BCF** – Bioconcentration Factor, describing chemical accumulation in organisms  
  - **Log S** – Aqueous Solubility  
  - **Log P** – Lipophilicity (partition coefficient between *n*-octanol and water). In chemistry, *logP* quantifies how well a neutral compound dissolves in a nonpolar solvent (like octanol) compared to water.

- **Other folders**  
  - `Data Statistics/` – Exploratory analysis and summary statistics  
  - `Descriptor Generators/` – Colab notebooks to generate molecular descriptors  
  - `Models/` – Colab notebooks for training and evaluating machine learning models  

---

## 🚀 Running the Workflows

All experiments are implemented as **Google Colab notebooks**.  
You can open any notebook directly in Colab and execute cells sequentially to reproduce the results.

Example:  
```text
Data Files/Descriptor Generators/GenerateDescriptorsData.ipynb
