# Historical and sociocultural analysis of film genre trends: Impact of world events and box office successes

## Abstract: 

This project explore the historical evolution of film genres, examining how societal and historical contexts influence trends in cinema. 

By analyzing the impact of major world events, we seek to understand how periods of conflict, economic upheaval, or stability shape audience preferences and genre popularity. For instance, we will investigate whether genres like war films or escapist comedies surge during turbulent times. Additionally, we will assess the influence of American culture and globalization on international cinema, examining how trends in U.S. films impact global production. 

Lastly, we’ll analyze how box office successes shape genre proliferation, investigating if highly successful films lead to a rise in similar productions. This research aims to uncover the interplay between cinema, historical context, and cultural diffusion, telling a broader story of how global and national phenomena shape what audiences see on screen.

## Research Questions:

* How do major historical events influence trends in cinema genres?
Which genres gain or lose popularity during historical periods such as wars or economic crises?
* To what extent do American culture and globalization shape genre preferences worldwide?
* How do box office successes affect the proliferation of specific genres, and over what time span?

## Proposed additional dataset:

We have integrated a dataset on major historical events, the World Important Events: Ancient to Modern dataset. Key features include:

Type of Event: Categorization of events (e.g., wars, revolutions, economic crises).
Impact and Outcome: Information on the severity and consequences of events.
And other information such as the Name of Incident, the date, the country, Affected Population and Important Person/Group Responsible.
This dataset covers a variety of periods, from ancient civilisations to the modern era, and includes major events such as wars, economic crises, political revolutions and technological advances.
Integrating this historical information will allow us to cross-reference film release dates with historical periods to investigate correlations between world events and genre trends. For instance, we can analyze whether war films increase during conflicts or comedies dominate during economic instability.

The dataset's columns, such as ‘Type of Event’, ‘Impact’ and ‘Outcome’, will allow us to group and classify events into categories (e.g. wars, social advances) and analyse their potential influence on the types of films produced at different times.

This additional dataset will provide a solid basis for enriching our analysis, helping us to understand how historical events shape audience preferences and influence film production.

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

6) Impact of Box Office Success:
Identify successful films by genre and assess how they influence the proliferation of similar genres over subsequent years.

7) NLP for Historical Context:
Utilize natural language processing (NLP) techniques to detect historical themes and events in film summaries, establishing correlations with genre trends.

8) Visualization and Insights:
Create visualizations such as timelines, stacked area charts, and heatmaps to summarize findings and present them intuitively.

## Proposed timeline

-> 01/11: Choice of subject and refining.

-> 05/11: Have found a complementary dataset containing the historical events we want to analyze. Consider its use: for example, can we recognize keywords like “war” or “politics”, and check whether our analysis method is feasible? If not, determine whether it's possible to create this dataset ourselves by selecting the relevant events.

-> Until 15/11 : Data Handling and Preprocessing & Initial Exploratory Data Analysis (EDA)

-> 15/11: Finalize visualizations, results, and repository structure. Submit the project.

## Organization within the team:

- 01/11: (All members) Initial meeting to present and discuss ideas. Selection of a common project topic, followed by refinement based on team interests and project goals.

- 04/11: (Laurine) Exploration and selection of the complementary dataset.
  
- 03/11 - 06/11: (Sarah) Drafting the README, including the title, abstract, research questions, information about the complementary dataset, methods, and a preliminary timeline. Reflection on the general structure of the project. Organized the project structure by creating files and code skeletons in src folder, and preparing the results notebook with a timeline and clear documentation for data processing steps.

- 07/11 - 14/11:

(Lucile) Preprocessed the movie dataset and conducted a case study on war movies.
(Diane) Focused on the exploratory data analysis (EDA) of the movie dataset.
(Laurine) Preprocessed the historical dataset, prepared it for integration and started a case study on historical events in India.
(Nouchine) Helped structure the project, documented progress for each step, and contributed to the preliminary analysis of the datasets.

- 14/11: (All members) Reviewed the notebook and consolidated results. Ensured consistency in analyses, added descriptive text for each section of the notebook, and finalized visualizations based on team feedback.Reviewed the notebook and consolidated results. Ensured consistency in analyses, added descriptive text for each section of the notebook, and finalized visualizations based on team feedback.

-15/11: (Sarah) Conducted a full review of the project, made minor adjustments and corrections, and revised the README for submission. 

## Questions for TAs (optional): 

- Any recommendations on how to regroup type of events and movie genres?
- Is using NLP techniques to detect historical themes and events in film summaries a good idea? If not, should we only focus on the movie release date and the date of event?
