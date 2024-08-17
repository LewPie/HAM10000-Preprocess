# Dataset HAM10000 Preprocessing

This project provides a script to preprocess the HAM10000 dataset, organizing it into a train and test directory structure with subdirectories for each disease category.

## Project Structure

The output structure will be organized as follows:

data3/\
│\
├── train/\
│   ├── akiec/\
│   ├── bcc/\
│   └── ...\
│\
└── test/\
    ├── akiec/\
    ├── bcc/\
    └── ...

## Preprocessed Data

If you prefer to use preprocessed data, you can download it from the following link:

- [Preprocessed HAM10000 Data](https://drive.google.com/file/d/1Q0MwLhwZ1y8orO4kIakpxJl6hU9bDeip/view?usp=drive_link)

## Prerequisites

- Python 3.x
- Required Python libraries: `pandas`, `scikit-learn`

You can install the required libraries using pip:

```bash
pip install pandas scikit-learn
```

## Usage

1. **Download and prepare the HAM10000 dataset:**
   - If you want to preprocess the data yourself, ensure you have the HAM10000 dataset and place it in a directory. The dataset should include a CSV file with metadata and image files in an `images` folder.

2. **Edit the script:**
   - Open the `preprocess.py` script and set the `dataset_path` variable to the location of your HAM10000 dataset.

3. **Run the preprocessing script:**
   - Execute the script with Python:

   ```bash
   python preprocess.py
   ```

   This will create the `data3` directory with `train` and `test` subdirectories, each containing folders for each disease category.

## Script Details

The script performs the following steps:

1. Reads the metadata CSV file to obtain disease categories.
2. Creates `train` and `test` directories if they do not exist.
3. Creates subdirectories for each disease category within `train` and `test`.
4. Splits the dataset into training and testing sets (80% train, 20% test).
5. Copies the images into the respective directories based on their disease category.

## Acknowledgements

- The HAM10000 dataset is provided by [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000).
- The preprocessed data is available for download [here](https://drive.google.com/file/d/1Q0MwLhwZ1y8orO4kIakpxJl6hU9bDeip/view?usp=drive_link).