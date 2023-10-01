import utils
import charts

def get_data_scores():
    
    team_local = input('Agrega el equipo local => ')
    team_away = input('Agrega el equipo visitante => ')

    # team_local = 'Monterrey'
    # team_away = 'Santos Laguna'

    more_one, more_two, both_goal = utils.filter_games_vs_last_teen(team_local, team_away)
    print(more_one, more_two, both_goal)

    labels = ['mas de 1', 'mas de 2', 'ambos anotan']
    values = [more_one, more_two, both_goal]

    charts.generate_bar_chart(labels, values)

    
if __name__ == '__main__':
    get_data_scores()
