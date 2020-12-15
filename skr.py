import os
import tkinter as tk
from psychopy import visual, core, event, clock
import random



def get_config_data():
    conf = open('config.txt', 'rt', encoding='utf-8')
    configuration = []
    for line in conf:
        configuration.append(line.split(" ")[2])
    return configuration



config = get_config_data()

isi_time = float(config[0])
stim_duration = float(config[1])




#### GET SCREEN RESOLUTION
root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
#### STIMULUS PREPARATION
neutral_dir = 'utrecht/neutral'
smile_dir = 'utrecht/smile'

neutral_stims = os.listdir(neutral_dir)
smile_stims = os.listdir(smile_dir)

random.shuffle(neutral_stims)
random.shuffle(smile_stims)

neu_number = len(neutral_stims)
sm_number = len(smile_stims)


total_stims_number = neu_number + sm_number



txt_1 = u'В эксперименте вибрационная стимуляция будет чередоваться с картинками, на которых Вам будет необходимо сконцентрироваться и просчитывать элементы картинок про себя.'
txt_2 = u'Эксперимент завершен. Для выхода нажмите "пробел"'

win = visual.Window([w, h], color=(config[2]))
ISI = clock.StaticPeriod(win=win, screenHz=59, name='ISI')

####OPENING
txt = visual.TextStim(win, text= u'Сейчас будет эксперимент по исследованию тактильной стимуляции.', font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])

stims = []
for i in range (0, total_stims_number, 1):
    r = random.randint(0,1)
    if r == 0:
        try:
            stims.append("utrecht/neutral/"+neutral_stims.pop())
        except:
            stims.append("utrecht/smile/"+smile_stims.pop())
    else:
        try:
            stims.append("utrecht/smile/"+smile_stims.pop())
        except:
            stims.append("utrecht/neutral/"+neutral_stims.pop())

movs = [visual.ImageStim(win, image=i, mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, name=None, autoLog=None, maskParams=None) for i in stims]

txt = visual.TextStim(win, text=txt_1, font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])


for a in range (0, total_stims_number, 1):

    mov = movs.pop()
    mov.draw()
    win.flip()
    core.wait(stim_duration)

    win.flip()
    ISI.start(isi_time)
    ISI.complete()

txt = visual.TextStim(win, text=txt_1, font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])





win.close()
core.quit()
