## Traffic Trends Across UK Regions
=========================

### Executive Summary

Traffic congestion is a growing issue in urban areas, leading to longer travel times, increased fuel consumption, and higher environmental pollution. This project leverages a time series approach to analyze and forecast traffic patterns across UK regions, examining factors like road type, road condition, and road class. The project aims to provide a comprehensive analysis of traffic patterns and trends, enabling policymakers to make informed decisions regarding traffic management and infrastructure investments.

### Problem Statement

The project's goal is to accurately predict traffic volumes by analyzing vehicle counts collected at regular intervals (monthly). By identifying patterns in vehicle counts and traffic flow dynamics, we aim to help local authorities optimize traffic flow, reduce congestion, and improve infrastructure. The project addresses the challenge of predicting traffic volumes across different regions using time series modeling to inform better traffic management and infrastructure planning.


### Data science opportunity
This project presents a data opportunity to leverage historical traffic patterns for predictive modeling, enabling more informed decisions in traffic management, congestion reduction, and infrastructure optimization. By applying data science techniques, the project aims to build models that forecast future traffic volumes based on historical data, helping stakeholders identify trends and optimize resources.

### Key takeaways

**Key Models:**

- Naive Model: SMAPE of 82.37%
- Prophet: SMAPE of 99.07%
- XGBoost: SMAPE of 82.93% (best performance)

**Features Used:**
- Road types, Year averages, Lagged traffic volumes, and Date-based features like day of the week.

**Technologies:**
- Python (pandas, XGBoost, Prophet, matplotlib)

**Setup:**
- Clone repo: git clone https://github.com/brainstation-datascience/capstone-Emillia-rosette.git

**Results:**

- XGBoost performed much better than the other two models, especially with added features like road types and lagged traffic data.

**Future Work:**
- Add weather, real-time data.
- Explore deep learning models for more complex patterns (e.g., LSTM).


### Datasets Overview
This project uses a comprehensive traffic dataset collected from the UK Department for Transport. The dataset includes vehicle counts by road type, direction, and location. Below is a summary of key variables used:

## Datasets Overview
This project uses a comprehensive traffic dataset collected from the UK Department for Transport. The dataset includes vehicle counts by road type, direction, and location. Below is a summary of key variables used:

| **Variable Name**           | **Description**                               |
|-----------------------------|-----------------------------------------------|
| `count_point_id`            | Unique ID for the traffic count point          |
| `direction_of_travel`       | Direction of traffic (North, South, East, West)|
| `year`                      | Year of traffic count                         |
| `count_date`                | Date of traffic count                         |
| `road_name`                 | Name of the road (e.g., M25, A3)              |
| `road_category`             | Road classification (Motorway, A-road, etc.)  |
| `cars_and_taxis`            | Vehicle counts for cars and taxis             |
| `all_motor_vehicles`        | Total vehicle counts (all types)              |

For more detailed documentation, refer to the [UK Traffic Data Documentation](https://storage.googleapis.com/dft-statistics/road-traffic/all-traffic-data-metadata.pdf).


### Demo
<!-- 
... Show your work:
...     Data visualisations
...     Interactive demo (e.g., stremlit app)
...     Short video of users trying out the solution -->

![alt text](<Emillia-rosette_Nlandu_Capstone Assets_Screenshots/volume.png>)
text
### Methodology

![Alt text](methodology.png)

### Project Structure
│
├── **.devcontainer/**            # Development container configuration
├── **.github/**                  # GitHub workflows and settings
├── **.ipynb_checkpoints/**       # Jupyter notebook checkpoints
├── **.vscode/**                  # VS Code workspace settings
├── **data/**                     # Contains datasets and processed data files
├── **docs/**                     # Documentation files for the project
├── **Emillia-rosette_Nlandu_Capstone Assets/** # Project assets like images and presentations
├── **model/**                    # Folder for storing trained models and artifacts
├── **notebooks/**                # Jupyter notebooks for data analysis and modeling
├── **references/**               # Research papers and additional references
├── **src/**                      # Source code for data processing and modeling
├── **.gitignore**                # Specifies files to be ignored by Git
├── **conda.yml**                 # Conda environment specification file
├── **Correlation.png**           # Correlation plot image
├── **data_dictionary.md**        # Data dictionary for the project
├── **essex_map.json**            # GeoJSON file for mapping
├── **final_presentation.pdf**    # Final project presentation (PDF)
├── **final_presentation.pptx**   # Final project presentation (PowerPoint)
├── **LICENSE**                   # License file for the project
├── **Makefile**                  # Makefile for project automation
├── **methodology.png**           # Methodology flowchart image
├── **notebooks.zip**             # Zipped folder of project notebooks
└── **README.md**                 # Project readme file


### Credits & References

- Department for Transport. (n.d.) All Traffic Data Metadata. Available at: https://storage.googleapis.com/dft-statistics/road-traffic/all-traffic-data-metadata.pdf (2024).
- Williams, D. (2023) 'Sadiq Khan says London's congestion problems are improving despite complaints of traffic jams', Daily Mail, 5 August. Available at: https://www.dailymail.co.uk/news/article-13566731/Sadiq-Khan-London-congestion-roads-traffic.html (Accessed: 4 August 2024)

#### Setup Instructions

1. Clone the repository to your local machine.
git clone https://github.com/Emillia-rosette/traffic-volume-prediction.git

2. Navigate to the project diretcory 
cd traffic-volume-prediction

3. Create a conda environment and activate it
conda env create -f conda.yml
conda activate <your-env-name>

4. Install the project dependencies
pip install -r requirements.txt

5. Run the project notebooks
python notebooks/01-data-loading-cleaning.ipynb (for example)

6. Launch the Streamlit app
streamlit run notebooks/streamlit_prophet.py

7. View the Streamlit app in your browser
http://localhost:8501

