
### Score ###
# Score
class Score:
    def __init__(self):
        self.score = 0

    # Updating the score depending on the size of the sprite
    def punkteUpdate(self, groesse):
        if groesse <= (47, 27):
            self.score +=15
        elif groesse <= (93,54):
            self.score +=10
        elif groesse <= (186, 108):
            self.score += 5
    
    def getScore(self):
        return self.score

    # Set the score to zero
    def setScoreZero(self):
        self.score = 0