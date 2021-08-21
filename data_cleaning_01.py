import pandas as pd
import numpy as np

def main():
    # Display rows, columns and width in full
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    df = pd.read_csv('nba_2015_2021.csv')
    df = df.rename(columns={'PTS.1': 'PTS_1'})
    df = df.rename(columns={'Attend.': 'Attendee'})

    df = df[df.Date != 'Playoffs'] # row with "Playoffs" is used to section the data.

    df[['day', 'date', 'year']] = df['Date'].str.split(',', expand=True)
    df['date'] = df['date'].str.strip() #Strip Leading and Trailing Space of the column
    df[['month', 'day_n']] = df.date.str.split(" ", expand=True, )
    df['day_n'] = np.where(df.day_n.apply(len) ==1, str(0)+df.day_n, df.day_n)
    df['year'] = df.year.str[1:]
    df['Attendee'] = np.where(df.Attendee.isnull(), 0, df.Attendee)

    month_dic = {"Jan": "01",
                 "Feb": '02',
                 'Mar': '03',
                 'Apr': '04',
                 'May': '05',
                 'Jun': '06',
                 'Jul': '07',
                 'Aug': '08',
                 'Sep': '09',
                 'Oct': '10',
                 'Nov': '11',
                 'Dec': '12'
                 }
    df['month'] = df['month'].map(month_dic)

    df['Date_New'] = [try_concat(x, y, z) for x, y, z in zip(df['year'], df['month'], df['day_n'])]

    df.drop(['Unnamed: 0', "Date", "day","date", "year","month","day_n", 'Unnamed: 6'], axis=1, inplace=True)
    df = df.astype({"Attendee": float})
    df = df.astype({"Attendee": int}) # int('5.0')->error, int(float('5.0'))=5

    df.to_csv("nba_2015_2021_v1.csv")

def try_concat(x, y, z):
    try:
        return x + '-' + y + '-' + z
    except(ValueError, TypeError):
        return np.nan

if __name__ == '__main__':
    main()