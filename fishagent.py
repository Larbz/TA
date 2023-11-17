import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor
from pade.behaviours.protocols import TimedBehaviour
import time 
class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        # self.agent = agent
        # print("init")/
        # self.on_time()

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        # display_message(self.agent.aid.localname, 'Updating the fishies!')
        # for fish in self.agent.fish_list:
        #     fish.updateStatus()
        #     fish.swim()
        print("asd")
        # self.agent.updateStatus()
        # self.agent.swim()
        # time.sleep(0.2)
        # for fish in self.agent.fish_list:
        #     fish.on_time()

        # gui.update()


class FishAgent(Agent):
    def __init__(self,aid):
        super(FishAgent, self).__init__(aid=aid, debug=False)
        self.x = random.randint(1, 100)
        self.y = random.randint(1, 500)
        self.color = QColor(random.randint(0, 0xffffff))
        self.size = random.randint(5, 30)
        self.speed = 10 * 25 / self.size
        self.status = -1
        self.spriteId = random.randint(0,5)
        mytimed = MyTimedBehaviour(self, .2)
        # yourtimed = YourTimedBehaviour(self, 2)
        self.behaviours.append(mytimed)
        # self.behaviours.append(yourtimed)
    #     self.loop()

    # def loop(self):
    #     self.updateStatus()
    #     self.swim()
    #     time.sleep(0.2)

    def updateStatus(self):
        if self.y < 500:
            self.status = 1
            if self.x > 100 + Global.x_center:
                self.status = 4;

        elif self.y > 900:
            self.status = 2;
            if self.x < 30 + Global.x_center:
                self.status = 3

        else:
            if self.x < 30 + Global.x_center:
                self.status = 3
            else:
                self.status = 4

    def swim(self):
        if self.status == 1: self.x += self.speed
        elif self.status == 2: self.x -= self.speed
        elif self.status == 3: self.y -= self.speed
        elif self.status == 4: self.y += self.speed


