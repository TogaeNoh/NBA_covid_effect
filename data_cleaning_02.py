import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Display rows, columns and width in full
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    df = pd.read_csv('nba_2015_2021_v1.csv')

    capa_dic ={
        'New Orleans Pelicans': 18626,
        'San Antonio Spurs': 19615,
        'Los Angeles Lakers':20000,
         'Charlotte Hornets':20200,
        'Indiana Pacers' :20000,
        'Toronto Raptors' :21050,
        'Miami Heat' :21000,
         'Boston Celtics' :19580,
        'New York Knicks': 20789,
        'Memphis Grizzlies' :18119,
        'Denver Nuggets':20106,
         'Utah Jazz' :19911,
        'Phoenix Suns':18422,
        'Sacramento Kings' :17853,
        'Portland Trail Blazers' :20241,
         'Orlando Magic' :20000,
        'Cleveland Cavaliers' :20562,
        'Minnesota Timberwolves':20412,
         'Dallas Mavericks' :21041,
        'Los Angeles Clippers' :20000,
        'Chicago Bulls':23500,
         'Milwaukee Bucks' :18717,
        'Philadelphia 76ers' :21171,
        'Washington Wizards':20476,
         'Atlanta Hawks' :21000,
        'Detroit Pistons' : 21584,
        'Houston Rockets' :18502,
         'Oklahoma City Thunder' : 18203,
        'Golden State Warriors' :19596,
        'Brooklyn Nets' :19000
    }
    df['Home_arena_Perc'] = df['Attendee'] / df['Home/Neutral'].map(capa_dic)

    #Figure 1
    pert_home = {
    "2015" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2015)) / np.sum((df['Season']==2015)),
    "2016" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2016)) / np.sum((df['Season'] == 2016)),
    "2017" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2017)) / np.sum((df['Season'] == 2017)),
    "2018" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2018)) / np.sum((df['Season'] == 2018)),
    "2019" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2019)) / np.sum((df['Season'] == 2019)),
    "2020\nFan" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2020) & (df.Date_New < '2020-04-01')) / np.sum((df['Season'] == 2020) & (df.Date_New < '2020-04-01')),
    "2021\nFan" : np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2021) & (df.Home_arena_Perc >= 0.8)) / np.sum((df['Season'] == 2021) & (df.Home_arena_Perc >= 0.8)),
    "2020\nNo Fan": np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2020) & (df.Date_New >= '2020-07-01')) / np.sum((df['Season'] == 2020) & (df.Date_New >= '2020-07-01')),
    "2021\nNo Fan": np.sum((df['PTS_1'] > df['PTS']) & (df['Season'] == 2021) & (df.Home_arena_Perc < 0.3)) / np.sum((df['Season'] == 2021) & (df.Home_arena_Perc < 0.3))
    }

    #Figure 2
    Home_point = {
        "2015" : df[df.Season == 2015]['PTS_1'].mean(),
        "2016" : df[df.Season == 2016]['PTS_1'].mean(),
        "2017" : df[df.Season == 2017]['PTS_1'].mean(),
        "2018" : df[df.Season == 2018]['PTS_1'].mean(),
        "2019" : df[df.Season == 2019]['PTS_1'].mean(),
        "2020\nFan" : df[(df.Season == 2020) & (df.Date_New < '2020-04-01')]['PTS_1'].mean(),
        "2021\nFan" : df[(df.Season == 2021) & (df.Home_arena_Perc >= 0.8)]['PTS_1'].mean(),
        "2020\nNo Fan": df[(df.Season == 2020) & (df.Date_New >= '2020-07-01')]['PTS_1'].mean(),
        "2021\nNo Fan" : df[(df.Season == 2021) & (df.Home_arena_Perc < 0.3)]['PTS_1'].mean()
    }

    #Figure 3
    diff_point = {
        "2015" : df[df.Season == 2015].eval('PTS_1 - PTS').mean(),
        "2016" : df[df.Season == 2016].eval('PTS_1 - PTS').mean(),
        "2017" : df[df.Season == 2017].eval('PTS_1 - PTS').mean(),
        "2018" : df[df.Season == 2018].eval('PTS_1 - PTS').mean(),
        "2019" : df[df.Season == 2019].eval('PTS_1 - PTS').mean(),
        "2020\nFan" : df[(df.Season == 2020) & (df.Date_New < '2020-04-01')].eval('PTS_1 - PTS').mean(),
        "2021\nFan" : df[(df.Season == 2021) & (df.Home_arena_Perc >= 0.8)].eval('PTS_1 - PTS').mean(),
        "2020\nNo Fan": df[(df.Season == 2020) & (df.Date_New >= '2020-07-01')].eval('PTS_1 - PTS').mean(),
        "2021\nNo Fan" : df[(df.Season == 2021) & (df.Home_arena_Perc < 0.3)].eval('PTS_1 - PTS').mean()
    }

    total_home_win_pert_Fan = len(df[(df.Season != 2020) & (df.Season != 2021) & (df['PTS_1'] > df['PTS'])].index)/len(df[(df.Season != 2020) & (df.Season != 2021)])
    avg_pts_diff = df[ df.Season.isin([2015,2016,2017,2018,2019]) | ((df.Season == 2020) & (df['Date_New'] < '2020-04-01'))|((df.Season == 2021) & (df['Home_arena_Perc'] > 0.8))].eval('PTS_1 - PTS').mean()

    year = list(pert_home.keys())
    percent = list(pert_home.values())
    year_a, year_b, year_c= list_split(year)
    percent_a, percent_b, percent_c = list_split(percent)

    year_1 = list(Home_point.keys())
    percent_1 = list(Home_point.values())
    year_1_a, year_1_b, year_1_c = list_split(year_1)
    percent_1_a, percent_1_b, percent_1_c  = list_split(percent_1)

    year_2 = list(diff_point.keys())
    percent_2 = list(diff_point.values())
    year_2_a, year_2_b, year_2_c = list_split(year_2)
    percent_2_a, percent_2_b, percent_2_c = list_split(percent_2)

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize = (12 ,12))
    fig.tight_layout(pad=4.0) #space between plots
    ax1.plot(year_a, percent_a, '-o')
    ax1.plot(year_b, percent_b, '-o')
    ax1.plot(year_c, percent_c, '-o')
    ax1.axvline('2019', ls="--")
    ax1.annotate("{:.2}".format(pert_home['2020\nNo Fan']) , (7, pert_home['2020\nNo Fan']+.005)) #labeling
    ax1.annotate("{:.2}".format(pert_home['2021\nNo Fan']) , (8, pert_home['2021\nNo Fan']+.005))
    ax1.title.set_text("Fig1. NBA home-court win percentage")
    ax1.text(.2, .05, "Average Winning Percentage \n"
                        "from 2015 to 2019 (No Covid): {:.2}".format(total_home_win_pert_Fan), transform=ax1.transAxes)

    ax1.set_ylim([0.51, .6])
    ax2.plot(year_1_a, percent_1_a, '-o')
    ax2.plot(year_1_b, percent_1_b, '-o')
    ax2.plot(year_1_c, percent_1_c, '-o')
    ax2.axvline('2019', ls="--")
    ax2.set_ylim([90, 120])
    #ax2.text(.2, .05, "Covid does not affect Home-court points.", transform = ax2.transAxes)
    ax2.title.set_text("Fig2. The average Home-court points")

    ax3.plot(year_2_a, percent_2_a, '-o')
    ax3.plot(year_2_b, percent_2_b, '-o')
    ax3.plot(year_2_c, percent_2_c, '-o')
    ax3.axvline('2021\nFan', ls="--")
    ax3.annotate("{:.2}".format(diff_point['2020\nNo Fan']) , (7, diff_point['2020\nNo Fan']+.2))
    ax3.annotate("{:.2}".format(diff_point['2021\nNo Fan']) , (8, diff_point['2021\nNo Fan']+.2))
    ax3.set_ylim([0, 5])
    ax3.title.set_text("Fig3. The average points difference between home and away matches")
    ax3.text(.2, .05, "Average points difference per year \n"
                          "from 2015 to 2021 (W/ Spectator): {:.2}".format(avg_pts_diff), transform=ax3.transAxes)

    plt.show()

def list_split(list):
    list_a = list[:-4]  #~2019
    list_b = list[-4:-2]    #2020-2021 Fan
    list_c = list[-2:]  #2020-2021 No Fan
    return list_a, list_b, list_c

if __name__ == '__main__':
    main()