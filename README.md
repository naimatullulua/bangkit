# E-Commerce Dashboard

## Overview
This project focuses on exploring and visualizing data from the E-Commerce Public Dataset. It leverages Streamlit to create interactive visualizations that provide insights into various aspects of e-commerce, including relationships between freight value and price, transaction count based on ratings, and order count by city. The goal is to analyze the dataset comprehensively, highlighting trends, patterns, and key metrics within the e-commerce landscape.

## Data Source
The data used in this project comes from the following source:

- E-Commerce Public Dataset

## Requirements
To run this project, you need to install the following Python packages:

- Babel==2.11.0
- matplotlib==3.8.4
- numpy==1.26.4
- pandas==2.2.2
- seaborn==0.13.2
- streamlit==1.39.0

You can find the required packages listed in the `requirements.txt` file.

## Installation

### Clone the Repository
First, clone the repository:

```bash
git clone https://github.com/naimatullulua/bangkit.git
cd bangkit
```
### Create a new virtual environment
```
python -m venv venv
```
### Activate the virtual environment
```
venv\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Prepare Data
Ensure that you have the order_items_dataset.csv dan order_reviews_dataset.csv file in the same directory as dashboard.py. Adjust the file paths in dashboard.py if necessary
## Running the dashboard
```
streamlit run dashboard.py
```

