model = MinesweeperModel()
controller = MinesweeperController( model );
view = MinesweeperView( model, controller )
view.pack()
view.mainloop()
