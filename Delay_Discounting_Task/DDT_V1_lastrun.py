#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 23, 2020, at 18:14
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
expName = 'DDT_V1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\James\\Desktop\\DDT\\DDT_V1_lastrun.py',
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
    size=[2560, 1080], fullscr=True, screen=0, 
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
DDTInstrMsg = visual.TextStim(win=win, name='DDTInstrMsg',
    text='Welcome to the “Money Task”!\n\nFor this task, you will be asked to make choices between two money alternatives. You will not actually receive the amounts of money you choose, but we want you to respond as if  you were given these options in real life. These choices will be displayed on the screen. One amount of money will always be available immediately, and the other amount will always be delayed.At times, the delay will change. If you would prefer to have the amount shown on the left, PRESS THE C KEY. If you would prefer to have the amount on the right, PRESS THE M KEY.  There are no correct or incorrect choices. We are interested in which option you would prefer.\n\nPRESS Y TO START...',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
DDTInsrKeys = keyboard.Keyboard()

# Initialize components for Routine "delayPrompt"
delayPromptClock = core.Clock()
delayPomptText = visual.TextStim(win=win, name='delayPomptText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
delayPromptKey = keyboard.Keyboard()

# Initialize components for Routine "DDTTrial"
DDTTrialClock = core.Clock()
which = visual.TextStim(win=win, name='which',
    text='Which would you prefer?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
smallerSoonerText = visual.TextStim(win=win, name='smallerSoonerText',
    text='default text',
    font='Arial',
    pos=(-0.3, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
largerLaterText = visual.TextStim(win=win, name='largerLaterText',
    text='default text',
    font='Arial',
    pos=(0.3, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
DDTKeys = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
DDTInsrKeys.keys = []
DDTInsrKeys.rt = []
# keep track of which components have finished
InstructionsComponents = [DDTInstrMsg, DDTInsrKeys]
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
    
    # *DDTInstrMsg* updates
    if DDTInstrMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DDTInstrMsg.frameNStart = frameN  # exact frame index
        DDTInstrMsg.tStart = t  # local t and not account for scr refresh
        DDTInstrMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DDTInstrMsg, 'tStartRefresh')  # time at next scr refresh
        DDTInstrMsg.setAutoDraw(True)
    
    # *DDTInsrKeys* updates
    waitOnFlip = False
    if DDTInsrKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DDTInsrKeys.frameNStart = frameN  # exact frame index
        DDTInsrKeys.tStart = t  # local t and not account for scr refresh
        DDTInsrKeys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DDTInsrKeys, 'tStartRefresh')  # time at next scr refresh
        DDTInsrKeys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(DDTInsrKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if DDTInsrKeys.status == STARTED and not waitOnFlip:
        theseKeys = DDTInsrKeys.getKeys(keyList=['y'], waitRelease=False)
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
thisExp.addData('DDTInstrMsg.started', DDTInstrMsg.tStartRefresh)
thisExp.addData('DDTInstrMsg.stopped', DDTInstrMsg.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DDT_conditions.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "delayPrompt"-------
    # update component parameters for each repeat
    # Set inital smaller sooner reward
    
    smallerSooner = 500
    largerLater = 1000
    delayPomptText.setText('The delay for the options on the right is now ' + str(block) + '\n \n PRESS Y TO CONTINUE')
    delayPromptKey.keys = []
    delayPromptKey.rt = []
    # keep track of which components have finished
    delayPromptComponents = [delayPomptText, delayPromptKey]
    for thisComponent in delayPromptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delayPromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "delayPrompt"-------
    while continueRoutine:
        # get current time
        t = delayPromptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delayPromptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *delayPomptText* updates
        if delayPomptText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            delayPomptText.frameNStart = frameN  # exact frame index
            delayPomptText.tStart = t  # local t and not account for scr refresh
            delayPomptText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayPomptText, 'tStartRefresh')  # time at next scr refresh
            delayPomptText.setAutoDraw(True)
        
        # *delayPromptKey* updates
        waitOnFlip = False
        if delayPromptKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            delayPromptKey.frameNStart = frameN  # exact frame index
            delayPromptKey.tStart = t  # local t and not account for scr refresh
            delayPromptKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayPromptKey, 'tStartRefresh')  # time at next scr refresh
            delayPromptKey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(delayPromptKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if delayPromptKey.status == STARTED and not waitOnFlip:
            theseKeys = delayPromptKey.getKeys(keyList=['y'], waitRelease=False)
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
        for thisComponent in delayPromptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delayPrompt"-------
    for thisComponent in delayPromptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('delayPomptText.started', delayPomptText.tStartRefresh)
    blocks.addData('delayPomptText.stopped', delayPomptText.tStopRefresh)
    # the Routine "delayPrompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=8, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "DDTTrial"-------
        # update component parameters for each repeat
        largerLaterText.setText(f'£ {largerLater:.2f} in ' + str(block))
        DDTKeys.keys = []
        DDTKeys.rt = []
        # keep track of which components have finished
        DDTTrialComponents = [which, smallerSoonerText, largerLaterText, DDTKeys]
        for thisComponent in DDTTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        DDTTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "DDTTrial"-------
        while continueRoutine:
            # get current time
            t = DDTTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=DDTTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *which* updates
            if which.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                which.frameNStart = frameN  # exact frame index
                which.tStart = t  # local t and not account for scr refresh
                which.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(which, 'tStartRefresh')  # time at next scr refresh
                which.setAutoDraw(True)
            
            # *smallerSoonerText* updates
            if smallerSoonerText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                smallerSoonerText.frameNStart = frameN  # exact frame index
                smallerSoonerText.tStart = t  # local t and not account for scr refresh
                smallerSoonerText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(smallerSoonerText, 'tStartRefresh')  # time at next scr refresh
                smallerSoonerText.setAutoDraw(True)
            if smallerSoonerText.status == STARTED:  # only update if drawing
                smallerSoonerText.setText(f'£ {smallerSooner:.2f} NOW', log=False)
            
            # *largerLaterText* updates
            if largerLaterText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                largerLaterText.frameNStart = frameN  # exact frame index
                largerLaterText.tStart = t  # local t and not account for scr refresh
                largerLaterText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(largerLaterText, 'tStartRefresh')  # time at next scr refresh
                largerLaterText.setAutoDraw(True)
            
            # *DDTKeys* updates
            waitOnFlip = False
            if DDTKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DDTKeys.frameNStart = frameN  # exact frame index
                DDTKeys.tStart = t  # local t and not account for scr refresh
                DDTKeys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DDTKeys, 'tStartRefresh')  # time at next scr refresh
                DDTKeys.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(DDTKeys.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(DDTKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if DDTKeys.status == STARTED and not waitOnFlip:
                theseKeys = DDTKeys.getKeys(keyList=['c', 'm'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    DDTKeys.keys = theseKeys.name  # just the last key pressed
                    DDTKeys.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in DDTTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "DDTTrial"-------
        for thisComponent in DDTTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if DDTKeys.keys == 'c':
            smallerSooner = smallerSooner * 0.5
        elif DDTKeys.keys == 'm':
            smallerSooner = smallerSooner * 1.5
        
        # Save data
        thisExp.addData('smallerSoonerValue', smallerSooner)
        thisExp.addData('largerLaterValue', largerLater)
        trials.addData('which.started', which.tStartRefresh)
        trials.addData('which.stopped', which.tStopRefresh)
        trials.addData('smallerSoonerText.started', smallerSoonerText.tStartRefresh)
        trials.addData('smallerSoonerText.stopped', smallerSoonerText.tStopRefresh)
        trials.addData('largerLaterText.started', largerLaterText.tStartRefresh)
        trials.addData('largerLaterText.stopped', largerLaterText.tStopRefresh)
        # check responses
        if DDTKeys.keys in ['', [], None]:  # No response was made
            DDTKeys.keys = None
        trials.addData('DDTKeys.keys',DDTKeys.keys)
        if DDTKeys.keys != None:  # we had a response
            trials.addData('DDTKeys.rt', DDTKeys.rt)
        trials.addData('DDTKeys.started', DDTKeys.tStartRefresh)
        trials.addData('DDTKeys.stopped', DDTKeys.tStopRefresh)
        # the Routine "DDTTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 8 repeats of 'trials'
    
# completed 1 repeats of 'blocks'


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
