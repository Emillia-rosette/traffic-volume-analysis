## Traffic Volume Analysis - UK Regions
===================================

### Executive Summary

Traffic congestion is a growing issue in urban areas, leading to longer travel times, increased fuel consumption, and higher environmental pollution. This project focuses on analyzing traffic patterns across UK regions, examining factors like road type, road condition, and road class. The aim is to provide a comprehensive analysis of traffic patterns and trends to help policymakers make informed decisions regarding traffic management and infrastructure investments.

### Problem Statement

The primary goal of this project is to perform a detailed analysis of traffic volumes by exploring vehicle counts collected at regular intervals (monthly). By identifying patterns in vehicle counts and traffic flow dynamics, the project seeks to provide insights into traffic behavior, which can support local authorities in optimizing traffic flow, reducing congestion, and improving infrastructure.

### Data science opportunity

This project presents an opportunity to leverage historical traffic data to uncover insights into traffic patterns and volumes across UK regions. The focus is on exploring trends and patterns, identifying peak periods, and understanding the impact of various factors such as road types and traffic conditions on overall traffic volumes.

### Key takeaways

**Key Insights:**

- Seasonal trends in traffic volumes across different road types and regions.
- Analysis of traffic behavior during holidays and special events.
- Insights into how traffic volumes vary across different regions and road classifications.

**Technologies:**
- Python 
- Data visualization: Plotly and Matplotlib 

**Setup:**
- Clone repo: git clone https://github.com/brainstation-datascience/capstone-Emillia-rosette.git

**Results:**

- The analysis provides insights into the patterns of traffic volumes, helping stakeholders to identify trends and make informed decisions for traffic management and road infrastructure planning

**Future Work:**
- Incorporate real-time traffic data.
- Analyze the effect of road incidents and disruptions on traffic volumes.
- Explore models suhc Prophet, XGBoost, and LSTM for more complex patterns.


### Datasets Overview
This project uses a comprehensive traffic dataset collected from the UK Department for Transport. The dataset includes vehicle counts by road type, direction, and location.

Below is a summary of key variables used:


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


### Methodology

![Alt text](methodology.png)

### Project Structure

├── **.github/**                  # GitHub workflows and settings
├── **data/**                     # Contains datasets and processed data files
├── **docs/**                     # Documentation files for the project
├── **Emillia-rosette_Nlandu_Capstone Assets/** # Project assets like images and presentations
├── **notebooks/**                # Jupyter notebooks for data analysis
├── **references/**               # Research papers and additional references
├── **src/**                      # Source code for data processing
├── **.gitignore**                # Specifies files to be ignored by Git
├── **conda.yml**                 # Conda environment specification file
├── **methodology.png**           # Methodology flowchart image
├── **README.md**                 # Project readme file


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

