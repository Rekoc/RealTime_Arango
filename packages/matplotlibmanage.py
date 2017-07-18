# python 3.5.X
# Made for matplotlib 2.0.2

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter
import matplotlib.pyplot as plt
import numpy as np

'''class MatplotlibManage:

    def __init__(self):
        pass

    def init(self):
        self.t = np.arange(0.0, 4.0, 0.01)
        self.s = 1 + np.sin(2 * np.pi * self.t)
        self.plt.plot(self.t, self.s, color='green')

        self.plt.xlabel('time (s)')
        self.plt.ylabel('voltage (mV)')
        self.plt.title('About as simple as it gets, folks')
        self.plt.grid(True)
        self.plt.savefig("test.png")

        self.plt.show()

        self.modify()

    def modify(self):
        self.s = 1 + np.sin(2 * np.pi * self.t)
        self.plt.plot(self.t, self.s, color='green')
        '''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.animation import FuncAnimation


class UpdateDist(object):
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 15)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')

    def init(self):
        self.success = 0
        self.line.set_data([], [])
        return self.line,

    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            return self.init()

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand(1,) < self.prob:
            self.success += 1
        y = ss.beta.pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,

fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=np.arange(100), init_func=ud.init,
                     interval=100, blit=True)
plt.show()