# Historical and sociocultural analysis of film genre trends: Impact of world events and box office successes

## Abstract: 

This project explores the historical evolution of film genres, analyzing how societal and historical contexts have influenced trends in cinema.

By analyzing the impact of major world events, we seek to understand how periods of conflict, economic upheaval, or stability shape audience preferences and genre popularity. For instance, we will investigate whether genres like war films or escapist comedies surge during turbulent times. 

## Research Questions:

* How do major historical events influence trends in cinema genres?
* Which genres gain or lose popularity during historical periods such as wars or economic crises?

## Proposed additional dataset:

Initially, we integrated the <u>*World Important Events: Ancient to Modern*</u> dataset to explore correlations between historical events and film genre trends. While it provided comprehensive coverage of events, its scope and complexity posed challenges for analysis and interpretation in our specific context.

To address this, we created a new dataset manually, with the assistance of a language model (LM). This tailored dataset focuses on a curated selection of historical events that are more directly relevant to our study. Key features include:

Event Name: The name of the historical event.
Year: The year of the event.
Location: The primary geographical region affected.
Impact Type: Categorized as "Positive," "Negative," or "Mixed."
Description: A brief explanation of the event's relevance to cultural or cinematic trends.
This approach allowed us to streamline the analysis, focusing on fewer, highly relevant events while maintaining sufficient detail for meaningful insights. 

This new dataset has become a cornerstone of our project, enabling us to overcome previous limitations and better align our analysis with the project's objectives.

## Methods

We will employ the following methods to analyze the data:

1) Data Cleaning:
Prepare both datasets by formatting data, eliminating outliers, and removing unnecessary columns to ensure consistency and reliability for further analysis.

2) Exploratory Data Analysis (EDA):
Conduct univariate and bivariate analyses to understand the distributions, relationships, and preliminary patterns within the data. This step will help refine our research questions and hypotheses.

3) Preliminary Studies:
Perform focused analyses on specific subsets, such as war movies and films from India, to uncover early trends and insights that might inform broader analyses.

4) Temporal Analysis of Genres:
Track the evolution of genres over time, identifying key periods of popularity or decline.

5) Correlation Analysis:
Investigate relationships between genre trends, major historical events, and box office performance using statistical methods.

6) Visualization and Insights:
Create visualizations such as timelines, stacked area charts, and heatmaps to summarize findings and present them intuitively.

## Proposed timeline

⟶ 01/11: Choice of subject and refining.

⟶ 05/11: Have found a complementary dataset containing the historical events we want to analyze. Consider its use: for example, can we recognize keywords like “war” or “politics”, and check whether our analysis method is feasible? If not, determine whether it's possible to create this dataset ourselves by selecting the relevant events.

⟶ Until 15/11 : Data Handling and Preprocessing & Initial Exploratory Data Analysis (EDA)

⟶ 15/11: Finalize visualizations, results, and repository structure. Submit the project milestone P2.

⟶ 26/11: Discuss feedback and reorganize code structure. 

⟶ 09/12: Restructured our repository (compressed formats, isolated the preprocessing, made everything clearer).

⟶ Until 12/12: New hypothese testing, statistical tests implemented. 

⟶ 16/12: Have a clear, coherent idea of the story we want to convey.

## Organization within the team:

▪️ 01/11: (All members) Initial meeting to present and discuss ideas. Selection of a common project topic, followed by refinement based on team interests and project goals.

▪️ 04/11: (Laurine) Exploration and selection of the complementary dataset.
  
▪️ 03/11 - 06/11: (Sarah) Drafting the README, including the title, abstract, research questions, information about the complementary dataset, methods, and a preliminary timeline. Reflection on the general structure of the project. Organized the project structure by creating files and code skeletons in src folder, and preparing the results notebook with a timeline and clear documentation for data processing steps.

▪️ 07/11 - 14/11:

(Lucile) Preprocessed the movie dataset (columns formatting, missing values,) and conducted a case study on war movies. Analyzed the distribution of movies across different countries and genres.

(Diane) Focused on data cleaning and exploratory data analysis of the movie dataset, including handling missing values, identifying outliers and duplicates, formatting, and examining distributions. Also contributed to structuring the project, exploring the genres and worked on the appendix.

(Laurine) Preprocessed the historical dataset, prepared it for integration and started a case study on historical events in India. Completed the '.gitinore' and 'requirements' files.

(Nouchine) Structured the project, documented progress for each step, and contributed to the preliminary analysis of the datasets. Conducted the bivariate analysis of events around the world.

▪️ 14/11: (All members) Reviewed the notebook and consolidated results. Ensured consistency in analyses, added descriptive text for each section of the notebook, and finalized visualizations based on team feedback.Reviewed the notebook and consolidated results. Ensured consistency in analyses, added descriptive text for each section of the notebook, and finalized visualizations based on team feedback.

▪️ 15/11: (Sarah and Diane) Conducted a full review of the project, made minor adjustments and corrections, and revised the README for submission. 

▪️ 01/12 - 09/12: 

(Laurine) Focused on cleaning and optimizing the preprocessing pipeline, compressing datasets, creating helper functions (e.g., for boxplots and geopandas), and exploring trends and correlations in event data

(Lucile) Reorganized the documentation for better clarity  and performed statistical analyses (ANOVA test and linear regression) on war movies, suggesting these methods could inspire future analyses.

▪️ 16/12: 

(Lucile) Lucile continued the statistical analyses, building on Laurine's case study, by applying methods like ANOVA tests and linear regression to deepen the insights.

(Diane) Investigated the manual identification of event-genre pairs to refine the analysis.

(Sarah) Created a more relevant historical dataset manually with the help of a language model to overcome limitations of the original dataset and began conducting analyses and general visualizations to represent both datasets together. Reorganized the notebook by structuring methods into the appendix and improving transitions between sections for better flow. Updated the README file.

