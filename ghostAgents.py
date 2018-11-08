# ghostAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util

class GhostAgent( Agent ):
  STOP_KEY = 'q'
  
  def __init__( self, index ):
    self.index = index
    self.keys = []
    self.lastMove = Directions.STOP

  '''def getAction( self, state ):
    dist = self.getDistribution(state)
    if len(dist) == 0: 
      return Directions.STOP
    else:
      return util.chooseFromDistribution( dist )'''

  def getAction( self, state):
    from graphicsUtils import keys_waiting
    from graphicsUtils import keys_pressed
    
    print(self.keys)
    legal = state.getLegalActions(self.index)
    move = self.getMove(legal)
    
    if move == Directions.STOP:
      # Try to move in the same direction as before
      if self.lastMove in legal:
        move = self.lastMove
    
    if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP

    if move not in legal:
      move = random.choice(legal)
      
    self.lastMove = move
    return move
    
  def getDistribution(self, state):
    "Returns a Counter encoding a distribution over actions from the provided state."
    util.raiseNotDefined()

  def getMove(self, legal):
      move = Directions.STOP
      if('LEFT' in self.keys) and Directions.WEST in legal:  move = Directions.WEST
      if('RIGHT' in self.keys) and Directions.EAST in legal: move = Directions.EAST
      if('UP' in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
      if('DOWN' in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
      return move
  
class RandomGhost( GhostAgent ):
  "A ghost that chooses a legal action uniformly at random."
  def getDistribution( self, state ):
    #dist = util.Counter()
    #for a in state.getLegalActions( self.index ): dist[a] = 1.0
    #dist.normalize()
    return 0 #dist

class DirectionalGhost( GhostAgent ):
  "A ghost that prefers to rush Pacman, or flee when scared."
  def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
    self.index = index
    self.prob_attack = prob_attack
    self.prob_scaredFlee = prob_scaredFlee
      
  def getDistribution( self, state ):
    return 0