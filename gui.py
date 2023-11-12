from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPaintEvent, QPainter, QPixmap
from PySide6.QtWidgets import QFrame


class Gui(QFrame):
    def __init__(self, agent) -> None:
        super(Gui, self).__init__()
        self.agent = agent
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.sprites=[
            QPixmap("images/Dory.png"),
            QPixmap("images/Marlin.png"),
            QPixmap("images/Nemo.png"),
            QPixmap("images/Sebastian.png"),
            QPixmap("images/StingRay.png"),
            QPixmap("images/Turtle.png")
        ]
 

    def paintEvent(self, _: QPaintEvent) -> None:
        painter = QPainter(self)
        for fish in self.agent.fish_list:
            own_sprite = self.sprites[fish.spriteId].scaled(fish.size,fish.size//2)
            #    print(fish.x, fish.y)
            # painter.fillRect(fish.x, fish.y, fish.size, fish.size//2, fish.color)
            painter.drawPixmap(fish.x,fish.y,own_sprite)
