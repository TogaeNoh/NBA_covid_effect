# Does empty stadium affect NBA players?
## Introduction
After Covid hit during 2020 season, no or limited spectators are permitted to see NBA team play sitting in arenas. 
I wondered if there is the impact on home-court advantage due to the decreased fan attendance.
## Data Handling Process
1. Web scraping
  * From NBA reference website, data was collected for the period from the 15/16 season to the 20/21 season with function read_html in module pandas.
  * The webpage shows data per month for each season. [Source](https://www.basketball-reference.com/leagues/NBA_2020_games-october-2019.html)
  * Each table contains match result, date, attendance figures, and venue. 
2. Data merging
  * DataFrames are collected from more than sixty web pages. <br>Those are put together into single DataFrame.
  * Export the combined DataFrame in the CSV file format.<br> By reading this merged CSV file, pulling data from dozens of web page every single time is avoided.
3. Data cleaning
  * Rename columns which contain a period.
  * Convert date column from object data type to date-time data type.
  * Replace null value to zero in the attendance column.
  * Drop unnecessary columns
  * Export cleaned dataframes in the CSV file format again. \Utilize this file for next step.
4. Data modification
  * New column is added: How much percent of stadium capacity was occupied per match.<br>This column helps to analyze how limited fans influence home match result. 
  * Create three datasets from the 15/16 season to the 20/21 season. <br>The 19/20 and 20/21 seasons are splitted into two datasets respectively, depending on whether fans are allowed to watch in the stadium or not.
    1) Home-court win percentage
    2) The average Home-court points
    3) The average points difference between home and away matches
5. Plotting Data.
![image](https://user-images.githubusercontent.com/84579416/130327072-c1cdb7ef-4988-4b82-9556-07a63672723e.png)

## Conclusion
Home-court winning percentage dropped by more than five percent in 19/20 and 20/21 seasons with no fans around from Fig 1.<br>
Hypothesis was made that small number of home court fans affect low match points. Contrary to the hypothesis, average home points without fans were higher than those of other seasons before Covid-19. <br> 
Another data analysis was performed to see if absent arena impacts on the difference between home and away points. <br> 
As you see the figure 3., points gaps decreased when there are no spectators. 
As a result, an empty home arena can be the reason for teams' mediocre performance at home.
    
