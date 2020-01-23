#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 23, 2020, at 16:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'IGT_V1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Documents\\Coding Projects\\PsychoPy_Tasks\\Iowa_Gambling_Task\\IGT_V1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
IGTInstrMsg = visual.TextStim(win=win, name='IGTInstrMsg',
    text='In this task, you play a "gambling" game.\nYou need to choose one of the four buttons (A,B,C,D) with the mouse.\n\nEach time you can win some money, but you may sometimes  also have to pay a fee to the bank.\nAfter each trial, you need to collect your money, which will adjust your pot of money.\n\nYou start with a loan of £2000\n\nThere are 100 trials (taking 5 minutes or so).\n\nGo until it stops and see how much you can make in addition to the load of £2000.\n\nPRESS Y TO START...',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
IGTInsrKeys = keyboard.Keyboard()

# Initialize components for Routine "IGT_trial"
IGT_trialClock = core.Clock()
# Setting initial balance

IGTTotalMoney = 2000
ThisTrialMoney = IGTTotalMoney

IGTThisTrialReward = 0
IGTThisTrialPenalty = 0

# Setting rewards and punishments

AReward = 100
APenalty = 250

BReward = 100
BPenalty = 250

CReward = 50
CPenalty = 50

DReward = 50
DPenalty = 50
IGTMoneyMsg = visual.TextStim(win=win, name='IGTMoneyMsg',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
buttonA = visual.ImageStim(
    win=win,
    name='buttonA', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
buttonB = visual.ImageStim(
    win=win,
    name='buttonB', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
buttonC = visual.ImageStim(
    win=win,
    name='buttonC', 
    image='sin', mask=None,
    ori=0, pos=(0.1, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
buttonD = visual.ImageStim(
    win=win,
    name='buttonD', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
IGTmouse = event.Mouse(win=win)
x, y = [None, None]
IGTmouse.mouseClock = core.Clock()

# Initialize components for Routine "IGT_feedback"
IGT_feedbackClock = core.Clock()
IGTRewardMsg = visual.TextStim(win=win, name='IGTRewardMsg',
    text='default text',
    font='Arial',
    pos=(0, 0.03), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
IGTPenaltyMsg = visual.TextStim(win=win, name='IGTPenaltyMsg',
    text='default text',
    font='Arial',
    pos=(0, -0.03), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
IGTInsrKeys.keys = []
IGTInsrKeys.rt = []
# keep track of which components have finished
InstructionsComponents = [IGTInstrMsg, IGTInsrKeys]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IGTInstrMsg* updates
    if IGTInstrMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IGTInstrMsg.frameNStart = frameN  # exact frame index
        IGTInstrMsg.tStart = t  # local t and not account for scr refresh
        IGTInstrMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IGTInstrMsg, 'tStartRefresh')  # time at next scr refresh
        IGTInstrMsg.setAutoDraw(True)
    
    # *IGTInsrKeys* updates
    waitOnFlip = False
    if IGTInsrKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IGTInsrKeys.frameNStart = frameN  # exact frame index
        IGTInsrKeys.tStart = t  # local t and not account for scr refresh
        IGTInsrKeys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IGTInsrKeys, 'tStartRefresh')  # time at next scr refresh
        IGTInsrKeys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(IGTInsrKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IGTInsrKeys.status == STARTED and not waitOnFlip:
        theseKeys = IGTInsrKeys.getKeys(keyList=['y'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IGTInstrMsg.started', IGTInstrMsg.tStartRefresh)
thisExp.addData('IGTInstrMsg.stopped', IGTInstrMsg.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
IGT_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IGT_Conditions1.xlsx'),
    seed=None, name='IGT_trials')
thisExp.addLoop(IGT_trials)  # add the loop to the experiment
thisIGT_trial = IGT_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIGT_trial.rgb)
if thisIGT_trial != None:
    for paramName in thisIGT_trial:
        exec('{} = thisIGT_trial[paramName]'.format(paramName))

for thisIGT_trial in IGT_trials:
    currentLoop = IGT_trials
    # abbreviate parameter names if possible (e.g. rgb = thisIGT_trial.rgb)
    if thisIGT_trial != None:
        for paramName in thisIGT_trial:
            exec('{} = thisIGT_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "IGT_trial"-------
    # update component parameters for each repeat
    # setup some python lists for storing info about the IGTmouse
    IGTmouse.x = []
    IGTmouse.y = []
    IGTmouse.leftButton = []
    IGTmouse.midButton = []
    IGTmouse.rightButton = []
    IGTmouse.time = []
    IGTmouse.clicked_name = []
    gotValidClick = False  # until a click is received
    IGTmouse.mouseClock.reset()
    # keep track of which components have finished
    IGT_trialComponents = [IGTMoneyMsg, buttonA, buttonB, buttonC, buttonD, IGTmouse]
    for thisComponent in IGT_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IGT_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "IGT_trial"-------
    while continueRoutine:
        # get current time
        t = IGT_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IGT_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IGTMoneyMsg* updates
        if IGTMoneyMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IGTMoneyMsg.frameNStart = frameN  # exact frame index
            IGTMoneyMsg.tStart = t  # local t and not account for scr refresh
            IGTMoneyMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IGTMoneyMsg, 'tStartRefresh')  # time at next scr refresh
            IGTMoneyMsg.setAutoDraw(True)
        if IGTMoneyMsg.status == STARTED:  # only update if drawing
            IGTMoneyMsg.setText(u"Your Balance:\n£%.2f" %IGTTotalMoney, log=False)
        
        # *buttonA* updates
        if buttonA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonA.frameNStart = frameN  # exact frame index
            buttonA.tStart = t  # local t and not account for scr refresh
            buttonA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonA, 'tStartRefresh')  # time at next scr refresh
            buttonA.setAutoDraw(True)
        if buttonA.status == STARTED:  # only update if drawing
            buttonA.setImage('buttonA.png', log=False)
        
        # *buttonB* updates
        if buttonB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonB.frameNStart = frameN  # exact frame index
            buttonB.tStart = t  # local t and not account for scr refresh
            buttonB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonB, 'tStartRefresh')  # time at next scr refresh
            buttonB.setAutoDraw(True)
        if buttonB.status == STARTED:  # only update if drawing
            buttonB.setImage('buttonB.png', log=False)
        
        # *buttonC* updates
        if buttonC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonC.frameNStart = frameN  # exact frame index
            buttonC.tStart = t  # local t and not account for scr refresh
            buttonC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonC, 'tStartRefresh')  # time at next scr refresh
            buttonC.setAutoDraw(True)
        if buttonC.status == STARTED:  # only update if drawing
            buttonC.setImage('buttonC.png', log=False)
        
        # *buttonD* updates
        if buttonD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonD.frameNStart = frameN  # exact frame index
            buttonD.tStart = t  # local t and not account for scr refresh
            buttonD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonD, 'tStartRefresh')  # time at next scr refresh
            buttonD.setAutoDraw(True)
        if buttonD.status == STARTED:  # only update if drawing
            buttonD.setImage('buttonD.png', log=False)
        # *IGTmouse* updates
        if IGTmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IGTmouse.frameNStart = frameN  # exact frame index
            IGTmouse.tStart = t  # local t and not account for scr refresh
            IGTmouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IGTmouse, 'tStartRefresh')  # time at next scr refresh
            IGTmouse.status = STARTED
            prevButtonState = IGTmouse.getPressed()  # if button is down already this ISN'T a new click
        if IGTmouse.status == STARTED:  # only update if started and not finished!
            buttons = IGTmouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [buttonA, buttonB, buttonC, buttonD]:
                        if obj.contains(IGTmouse):
                            gotValidClick = True
                            IGTmouse.clicked_name.append(obj.name)
                    x, y = IGTmouse.getPos()
                    IGTmouse.x.append(x)
                    IGTmouse.y.append(y)
                    buttons = IGTmouse.getPressed()
                    IGTmouse.leftButton.append(buttons[0])
                    IGTmouse.midButton.append(buttons[1])
                    IGTmouse.rightButton.append(buttons[2])
                    IGTmouse.time.append(IGTmouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IGT_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "IGT_trial"-------
    for thisComponent in IGT_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # A button
    if IGTmouse.isPressedIn(buttonA) and FEE == 1:
        IGTThisTrialReward = AReward
        IGTThisTrialPenalty = APenalty
        ThisTrialMoney = (IGTTotalMoney + IGTThisTrialReward) - IGTThisTrialPenalty
        IGTTotalMoney = ThisTrialMoney
    
    elif IGTmouse.isPressedIn(buttonA) and FEE == 0:
        IGTThisTrialReward = AReward
        IGTThisTrialPenalty = 0
        ThisTrialMoney = IGTTotalMoney + IGTThisTrialReward
        IGTTotalMoney = ThisTrialMoney
    
    # B button
    if IGTmouse.isPressedIn(buttonB) and FEE == 1:
        IGTThisTrialReward = BReward
        IGTThisTrialPenalty = BPenalty
        ThisTrialMoney = (IGTTotalMoney + IGTThisTrialReward) - IGTThisTrialPenalty
        IGTTotalMoney = ThisTrialMoney
    
    elif IGTmouse.isPressedIn(buttonB) and FEE == 0:
        IGTThisTrialReward = BReward
        IGTThisTrialPenalty = 0
        ThisTrialMoney = IGTTotalMoney + IGTThisTrialReward
        IGTTotalMoney = ThisTrialMoney
    
    # C button
    if IGTmouse.isPressedIn(buttonC) and FEE == 1:
        IGTThisTrialReward = CReward
        IGTThisTrialPenalty = CPenalty
        ThisTrialMoney = (IGTTotalMoney + IGTThisTrialReward) - IGTThisTrialPenalty
        IGTTotalMoney = ThisTrialMoney
    
    elif IGTmouse.isPressedIn(buttonC) and FEE == 0:
        IGTThisTrialReward = CReward
        IGTThisTrialPenalty = 0
        ThisTrialMoney = IGTTotalMoney + IGTThisTrialReward
        IGTTotalMoney = ThisTrialMoney
    
    
    # D button
    if IGTmouse.isPressedIn(buttonD) and FEE == 1:
        IGTThisTrialReward = DReward
        IGTThisTrialPenalty = DPenalty
        ThisTrialMoney = (IGTTotalMoney + IGTThisTrialReward) - IGTThisTrialPenalty
        IGTTotalMoney = ThisTrialMoney
    
    elif IGTmouse.isPressedIn(buttonD) and FEE == 0:
        IGTThisTrialReward = DReward
        IGTThisTrialPenalty = 0
        ThisTrialMoney = IGTTotalMoney + IGTThisTrialReward
        IGTTotalMoney = ThisTrialMoney
    
    # Save data
    thisExp.addData('IGTThisTrialReward', IGTThisTrialReward)
    thisExp.addData('IGTThisTrialPenalty', IGTThisTrialPenalty)
    thisExp.addData('IGTTotalMoney', IGTTotalMoney)
    
    
    
    IGT_trials.addData('IGTMoneyMsg.started', IGTMoneyMsg.tStartRefresh)
    IGT_trials.addData('IGTMoneyMsg.stopped', IGTMoneyMsg.tStopRefresh)
    IGT_trials.addData('buttonA.started', buttonA.tStartRefresh)
    IGT_trials.addData('buttonA.stopped', buttonA.tStopRefresh)
    IGT_trials.addData('buttonB.started', buttonB.tStartRefresh)
    IGT_trials.addData('buttonB.stopped', buttonB.tStopRefresh)
    IGT_trials.addData('buttonC.started', buttonC.tStartRefresh)
    IGT_trials.addData('buttonC.stopped', buttonC.tStopRefresh)
    IGT_trials.addData('buttonD.started', buttonD.tStartRefresh)
    IGT_trials.addData('buttonD.stopped', buttonD.tStopRefresh)
    # store data for IGT_trials (TrialHandler)
    if len(IGTmouse.x): IGT_trials.addData('IGTmouse.x', IGTmouse.x[0])
    if len(IGTmouse.y): IGT_trials.addData('IGTmouse.y', IGTmouse.y[0])
    if len(IGTmouse.leftButton): IGT_trials.addData('IGTmouse.leftButton', IGTmouse.leftButton[0])
    if len(IGTmouse.midButton): IGT_trials.addData('IGTmouse.midButton', IGTmouse.midButton[0])
    if len(IGTmouse.rightButton): IGT_trials.addData('IGTmouse.rightButton', IGTmouse.rightButton[0])
    if len(IGTmouse.time): IGT_trials.addData('IGTmouse.time', IGTmouse.time[0])
    if len(IGTmouse.clicked_name): IGT_trials.addData('IGTmouse.clicked_name', IGTmouse.clicked_name[0])
    IGT_trials.addData('IGTmouse.started', IGTmouse.tStart)
    IGT_trials.addData('IGTmouse.stopped', IGTmouse.tStop)
    # the Routine "IGT_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "IGT_feedback"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # Reward
    IGTFeedback1 = u"You won £%.2f" %IGTThisTrialReward
    
    # Penalty
    IGTFeedback2 = u"You lost £%.2f" %IGTThisTrialPenalty
    IGTRewardMsg.setText(IGTFeedback1)
    IGTPenaltyMsg.setText(IGTFeedback2)
    # keep track of which components have finished
    IGT_feedbackComponents = [IGTRewardMsg, IGTPenaltyMsg]
    for thisComponent in IGT_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IGT_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "IGT_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IGT_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IGT_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IGTRewardMsg* updates
        if IGTRewardMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IGTRewardMsg.frameNStart = frameN  # exact frame index
            IGTRewardMsg.tStart = t  # local t and not account for scr refresh
            IGTRewardMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IGTRewardMsg, 'tStartRefresh')  # time at next scr refresh
            IGTRewardMsg.setAutoDraw(True)
        if IGTRewardMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IGTRewardMsg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                IGTRewardMsg.tStop = t  # not accounting for scr refresh
                IGTRewardMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IGTRewardMsg, 'tStopRefresh')  # time at next scr refresh
                IGTRewardMsg.setAutoDraw(False)
        
        # *IGTPenaltyMsg* updates
        if IGTPenaltyMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IGTPenaltyMsg.frameNStart = frameN  # exact frame index
            IGTPenaltyMsg.tStart = t  # local t and not account for scr refresh
            IGTPenaltyMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IGTPenaltyMsg, 'tStartRefresh')  # time at next scr refresh
            IGTPenaltyMsg.setAutoDraw(True)
        if IGTPenaltyMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IGTPenaltyMsg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                IGTPenaltyMsg.tStop = t  # not accounting for scr refresh
                IGTPenaltyMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IGTPenaltyMsg, 'tStopRefresh')  # time at next scr refresh
                IGTPenaltyMsg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IGT_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "IGT_feedback"-------
    for thisComponent in IGT_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    IGT_trials.addData('IGTRewardMsg.started', IGTRewardMsg.tStartRefresh)
    IGT_trials.addData('IGTRewardMsg.stopped', IGTRewardMsg.tStopRefresh)
    IGT_trials.addData('IGTPenaltyMsg.started', IGTPenaltyMsg.tStartRefresh)
    IGT_trials.addData('IGTPenaltyMsg.stopped', IGTPenaltyMsg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IGT_trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
