from dlgo.gotypes import Player
import random

class MCTSNode(object):
  def __init__(self, game_state, parent=None, move=None):
    self.game_state = game_state
    self.parent = parent
    self.move = move
    self.win_counts = {
        Player.black: 0,
        Player.white: 0,
    }
    self.num_rollouts = 0
    self.children = []
    self.unvisited_moves = game_state.legal_moves()


  def add_random_child(self):
    index = random.randint(0, len(self.unvisited_moves) - 1)
    new_move = self.unvisited_moves.pop(index)
    new_game_state = self.game_state.apply_move(new_move)
    new_node = MCTSNode(new_game_state, self, new_move)
    self.children.append(new_node)
    return new_node

  def record_win(self, winner):
    self.win_counts[winner] += 1
    self.num_rollouts += 1
