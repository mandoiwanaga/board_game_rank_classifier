# Battle of the Boards - Board game rank classification 
#### Flatiron School - Data Science Immersive Program - Mod 3 Project
John Naujoks - Mando Iwanaga
***
[Complete testing and workflow (Jupyter Notebook)](https://github.com/jnawjux/mod3_project/blob/master/final.ipynb)

[Web Scraping & API call workflow (Jupyter Notebook)](https://github.com/jnawjux/mod3_project/blob/master/bgg_scrape.ipynb)

[Stakeholder Presentation (Google Slides)](https://docs.google.com/presentation/d/1gYG9376JoFvMicMIsHURCwtKGJCtEXhjXfAyygJ4iEo/edit?usp=sharing)

[Custom functions (Python)](https://github.com/jnawjux/mod3_project/blob/master/functions.py)

***
## Project Overview
Our task for this project was to create a calssification model on data of our choosing. Further instructions and details can be found [here.](https://github.com/jnawjux/mod3_project/blob/master/project_instructions.md)

**Initial Question**: Can we classify whether a game will score well on BoardGameGeek.com?
* We built our model and process assuming we were working as a consulting firm contracted by an entertainment company, interested in getting into the board game business.
* We obtained our data through a mix of web scraping and API calls to get data from the past 4 years of games. 
* Our goal was working with classification, so we made a binary feature to represent whether a game was within the top 25% of rated games and used that as our target. 
* We tried several classification models  to find out best fitting one, including testing hyperparameter tuning. 
* Our final model uses a mix of features (including average play time and game mechanics) to achieve the best score on our key metrics (focused on Log Loss and ROC AUC Score).

