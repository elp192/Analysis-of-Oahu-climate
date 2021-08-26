# Analysis of Oahu's climate
## Project Overview
### Background
The [hawaii.sqlite](https://github.com/elp192/Surfing/blob/3a9586527e67f052c1907bc453e387250a8a6433/hawaii.sqlite) is a data source that includes two tables (i.e., measurement and station). The measurement table consists of 5 columns (i.e., id, station, date, prcp, and tobs) and 19550 rows. The station table includes 6 columns (i.e., id, station, name, latitude, longitude, elevation) and 9 rows (number of stations). The data was gathered from 2010 to 2017. Analysis of climate in Oahu, Hawaii, using this dataset helps us to undrestand whether opening the surf and ice cream shop is economical during whole months of the year.
### Project Overview
This project aims to analyze the weather of Oahu, Hawaii, to understand whether the weather in different months of the year (e.g., June and December) could influence the start of new business in this region (i.e., opening the surfboards and ice cream shop).<br>
The following resources are used to perform the analysis:<br>
Software: Python (version 3.8.8), Jupyter Notebook, SQLite
Tools: SQLALchemy, DB Browser for SQLite
## Results
In this section, temperature and precipitation levels for June and December are compared.

**Determine June and December temperature** (Figure 1)<br>
- The number of available data for June (1700 data) is more than December (1517 data).<br>
- The average temperatures in June and December are 74.94 °F and 71.04 °F, respectively.<br>
- The medians of temperature in June and December are 75 °F and 71 °F, respectively.<br>
- The spread of temperatures in December (std=3.74) is more than in June (std=3.25).<br>
- The maximum temperatures in June and December are 84 °F and 83 °F, respectively.<br>
- The minimum temperatures in June and December are 64 °F and 56 °F, respectively.<br>
- The first quartiles of temperatures in June and December are 73 °F and 69 °F, respectively.<br>
- The third quartiles of temperatures in June and December are 77 °F and 74 °F, respectively.

<p img align="center" width="100%">
<img width="381" alt="box_plot_June_Dec_temps" src="https://user-images.githubusercontent.com/85843401/130854705-d6acc3ee-4fd6-4560-9b15-302cf573438a.png">
<img width="132" alt="temps_June" src="https://user-images.githubusercontent.com/85843401/130854626-f8eeff48-e44a-4ad8-9f24-dea9d09e3500.png">
<img width="134" alt="temps_Dec" src="https://user-images.githubusercontent.com/85843401/130854645-f987a482-a82f-432a-b7ce-fc2e762a50ae.png"><figcaption>Figure 1: Comparison of June and December temperature, left: box plot, rigth: statistic summary.</figcaption></figure>
</p>




 
