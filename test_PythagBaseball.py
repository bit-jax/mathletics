import PythagBaseball as pb


# verifies pull from csv
# def test_GetFromCSV():
#     teamlist = pb.teams()
#     assert teamlist[0] == 'Arizona Diamondbacks'

def test_GetRuns():
    teamlist=pb.teams_runs()
    assert teamlist[0] == 'Arizona Diamondbacks,449'

def test_GetWinLossRunsallowed():
    teamlist = pb.teams_win_loss_allowed()
    assert teamlist[0] == '617,34,74'

def test_CombineRunsRunsAllowedWinLoss():
    teamlist = pb.teams_RRaWL()
    assert teamlist[0] == 'Arizona Diamondbacks,449,617,34,74'

def test_SavetoCSV():
    file = open('MLB_2021_pythag_data.txt', 'r')
    team_list = file.read().split('\n')
    assert team_list[0] == 'Tm,R,RA,W,L'

