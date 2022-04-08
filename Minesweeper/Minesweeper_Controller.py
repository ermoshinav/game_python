class MinesweeperController:
  def _init_(self, model):
     self.model=model
     
    def setView( self, view ):
        self.view = view
    
    def startnewgae(self);
     gamesettings=self.view.getgamesettings()
     try:
      self.model.startgae(*map(int, gamesettings))
       except:
            self.model.startGame( self.model.rowCount, self.model.columnCount, self.model.mineCount )
 
        self.view.createBoard()
     def onLeftClick( self, row, column ):
        self.model.openCell( row, column )
        self.view.syncWithModel()
        if self.model.isWin():
            self.view.showWinMessage()
            self.startNewGame()
        elif self.model.isGameOver():
            self.view.showGameOverMessage()
            self.startNewGame()
 
    def onRightClick( self, row, column ):
        self.model.nextCellMark( row, column )
        self.view.blockCell( row, column, self.model.getCell( row, column ).state == 'flagged' )
        self.view.syncWithModel()