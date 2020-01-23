#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on October 23, 2019, at 16:28
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
expName = 'SST_Task'  # from the Builder filename that created this script
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
    originPath='G:\\My Drive\\Projects\\5_Computer_Tasks\\PsychoPy\\Stop_Signal_Task\\SST_Task_V7_Final_lastrun.py',
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

# Initialize components for Routine "welcomScreen"
welcomScreenClock = core.Clock()
instr_resp = keyboard.Keyboard()
intr_text = visual.TextStim(win=win, name='intr_text',
    text='In this task, you need to respond to an arrow, which is surrounded \nby a white circle, pointing either left or right as fast as you can.\n\nIf the arrow points to the right,you should press the M key. \nIf the arrow points to the left, you should press the C key.\n\nHowever, if the arrow is surrounded by a RED CIRCLE, you\nshould NOT RESPOND.\n\nIn the first block of trials, you will be able to practice the task.\nIn the second block, the real experiment will begin.\nYou WILL be notified when the real experiment begins.\n\n\nPRESS ENTER TO START THE EXPERIMENT...',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Inital Stop Signal Start Time
ssigStartThis = 1.35
ssigStartLast = ssigStartThis

# Inital Stop Signal Duration
ssigDur = 0.65

fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stop = visual.ImageStim(
    win=win,
    name='stop', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
SST_resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
msg = " "
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "expStartScreen"
expStartScreenClock = core.Clock()
expStartScreenText = visual.TextStim(win=win, name='expStartScreenText',
    text='The practice trails are over.\nThe REAL trials will begin after this screen.\n\n\nPRESS ENTER TO CONTINUE...',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
expStartKey = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Inital Stop Signal Start Time
ssigStartThis = 1.35
ssigStartLast = ssigStartThis

# Inital Stop Signal Duration
ssigDur = 0.65

fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stop = visual.ImageStim(
    win=win,
    name='stop', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
SST_resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
msg = " "
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcomScreen"-------
# update component parameters for each repeat
instr_resp.keys = []
instr_resp.rt = []
# keep track of which components have finished
welcomScreenComponents = [instr_resp, intr_text]
for thisComponent in welcomScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "welcomScreen"-------
while continueRoutine:
    # get current time
    t = welcomScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_resp* updates
    waitOnFlip = False
    if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp.frameNStart = frameN  # exact frame index
        instr_resp.tStart = t  # local t and not account for scr refresh
        instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
        instr_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *intr_text* updates
    if intr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intr_text.frameNStart = frameN  # exact frame index
        intr_text.tStart = t  # local t and not account for scr refresh
        intr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intr_text, 'tStartRefresh')  # time at next scr refresh
        intr_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomScreen"-------
for thisComponent in welcomScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intr_text.started', intr_text.tStartRefresh)
thisExp.addData('intr_text.stopped', intr_text.tStopRefresh)
# the Routine "welcomScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_prac_V1.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    # Should a stop signal display?
    if ssig:
        ssigOpp = 1
    else:
        ssigOpp = 0
    arrow.setImage(arrows)
    stop.setOpacity(ssigOpp)
    stop.setImage(ssigImg)
    SST_resp.keys = []
    SST_resp.rt = []
    # keep track of which components have finished
    trialComponents = [fix, arrow, stop, SST_resp, ISI]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *stop* updates
        if stop.status == NOT_STARTED and tThisFlip >= ssigStartThis-frameTolerance:
            # keep track of start time/frame for later
            stop.frameNStart = frameN  # exact frame index
            stop.tStart = t  # local t and not account for scr refresh
            stop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop, 'tStartRefresh')  # time at next scr refresh
            stop.setAutoDraw(True)
        if stop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop.tStartRefresh + ssigDur-frameTolerance:
                # keep track of stop time/frame for later
                stop.tStop = t  # not accounting for scr refresh
                stop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop, 'tStopRefresh')  # time at next scr refresh
                stop.setAutoDraw(False)
        
        # *SST_resp* updates
        waitOnFlip = False
        if SST_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            SST_resp.frameNStart = frameN  # exact frame index
            SST_resp.tStart = t  # local t and not account for scr refresh
            SST_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SST_resp, 'tStartRefresh')  # time at next scr refresh
            SST_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(SST_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(SST_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if SST_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SST_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                SST_resp.tStop = t  # not accounting for scr refresh
                SST_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SST_resp, 'tStopRefresh')  # time at next scr refresh
                SST_resp.status = FINISHED
        if SST_resp.status == STARTED and not waitOnFlip:
            theseKeys = SST_resp.getKeys(keyList=['c', 'm'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                SST_resp.keys = theseKeys.name  # just the last key pressed
                SST_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (SST_resp.keys == str(corrAns)) or (SST_resp.keys == corrAns):
                    SST_resp.corr = 1
                else:
                    SST_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Control Stop Signal Difficulty
    if ssig and corrAns and ssigStartLast >= 1.05:
        ssigStartThis = ssigStartLast - 0.1
        ssigDur = 2 - ssigStartThis
    elif ssig and not corrAns and ssigStartLast <= 1.35:
        ssigStartThis = ssigStartLast + 0.1
        ssigDur = 2 - ssigStartThis
    prac_trials.addData('fix.started', fix.tStartRefresh)
    prac_trials.addData('fix.stopped', fix.tStopRefresh)
    prac_trials.addData('arrow.started', arrow.tStartRefresh)
    prac_trials.addData('arrow.stopped', arrow.tStopRefresh)
    prac_trials.addData('stop.started', stop.tStartRefresh)
    prac_trials.addData('stop.stopped', stop.tStopRefresh)
    # check responses
    if SST_resp.keys in ['', [], None]:  # No response was made
        SST_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           SST_resp.corr = 1;  # correct non-response
        else:
           SST_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac_trials (TrialHandler)
    prac_trials.addData('SST_resp.keys',SST_resp.keys)
    prac_trials.addData('SST_resp.corr', SST_resp.corr)
    if SST_resp.keys != None:  # we had a response
        prac_trials.addData('SST_resp.rt', SST_resp.rt)
    prac_trials.addData('SST_resp.started', SST_resp.tStartRefresh)
    prac_trials.addData('SST_resp.stopped', SST_resp.tStopRefresh)
    prac_trials.addData('ISI.started', ISI.tStart)
    prac_trials.addData('ISI.stopped', ISI.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(1.750000)
    # update component parameters for each repeat
    # Mistake Code
    
    if ssig and not SST_resp.corr:
        msg = "You should NOT have pressed!"
    elif not ssig and not SST_resp.corr:
        msg = "You should have pressed!"
    else:
        msg = "Correct!"
    feedbackMsg.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg, ISI_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackMsg* updates
        if feedbackMsg.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.tStart = t  # local t and not account for scr refresh
            feedbackMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        if feedbackMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMsg.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMsg.tStop = t  # not accounting for scr refresh
                feedbackMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(False)
        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            ISI_2.start(0.25)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    prac_trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    prac_trials.addData('ISI_2.started', ISI_2.tStart)
    prac_trials.addData('ISI_2.stopped', ISI_2.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_trials'


# ------Prepare to start Routine "expStartScreen"-------
# update component parameters for each repeat
expStartKey.keys = []
expStartKey.rt = []
# keep track of which components have finished
expStartScreenComponents = [expStartScreenText, expStartKey]
for thisComponent in expStartScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
expStartScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "expStartScreen"-------
while continueRoutine:
    # get current time
    t = expStartScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=expStartScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *expStartScreenText* updates
    if expStartScreenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        expStartScreenText.frameNStart = frameN  # exact frame index
        expStartScreenText.tStart = t  # local t and not account for scr refresh
        expStartScreenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(expStartScreenText, 'tStartRefresh')  # time at next scr refresh
        expStartScreenText.setAutoDraw(True)
    
    # *expStartKey* updates
    waitOnFlip = False
    if expStartKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        expStartKey.frameNStart = frameN  # exact frame index
        expStartKey.tStart = t  # local t and not account for scr refresh
        expStartKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(expStartKey, 'tStartRefresh')  # time at next scr refresh
        expStartKey.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(expStartKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if expStartKey.status == STARTED and not waitOnFlip:
        theseKeys = expStartKey.getKeys(keyList=['return'], waitRelease=False)
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
    for thisComponent in expStartScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "expStartScreen"-------
for thisComponent in expStartScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('expStartScreenText.started', expStartScreenText.tStartRefresh)
thisExp.addData('expStartScreenText.stopped', expStartScreenText.tStopRefresh)
# the Routine "expStartScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
experimental_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_cond_V4.xlsx'),
    seed=None, name='experimental_trials')
thisExp.addLoop(experimental_trials)  # add the loop to the experiment
thisExperimental_trial = experimental_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperimental_trial.rgb)
if thisExperimental_trial != None:
    for paramName in thisExperimental_trial:
        exec('{} = thisExperimental_trial[paramName]'.format(paramName))

for thisExperimental_trial in experimental_trials:
    currentLoop = experimental_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExperimental_trial.rgb)
    if thisExperimental_trial != None:
        for paramName in thisExperimental_trial:
            exec('{} = thisExperimental_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    # Should a stop signal display?
    if ssig:
        ssigOpp = 1
    else:
        ssigOpp = 0
    arrow.setImage(arrows)
    stop.setOpacity(ssigOpp)
    stop.setImage(ssigImg)
    SST_resp.keys = []
    SST_resp.rt = []
    # keep track of which components have finished
    trialComponents = [fix, arrow, stop, SST_resp, ISI]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *stop* updates
        if stop.status == NOT_STARTED and tThisFlip >= ssigStartThis-frameTolerance:
            # keep track of start time/frame for later
            stop.frameNStart = frameN  # exact frame index
            stop.tStart = t  # local t and not account for scr refresh
            stop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop, 'tStartRefresh')  # time at next scr refresh
            stop.setAutoDraw(True)
        if stop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop.tStartRefresh + ssigDur-frameTolerance:
                # keep track of stop time/frame for later
                stop.tStop = t  # not accounting for scr refresh
                stop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop, 'tStopRefresh')  # time at next scr refresh
                stop.setAutoDraw(False)
        
        # *SST_resp* updates
        waitOnFlip = False
        if SST_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            SST_resp.frameNStart = frameN  # exact frame index
            SST_resp.tStart = t  # local t and not account for scr refresh
            SST_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SST_resp, 'tStartRefresh')  # time at next scr refresh
            SST_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(SST_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(SST_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if SST_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SST_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                SST_resp.tStop = t  # not accounting for scr refresh
                SST_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SST_resp, 'tStopRefresh')  # time at next scr refresh
                SST_resp.status = FINISHED
        if SST_resp.status == STARTED and not waitOnFlip:
            theseKeys = SST_resp.getKeys(keyList=['c', 'm'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                SST_resp.keys = theseKeys.name  # just the last key pressed
                SST_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (SST_resp.keys == str(corrAns)) or (SST_resp.keys == corrAns):
                    SST_resp.corr = 1
                else:
                    SST_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Control Stop Signal Difficulty
    if ssig and corrAns and ssigStartLast >= 1.05:
        ssigStartThis = ssigStartLast - 0.1
        ssigDur = 2 - ssigStartThis
    elif ssig and not corrAns and ssigStartLast <= 1.35:
        ssigStartThis = ssigStartLast + 0.1
        ssigDur = 2 - ssigStartThis
    experimental_trials.addData('fix.started', fix.tStartRefresh)
    experimental_trials.addData('fix.stopped', fix.tStopRefresh)
    experimental_trials.addData('arrow.started', arrow.tStartRefresh)
    experimental_trials.addData('arrow.stopped', arrow.tStopRefresh)
    experimental_trials.addData('stop.started', stop.tStartRefresh)
    experimental_trials.addData('stop.stopped', stop.tStopRefresh)
    # check responses
    if SST_resp.keys in ['', [], None]:  # No response was made
        SST_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           SST_resp.corr = 1;  # correct non-response
        else:
           SST_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for experimental_trials (TrialHandler)
    experimental_trials.addData('SST_resp.keys',SST_resp.keys)
    experimental_trials.addData('SST_resp.corr', SST_resp.corr)
    if SST_resp.keys != None:  # we had a response
        experimental_trials.addData('SST_resp.rt', SST_resp.rt)
    experimental_trials.addData('SST_resp.started', SST_resp.tStartRefresh)
    experimental_trials.addData('SST_resp.stopped', SST_resp.tStopRefresh)
    experimental_trials.addData('ISI.started', ISI.tStart)
    experimental_trials.addData('ISI.stopped', ISI.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(1.750000)
    # update component parameters for each repeat
    # Mistake Code
    
    if ssig and not SST_resp.corr:
        msg = "You should NOT have pressed!"
    elif not ssig and not SST_resp.corr:
        msg = "You should have pressed!"
    else:
        msg = "Correct!"
    feedbackMsg.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg, ISI_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackMsg* updates
        if feedbackMsg.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.tStart = t  # local t and not account for scr refresh
            feedbackMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        if feedbackMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMsg.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMsg.tStop = t  # not accounting for scr refresh
                feedbackMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(False)
        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            ISI_2.start(0.25)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experimental_trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    experimental_trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    experimental_trials.addData('ISI_2.started', ISI_2.tStart)
    experimental_trials.addData('ISI_2.stopped', ISI_2.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'experimental_trials'


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
