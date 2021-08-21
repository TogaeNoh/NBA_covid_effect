# Does empty stadium affect players?
## Introduction
After Covid hit during 2020 season, no or limited spectators are permitted to see NBA team play sitting in arenas. 
I wondered if an empty home arena can be the reason for mediocre performance at home.
## Data Handling Procedure
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
  * Replace null value to zero in the attendence column.
  * Drop unnecessary columns
  * Export cleaned datafrom in the CSV file format again. \Utilize this file for next step.
4. Data modification
  * New column is added: How much percent capacity were occupied for arena.<br>This columns helps to analyze how limited fans influence home match result. 
  * Create three dat

 For arena suites that are occupied at 25 percent capacity or less
6. Plotting Data.
  * 
![image](https://user-images.githubusercontent.com/84579416/130312754-3536c29f-4a37-4616-8c04-487082959939.png)



![image](https://user-images.githubusercontent.com/84579416/130248581-3400a94e-8306-4757-a058-df62dc2089a4.png)

## Conclusion
