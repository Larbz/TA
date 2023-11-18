import sys
import threading
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import start_loop, display_message
from fishagent import FishAgent
from pade.core.agent import Agent
import time
from globals import Global
from gui import Gui


class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent
        # start_loop(self.agent.fish_list)

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        self.agent.fish.updateStatus()
        self.agent.fish.swim()
        # display_message(self.agent.aid.localname, 'Updating the fishies!')
        # for fish in self.agent.fish_list:
        #     fish.updateStatus()
        #     fish.swim()

        # print("ASd")

        

        gui.update()

class YourTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(YourTimedBehaviour, self).__init__(agent, time)
        self.agent=agent


    def on_time(self):
        super(YourTimedBehaviour, self).on_time()
        Global.x_center += 3

class HostAgent(Agent):
    gui = None
    # num_fishes = 20
    fish=None
    fish_list = []
    
    enabled = False

    def __init__(self, aid):
        super(HostAgent, 
              self).__init__(aid=aid, debug=False)
        Global.x_center = 0
        self.fish = FishAgent(AID(name=aid.name))
        # for _ in range(self.num_fishes):
        #     # self.fish_list.append(FishAgent(AID(name=host_agent_name)))
        #     self.createFishAgent()
            # TODO name it and launch it as an agent of chaos
        mytimed = MyTimedBehaviour(self, .2)
        yourtimed = YourTimedBehaviour(self, 2)
        self.behaviours.append(mytimed)
        self.behaviours.append(yourtimed)
        # fsel.fish_list.append(self.fish)
        # hilo=threading.Thread(target=self.startFishLoop)
        # hilo.start()
        
        # hilo.join()



def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    # fish_list=list()
    agents = list()
    c=0
    for i in range(2000):
        port = int(sys.argv[1]) + c
        host_agent_name = 'host_agent_{}@localhost:{}'.format(port, port)
        host_agent = HostAgent(AID(name=host_agent_name))
        agents.append(host_agent)
        c += 1

    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(agents)
    gui.show()
    app.exec()
    x.join()

# CREAR PESCADOS EN EL MAIN Y LUEGO AGREGARLOS AL AGENT
# PUEDE SER QUE POR LA CANTIDAD DE PUERTOS EL PROGRAMA NO SE PUEDA USAR BIEN