from clue_game import *
from pysat.solvers import Glucose3


class ClueReasoner:

    def __init__(self, player_id, num_players):
        self.player_id = player_id
        self.num_players = num_players

    def initialize(self,
                   player_id: int,
                   num_players: int, ) -> None:
        self.player_id = player_id
        self.num_players = num_players

        sat_solver = Glucose3
        clause = []
        num_cards = len(Suspect) + len(Location) + len(Weapon)

        """set up initial clauses"""

        """Each card is in at least one place"""
        for i in range(0, num_cards):
            for j in range(0, num_players + 1):
                clause.append(i + j * num_cards + 1)
            sat_solver.add_clause(clause)
            clause.clear()

        """If a card is in one place, it cannot be in another place"""
        for i in range(0, num_cards):
            for j in range(0, num_players + 1):
                clause = []
                for k in range(j, num_players + 1):
                    clause.append(-1 * (i + j * num_cards + 1))
                    clause.append(-1 * (i + k * num_cards + 1))
                    sat_solver.add_clause(clause)
                    clause.clear()

        """At least one of each category is in the case file"""
        for i in Suspect:
            clause.append(i + (num_players + 1) * (num_cards + 1) + 1)
        sat_solver.add_clause(clause)
        clause.clear()

        for i in Location:
            clause.append(i + (num_players + 1) * (num_cards + 1) + 1)
        sat_solver.add_clause(clause)
        clause.clear()

        for i in Weapon:
            clause.append(i + (num_players + 1) * (num_cards + 1) + 1)
        sat_solver.add_clause(clause)
        clause.clear()

        """No two cards in each category are in the case file"""
        for i in Suspect:
            for j in range(i, len(Suspect)):
                clause.append(-1 * (i + (num_players + 1) * (num_cards + 1)))
                clause.append(-1 * (j + (num_players + 1) * (num_cards + 1)))
                sat_solver.add_clause(clause)
                clause.clear()

        for i in Location:
            for j in range(i, len(Location)):
                clause.append(-1 * (i + (num_players + 1) * (num_cards + 1)))
                clause.append(-1 * (j + (num_players + 1) * (num_cards + 1)))
                sat_solver.add_clause(clause)
                clause.clear()

        for i in Weapon:
            for j in range(i, len(Weapon)):
                clause.append(-1 * (i + (num_players + 1) * (num_cards + 1)))
                clause.append(-1 * (j + (num_players + 1) * (num_cards + 1)))
                sat_solver.add_clause(clause)
                clause.clear()

    def observe_suggestion(self,
                           suggestor_id: int,
                           suggestion: Suggestion,
                           blocker_id: Optional[int]) -> None:
        pass

    def observe_accusation(self,
                           accusor_id: int,
                           accusation: Accusation) -> None:
        pass
