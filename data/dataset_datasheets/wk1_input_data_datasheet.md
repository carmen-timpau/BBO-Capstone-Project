**Datasheet V.1.**

<br>


**Dataset File Name:** [wk1_input_data.pkl](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/wk1_input_data.pkl)

**Dataset Description:** BBO Capstone Week 1 Input Dataset = Initial Datasets provided for all 8 Black-Box Functions

<br>


**Motivation:**

This dataset was created to serve as input for the [Main Execution Script of the BBO Week 1 Full ML Bayesian Optimisation Pipeline](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/main.py), to generate the first query points predicted _via_ a Bayesian Optimisation pipeline for submission during Week 1 of the BBO Capstone Project. This project represents my work as a participant in the Black-Box Optimisation Challenge hosted by Imperial College London Executive Education, as part of their 6-month Professional Certificate in Machine Learning and Artificial Intelligence joint programme, which took place between February – September 2026. The overarching aim of this project is to develop ML algorithms in Python that maximise the 8 expensive-to-query black-box functions.

A technical summary of the specific Bayesian Optimisation ML pipeline which used this dataset as an input can be found in [BBO Week 1 - Bayesian Optimisation Strategy Summary](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/strategy_summary.md).

<br>


**Composition:**  

This is now a static dataset saved as a .pkl file, which stores all initial datasets that have been provided at the beginning of this project by Imperial College London for all 8 unknown objective functions. 

The **structure**, **size** and **format** of this dataset (saved as a .pkl file) is as follows:

[wk1_input_data.pkl](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/wk1_input_data.pkl): dict
```text
|── "function_1": dict
|   |── "x”: np.ndarray, shape (10, 2)   # input coordinates
|   └── "y”: np.ndarray, shape (10,)     # function outputs
|
|── "function_2": dict
|   |── "x”: np.ndarray, shape (10, 2)
|   └── "y”: np.ndarray, shape (10,)
|
|── "function_3": dict
|   |── "x”: np.ndarray, shape (15, 3)
|   └── "y”: np.ndarray, shape (15,)
|
|── "function_4”: dict
|   |── "x”: np.ndarray, shape (30, 4)
|   └── "y”: np.ndarray, shape (30,)
|
|── "function_5”: dict
|   |── "x”: np.ndarray, shape (20, 4)
|   └── "y”: np.ndarray, shape (20,)
|
|── "function_6”: dict
|    |── "x”: np.ndarray, shape (20, 5)
|    └── "y”: np.ndarray, shape (20,)
|
|── "function_7”: dict
|    |── "x”: np.ndarray, shape (30, 6)
|    └── "y”: np.ndarray, shape (30,)
|
|── "function_8”: dict
|    |── “x”: np.ndarray, shape (40, 8)
|    └── "y”: np.ndarray, shape (40,)
```
There are no gaps within this dataset.

<br>


**Collection Process:**

The datasets within this .pkl file have been provided by Imperial College London as the initial datasets of the 8 unknown objective functions, as part of the Black-Box Optimisation Challenge.

<br>


**Preprocessing and Uses:**

No preprocessing transformations have been applied to the contents of this dataset. This dataset contains the raw data which was directly provided by Imperial College London. The data was obtained by querying the 8 black-box functions investigated in this project, at the respective high-dimensional input points to obtain their true output values and aid in Bayesian Optimisation pipeline developments as part of this BBO capstone project.

As this is a static dataset now that the BBO capstone project has ended (September 2026), the intended further use of this dataset is only as an input dataset for ML pipeline validation purposes. 
This dataset is inappropriate for use in any other projects, or in any other ways other the one stated above, as it is strictly relevant for these specific black-box functions investigated within this project, at the exact stage of this project (Week 1) when it was used.

<br>


**Terms of Use, Distribution and Maintenance:** 

The dataset is available to download here: [wk1_input_data.pkl](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/wk1_input_data.pkl).

This dataset may only be used as stated in the above section. Attribution must be provided whenever this dataset, or any portion of it, is cited, used for analysis, or incorporated into any derivative materials.

This is a static dataset – it is no longer maintained, and it will not be modified in the future. 

The original creator of the datasets within this .pkl file is Imperial College London. 

The original creator of this .pkl file is Carmen-Mihaela Timpau and can be contacted for any project-related queries, including to request more information about this dataset and its use. Contact details can be found at the bottom of the [README.md](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/README.md) file of this repository.
