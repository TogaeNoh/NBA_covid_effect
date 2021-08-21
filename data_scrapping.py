import pandas as pd

def main():
    # Display rows, columns and width in full
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    df20oct_19 = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-october-2019.html')[0]
    df20nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-november.html')[0]
    df20dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-december.html')[0]
    df20jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-january.html')[0]
    df20feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-february.html')[0]
    df20mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-march.html')[0]
    df20jul = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-july.html')[0]
    df20aug = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-august.html')[0]
    df20sep = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-september.html')[0]
    df20oct_20 = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-october-2020.html')[0]

    df20 = pd.concat([df20oct_19, df20nov, df20dec, df20jan, df20feb, df20mar, df20jul, df20aug, df20sep, df20oct_20],
                     ignore_index = True)
    df20['Season'] = "2020"

    df21_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-december.html')[0]
    df21_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-january.html')[0]
    df21_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-february.html')[0]
    df21_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-march.html')[0]
    df21_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-april.html')[0]
    df21_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-may.html')[0]
    df21_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-june.html')[0]
    df21_jul = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_games-july.html')[0]

    df21 = pd.concat([df21_dec, df21_jan, df21_feb, df21_mar, df21_apr, df21_may, df21_jun, df21_jul],
                     ignore_index = True)
    df21['Season'] = "2021"

    df19_oct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-october.html')[0]
    df19_nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-november.html')[0]
    df19_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-december.html')[0]
    df19_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-january.html')[0]
    df19_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-february.html')[0]
    df19_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-march.html')[0]
    df19_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-april.html')[0]
    df19_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-may.html')[0]
    df19_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_games-june.html')[0]

    df19 = pd.concat([df19_oct, df19_nov, df19_dec, df19_jan, df19_feb, df19_mar, df19_apr, df19_may, df19_jun],
                     ignore_index = True)
    df19['Season'] = "2019"

    df18_oct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-october.html')[0]
    df18_nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-november.html')[0]
    df18_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-december.html')[0]
    df18_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-january.html')[0]
    df18_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-february.html')[0]
    df18_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-march.html')[0]
    df18_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-april.html')[0]
    df18_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-may.html')[0]
    df18_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2018_games-june.html')[0]

    df18 = pd.concat([df18_oct, df18_nov, df18_dec, df18_jan, df18_feb, df18_mar, df18_apr, df18_may, df18_jun],
                     ignore_index = True)
    df18['Season'] = "2018"

    df17_oct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-october.html')[0]
    df17_nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-november.html')[0]
    df17_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-december.html')[0]
    df17_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-january.html')[0]
    df17_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-february.html')[0]
    df17_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-march.html')[0]
    df17_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-april.html')[0]
    df17_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-may.html')[0]
    df17_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2017_games-june.html')[0]

    df17 = pd.concat([df17_oct, df17_nov, df17_dec, df17_jan, df17_feb, df17_mar, df17_apr, df17_may, df17_jun],
                     ignore_index = True)
    df17['Season'] = "2017"

    df16_oct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-october.html')[0]
    df16_nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-november.html')[0]
    df16_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-december.html')[0]
    df16_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-january.html')[0]
    df16_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-february.html')[0]
    df16_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-march.html')[0]
    df16_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-april.html')[0]
    df16_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-may.html')[0]
    df16_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2016_games-june.html')[0]

    df16 = pd.concat([df16_oct, df16_nov, df16_dec, df16_jan, df16_feb, df16_mar, df16_apr, df16_may, df16_jun],
                     ignore_index = True)
    df16['Season'] = "2016"

    df15_oct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-october.html')[0]
    df15_nov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-november.html')[0]
    df15_dec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-december.html')[0]
    df15_jan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-january.html')[0]
    df15_feb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-february.html')[0]
    df15_mar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-march.html')[0]
    df15_apr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-april.html')[0]
    df15_may = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-may.html')[0]
    df15_jun = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_games-june.html')[0]

    df15 = pd.concat([df15_oct, df15_nov, df15_dec, df15_jan, df15_feb, df15_mar, df15_apr, df15_may, df15_jun],
                     ignore_index = True)
    df15['Season'] = "2015"

    df15_21 = pd.concat([df15, df16, df17, df18, df19, df20, df21],
                     ignore_index = True)
    df15_21.to_csv("nba_2015_2021.csv")

    

if __name__ == '__main__':
    main()