from project.player import Player, player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return f"Player {player_name} is not in the guild."
        else:
            self.players.remove(player_name)
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been kicked from the guild."

    def guild_info(self):
        recult = [f'Guild: {self.name}']
        for p in self.players:
            recult.append(p.player_info())
        return '\n'.join(recult)


guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
