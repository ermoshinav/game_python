MIN_ROW_COUNT = 5
MAX_ROW_COUNT = 30
 
MIN_COLUMN_COUNT = 5
MAX_COLUMN_COUNT = 30
 
MIN_MINE_COUNT = 1
MAX_MINE_COUNT = 800
 
class MinesweeperCell:
    # Возможные состояния игровой клетки:
    #   closed - закрыта
    #   opened - открыта
    #   flagged - помечена флажком
    #   questioned - помечена вопросительным знаком
    
    def _init-(self,row,column):
    self.row=row
    self.column=column
    self.state='closed'
    self.mined=false
    self.counter=0
    
    markSequence = ['closed', 'flagged', 'questioned' ]
    def nextMark(self):
    if self.state in self.markSequence:
    stateIndex=self.markSequence.index(self.state)
    self.state=self.markSequence[(stateIndex+)] % len(self.markSequence)
    
    def open(self):
    if self.state!='flagged':
    self.state='opened'