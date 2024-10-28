# ETL Pipelines Repository

Welcome to the ETL Pipelines Repository! This project contains a collection of Python scripts that define various Extract, Transform, Load (ETL) pipelines, each utilizing different data sources and transformation techniques.

## Table of Contents

- [Overview](#overview)
- [Pipelines](#pipelines)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Overview

This repository showcases several ETL pipelines designed to extract data from multiple sources, perform various transformation techniques, and load the cleaned data into designated destinations. Each pipeline is implemented as a separate Python file, allowing for easy understanding and modification.

## Pipelines

1. **Airflow_Pipeline_ETL_Check.py**
   - **Source**: web server access log
   - **Transformations**: download, transform to CSV, capitalize data
   - **Destination**: save as a CSV file

2. **Airflow_Pipeline_ETL_Daily.py**
   - **Transformations**: selecting specified fields of data, converting text file to CSV

3. **Airflow_Pipeline_ETL_transform.py**
   - **Source**: text file
   - **Transformations**: download, select specified fields of data, capitalize, compress the data

4. **Airflow_Pipeline_ETL.py**
   - **Transformations**: transform to CSV
   - **Destination**: save as a CSV file

5. **ETL_Project.py**
   - **Source**: zip file
   - **Transformations**: unzip file, extracting from CSV, TSV, fixed-width file, selecting specified fields of data, consolidating data
   - **Destination**: save as CSV

## Technologies Used

- Python, Shell Scripting
- Apache Airflow, Apache Kafka
- DAG, Bash Operator, Python Operator

## Installation

To run the ETL pipelines, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ETL-Data-Pipeline.git
