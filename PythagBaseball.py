import pandas as pd

b_data = pd.read_csv(r'./MLB_2021_batting.txt')
p_data = pd.read_csv(r'./MLB_2021_pitching.txt')

b_df = pd.DataFrame(b_data)
p_df = pd.DataFrame(p_data)

def teams_runs():
    team_list = []
    for row in b_df.itertuples():
        team = row.Tm
        runs = row.R
        line = str(team) + ',' + str(runs)
        team_list.append(line)
    return team_list

def teams_win_loss_allowed():
    team_list = []
    for row in p_df.itertuples():
        win = row.W
        loss = row.L
        runs = row.R
        line = str(runs) + ',' + str(win) + ',' + str(loss)
        team_list.append(line)
    return team_list

def teams_RRaWL():
    team_list = []
    runs = teams_runs()
    wla = teams_win_loss_allowed()
    for i in range(len(runs)):
        line = runs[i] + ',' + wla[i]
        team_list.append(line)
    return team_list

def teams_to_CSV():
    team_list = 'Tm,R,RA,W,L'
    for row in teams_RRaWL():
        team_list += '\n' + row
    file = open('MLB_2021_pythag_data.txt', 'w')
    file.write(team_list)

teams_to_CSV()
    
