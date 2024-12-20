# Historical and sociocultural analysis of film genre trends: Impact of world events and box office successes

## Data Story:

https://noushskadoush.github.io/adatched_data_story/

## Abstract: 

This project explores the historical evolution of film genres, analyzing how societal and historical contexts have influenced trends in cinema.

By analyzing the impact of major world events, we seek to understand how periods of conflict, economic upheaval, or stability shape genre popularity. 
For instance, we will investigate whether genres like war films or escapist comedies surge during turbulent times.

The project's functionality is encapsulated in modular files, with key functions housed in src/utils/data_cleaning, src/utils/appendix and src/utils/visualization scripts for data handling and visual output.

To visualize our research and results, one can run the notebook results.ipynb and set up the environment using pip install -r pip_requirements.txt.

## Research Questions:

* How do major historical events influence trends in cinema genres?
* Which genres gain or lose popularity during historical periods such as wars or economic crises?
* Do these events translate in Immediate Spike or a Long-Term Influence on genre trends?

## Proposed additional dataset:

Initially, we integrated the <u>*World Important Events: Ancient to Modern*</u> dataset to explore correlations between historical events and film genre trends. While it provided comprehensive coverage of events, its scope and complexity posed challenges for analysis and interpretation in our specific context.

To address this, we created a new dataset manually, with the assistance of a language model (LM). This tailored dataset focuses on a curated selection of historical events that are more directly relevant to our study. Key features include:

Event Name: The name of the historical event.
Year: The year of the event.
Location: The primary geographical region affected.
Impact Type: Categorized as "Positive," "Negative," or "Mixed."
Description: A brief explanation of the event's relevance to cultural or cinematic trends.
This approach allowed us to streamline the analysis, focusing on fewer, highly relevant events while maintaining sufficient detail for meaningful insights. 

This new dataset has become a cornerstone of our project, enabling us to overcome previous limitations and better align our analysis with the project's objectives. Both will be used, according to the needs of the analysis.

## Methods

We will employ the following methods to analyze the data:

1) Data Cleaning:
Prepare both datasets by formatting data, eliminating outliers, and removing unnecessary columns to ensure consistency and reliability for further analysis.

2) Exploratory Data Analysis (EDA):
Conduct univariate and bivariate analyses to understand the distributions, relationships, and preliminary patterns within the data. This step will help refine our research questions and hypotheses.

3) Manual Identification of interesting pairs of events and genres, and temporal analysis of the corresponding genres over time to evaluate the impact of events.

4) Hypothesis testing using statistical tools and modeling for the most relevant pairs.

5) Visualization and Insights:
Create visualizations such as timelines, stacked area charts, and heatmaps to summarize findings and present them intuitively.

## Proposed timeline

⟶ 01/11: Choice of subject and refining.

⟶ 05/11: Have found a complementary dataset containing the historical events we want to analyze. Consider its use: for example, can we recognize keywords like “war” or “politics”, and check whether our analysis method is feasible? If not, determine whether it's possible to create this dataset ourselves by selecting the relevant events.

⟶ Until 15/11 : Data Handling and Preprocessing & Initial Exploratory Data Analysis (EDA). Final visualizations and results for P2.

⟶ 26/11: Discuss feedback and reorganize code structure. 

⟶ Until 12/12: New hypothesis testing, statistical tests implemented. Identification of the relevant events-genre pairs and the story we want to convey.

⟶ Until 20/12 : Writing this story in details in the notebook and making it interactive on the website for P3.

## Organization within the team:

▪️ 01/11: (All members) Initial meeting to present and discuss ideas. Selection of a common project topic, followed by refinement based on team interests and project goals.

▪️ 04/11 - 14/11:: (Laurine):  Exploration and selection of the complementary events dataset. Preprocessing and cleaning of the latter. 

(Diane, Sarah, Nouchine) : Structuring the project and steps to follow.

(Diane, Lucile) : Focused on data cleaning and exploratory data analysis of the movie dataset, including handling missing values, identifying outliers and duplicates, formatting, and examining distributions. 

(Lucile) : Start of analysis on war movies

(All) : preliminary analysis of the dataset, visualizations 


▪️ 01/12 - 09/12: 

(Laurine) Focused on cleaning and optimizing the preprocessing pipeline, compressing datasets, creating helper functions and exploring trends and correlations in event data. Started cases studies and first identification of several pairs of events and genres.

(Lucile) Reorganized the documentation for better clarity  and performed statistical analyses (ANOVA test and linear regression) on war movies, suggesting these methods could inspire future analyses.

▪️ 09/12 - 20/12: 

(Sarah) Worked on creating an initial global plot to provide a general overview and set the stage for transitioning into more specific analyses. Reformated the project structure.
        Created a more relevant historical dataset manually with the help of a language model to overcome limitations of the original dataset and began conducting analyses and general visualizations to represent         both datasets together. Creation of additional plots to highlight the most relevant things for the website.

(Laurine and Lucile) : further statistical analyses on case studies.

(Diane) : Further investigation to identify new pairs of genres and events to refine the analysis. Investigated their relationship and created functions for the visualization, adding also statistical analyses.

(Nouchine) Creation of the website's framework. Wrote the Data Story website and filled it with text and figures from the notebook.

(Diane, Lucile, Laurine, Sarah) Conducted the analysis of the remaining event-genre pairs. 

▪️ 20/12: (All members) Reviewed the work and made final adjustments for submission.
