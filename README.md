# Historical and sociocultural analysis of film genre trends: Impact of world events and box office successes

## Abstract: 

This project explore the historical evolution of film genres, examining how societal and historical contexts influence trends in cinema. 
By analyzing the impact of major world events, we seek to understand how periods of conflict, economic upheaval, or stability shape audience preferences and genre popularity. For instance, we will investigate whether genres like war films or escapist comedies surge during turbulent times. Additionally, we will assess the influence of American culture and globalization on international cinema, examining how trends in U.S. films impact global production. 
Lastly, we’ll analyze how box office successes shape genre proliferation, investigating if highly successful films lead to a rise in similar productions. This research aims to uncover the interplay between cinema, historical context, and cultural diffusion, telling a broader story of how global and national phenomena shape what audiences see on screen.

## Research Questions:

1) How do major historical events influence trends in cinema genres?
Which genres gain or lose popularity during historical periods such as wars or economic crises?
2) To what extent do American culture and globalization shape genre preferences worldwide?
3) How do box office successes affect the proliferation of specific genres, and over what time span?

## Proposed additional datasets (if any):

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

-> 04/11: Have found a complementary dataset containing the historical events we want to analyze. Consider its use: for example, can we recognize keywords like “war” or “politics”, and check whether our analysis method is feasible? If not, determine whether it's possible to create this dataset ourselves by selecting the relevant events.

-> 05/11: Clean up the data and additional dataset and assess the feasibility of the project by carrying out preliminary analyses to check data quality, accuracy of genre extractions and possible correlations with historical events.

-> 08/11: Have coded, plotted and analysed as many things as possible before asking the TA questions about what they think.

## Organization within the team:

- 01/11: (All members) Meeting of all members to present and discuss ideas. Choice of a common idea, then refinement according to the interests and desired impact of the project.

- 03/11: (Sarah) Writing of the README, including the title, abstract, research questions, informations about the complementary datset, methods and preliminary timetable. Reflection on the general structure of the project.

- 04/11: (Laurine and Sarah) Selection, exploration and reflection on a complementary dataset. Discussion of the possibilities for enrichment and the usefulness of this dataset in answering the research questions.
(Sarah) Structuring the project by adding files to the src and test folders, creating empty shells for each cleaning and vectorisation function. These are code skeletons containing function definitions that will be completed later, but which already show a clear intention of the data processing steps. Organising the results.ipynb notebook, integrating the calls to these functions while clearly detailing our intentions, in order to document the data processing process and ensure a fluid understanding of the data pipeline.

-[Complete...]

- 14/11:
Revision of the notebook and consolidation of the results (all members): Checking the consistency of the analyses, adding text descriptions to explain each section of the notebook. Final check of the visualisations and adjustment of the analyses according to the team's comments.

- 15/11: Finalisation of the project. Final check of the GitHub repository (README, file and code structure). Submission of the project before midnight.

## Questions for TAs (optional): 

- Any recommendations on specific natural language processing methods for detecting correlations between events and genres?
- Advice on how to interpret correlations between box office success and genre proliferation (e.g.: criteria for measuring “success”)?
