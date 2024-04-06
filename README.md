# Iris Explore
## Overview
It is a website showing a dataset of leaves informations of Iris. It also includes analysis applications to find out interesting insights about iris's sepal and retal in the three species.

## Getting started

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

streamlit run app.py

```

## Lessons Learned
- How to access dataset ```.csv``` in internet.
- Use sidebar to divide screening widges and main analytical charts.
- The page logic consists of two parts: 
    1.  Creating the filter criteria with ```input widges``` (slider, dropdown, select widgets)
    2. Connecting the filter to the dataset with ``` if ```conditoin.
- Add ```color="species"``` in scatter charts to improve data visualization, like differing three species in three colors.
- Use ```isin()```when want to make a multiselect.

## Question
- I attempted to use columns to display charts, but I found that the total width of the two columns exceeds the screen's width, requiring me to slide to view. Therefore, I'm wondering how to adjust the size of the charts to optimize the layout?
## Todo
- I want to add a ```reset```button for users to clean all the screenings in one click instead of one by one, to improve the user experience.