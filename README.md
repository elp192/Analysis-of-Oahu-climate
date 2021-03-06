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
- The median of temperatures in June and December are 75 °F and 71 °F, respectively.<br>
- The spread of temperatures in December (std=3.74) is more than in June (std=3.25).<br>
- The maximum temperatures in June and December are 84 °F and 83 °F, respectively.<br>
- The minimum temperatures in June and December are 64 °F and 56 °F, respectively.<br>
- The first quartile of temperatures in June and December are 73 °F and 69 °F, respectively.<br>
- The third quartile of temperatures in June and December are 77 °F and 74 °F, respectively.

<p img align="center" width="100%">
<img width="381" alt="box_plot_June_Dec_temps" src="https://user-images.githubusercontent.com/85843401/130854705-d6acc3ee-4fd6-4560-9b15-302cf573438a.png">
<img width="132" alt="temps_June" src="https://user-images.githubusercontent.com/85843401/130854626-f8eeff48-e44a-4ad8-9f24-dea9d09e3500.png">
<img width="134" alt="temps_Dec" src="https://user-images.githubusercontent.com/85843401/130854645-f987a482-a82f-432a-b7ce-fc2e762a50ae.png"><figcaption>Figure 1: Comparison of June and December temperature, left: box plot, rigth: statistic summaries.</figcaption></figure>
</p>

**Determine June and December precipitation levels** (Figure 2)<br>
- The number of available data for June (1574 data) is more than December (1405).
- The average of precipitation levels in June and December are 0.13 mm and 0.21 mm, respectively.
- The median of precipitation levels in June and December are 0.02 mm and 0.03 mm, respectively.
- The spread of precipitation levels in December (std=0.54 mm) is more than June (std=0.33 mm).<br>
- The maximum precipitation levels in June and December are 6.4 mm and 4.4 mm, respectively.<br>
- The minimum and first quartile of precipitation levels in June and December are 0.<br>
- The third quartile of precipitation levels in June and December are 0.12 mm and 0.15 mm, respectively.

<p img align="center" width="100%">
<img width="360" alt="box_plot_June_Dec_prcps" src="https://user-images.githubusercontent.com/85843401/130854793-1ec6d986-fa12-418f-be47-792a45396b06.png">
<img width="132" alt="prcps_June" src="https://user-images.githubusercontent.com/85843401/130849076-8a8e7ab3-e243-4c77-970d-52f815dbf2a5.png">
<img width="133" alt="prcps_Dec" src="https://user-images.githubusercontent.com/85843401/130849083-b9fd3a1f-f085-4f0c-9258-715b540f23f3.png"><figcaption>Figure 2: Comparison of June and December precipitation levels, left: box plot, rigth: statistic summaries.</figcaption></figure>
</p>

## Summary
The following conclusions are obtained from Figures 1 and 2.<br>
:white_medium_small_square: The average temperature in December (example of the cold month) is close to June (example of the warm month)(about 3.0 °F). So, it can be concluded that the weather in cold months is quite good.<br>
:white_medium_small_square: Results related to standard deviation confirms the above conclusion as the dispersions of temperature from mean for June and December are similar. So, there is no significant difference between changes in temperature range in cold and warm months.<br>
:white_medium_small_square: The difference between minimum temperature in June and December is 8 °F; however, this difference for 25% and 75% data points are 4 °F and 3 °F, respectively. This shows that in warm and cold months of the year for most of the data points, the difference of temperature is less than 4 °F.<br>
:white_medium_small_square: The outliers are observed in boxplots related to the precipitation levels, which impacts the average of data. Further analysis is required to better interpret the precipitation levels of these months.

 
