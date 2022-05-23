class Team:
    def __init__(self, input_team_name, input_team_players, input_coach):
        self.name = input_team_name
        self.players = input_team_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        temp = 0
        for player in self.players:
            if player == player_name:
                temp = player
        return bool(temp)

    def play_game(self, game_won):
        if game_won == True:
            self.points += 3
