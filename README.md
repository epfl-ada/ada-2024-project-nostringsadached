# Historical and sociocultural analysis of film genre trends: Impact of world events and box office successes

## Abstract: 

This project aims to explore the historical evolution of film genres, examining how societal and historical contexts influence trends in cinema. 
By analyzing the impact of major world events, we seek to understand how periods of conflict, economic upheaval, or stability shape audience preferences and genre popularity. For instance, we will investigate whether genres like war films or escapist comedies surge during turbulent times. Additionally, we will assess the influence of American culture and globalization on international cinema, examining how trends in U.S. films impact global production. 
Lastly, we’ll analyze how box office successes shape genre proliferation, investigating if highly successful films lead to a rise in similar productions. This research aims to uncover the interplay between cinema, historical context, and cultural diffusion, telling a broader story of how global and national phenomena shape what audiences see on screen.

## Research Questions:

- How do major historical events influence genre trends in cinema?
- Are American culture and globalization changing genre preferences worldwide? How do these influences manifest themselves?
- To what extent do box office successes affect the proliferation of a specific genre? How long after a success do similar films gain in popularity?
- Which genres tend to increase or decrease in popularity during different historical periods (e.g., wars, economic crises)?

## Proposed additional datasets (if any):

To complete our analysis, we plan to integrate an additional dataset on major historical events, such as the ‘World Important Events - Ancient to Modern’ dataset. This dataset covers a variety of periods, from ancient civilisations to the modern era, and includes major events such as wars, economic crises, political revolutions and technological advances.

Integrating this historical information will allow us to cross-reference film release dates with specific periods of significant events to explore potential correlations between historical context and the popularity of film genres. For example, we can examine whether war films are produced more during or after periods of conflict, or whether comedies gain in popularity during periods of economic crisis.

The dataset's columns, such as ‘Type of Event’, ‘Impact’ and ‘Outcome’, will allow us to group and classify events into categories (e.g. wars, social advances) and analyse their potential influence on the types of films produced at different times.

This additional dataset will provide a solid basis for enriching our analysis, helping us to understand how historical events shape audience preferences and influence film production.

## Methods

We will use the following methods to analyse the data:

1) Temporal analysis of genres: Visualise the evolution of genres over time, identifying periods of high popularity for certain genres.
2) Extraction of trends and correlations: Use natural language processing (NLP) techniques to recognise historical themes and events mentioned in film summaries, and establish correlations with genres.
3) Analysing the influence of box office success: Identify successful films by genre, then observe the popularity of similar genres in subsequent years.
4) Visualisation and interpretation: Present visualisations (stacked area graphs, timelines, heatmaps, etc.) to make the results easy to interpret.

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
