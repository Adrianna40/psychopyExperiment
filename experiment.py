from psychopy import visual, core, event # import some libraries from PsychoPy
from pathlib import Path
import os
import random

images_dirs = []
for root, dirs, files in os.walk("./images", topdown=False):
   for name in files:
      if name.endswith('jpg') or name.endswith('jpeg'):
         images_dirs.append(os.path.join(root, name))

possible_times = [0.027, 0.04, 0.053, 0.067, 0.08, 0.107, 0.5]


# create a window
win = visual.Window([1440, 900], monitor="testMonitor", units="deg", fullscr=True)

# prepare a mask 
# credit: https://robson.plus/white-noise-image-generator/
path_to_mask = Path('mask.png')
mask_stim = visual.ImageStim(win, image=path_to_mask)

# fixation cross
fixation = visual.ShapeStim(win, 
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor="white"
)

# texts stimulti  
text_stim = visual.TextStim(win, text="Please, type your description and press space button")
task_stim = visual.TextStim(win, text="Please describe in detail what you see in the picture. Two sample responses are: 1. City scene. I see a big building on the right, and some people walking by shops. There are also trees. Most of the trees are on the left of the picture, against some background buildings. 2. Possibly outdoor. I really cannot tell much. Probably some animals, maybe mammals...")

task_stim.draw()
win.flip()
event.waitKeys()

for image_dir in images_dirs:
    time = random.choice(possible_times)
    path_to_image_file = Path(image_dir)

    # present fixation
    fixation.draw()
    win.flip()
    core.wait(0.25)

    # present image 
    image_stim = visual.ImageStim(win, image=path_to_image_file)
    image_stim.draw()
    win.flip()
    core.wait(time)

    # present mask 
    mask_stim.draw()
    win.flip()
    core.wait(0.5)


    # write an instruction 
    text_stim.draw()
    win.flip()
    
    event.waitKeys()

#cleanup
win.close()
core.quit()


