# Author: Roshan Ram
# andrewID: rram

from cmu_112_graphics import *
# cmu_112_graphics framework credit:
# http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

import tkinter as tk
from tkinter import *
import random
from PIL import Image
# import import_ipynb
# template: from ipynb.fs.full.<notebookname> import *
# import v1mainstockfile_notebookversion # ipynb file main
# from mainstocks import *


import pandas as pd
from pandas import *

#####
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

####

from ipynb.fs.full.v1mainstockfile_notebookversion import *

# from ipynb.fs.full.v1REALTP_lstm_stuff import *

from ipynb.fs.full.BACKUPv1REALTP_lstm_stuff import *

# source: https://datatofish.com/matplotlib-charts-tkinter-gui/
#####


class startMode(Mode):
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'orange')
        font = 'Arial 26 bold'
        canvas.create_text(mode.width / 2, 150, text='Welcome to', font=font)
        canvas.create_text(mode.width / 2, 200, text='getRichWithStocks.py', font=font)
        canvas.create_text(mode.width / 2, 250, text='Press any key for the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.instructionsMode)


class instructionsMode(Mode):
    def appStarted(mode):

        mode.button1 = (mode.width*(2/10), mode.height*(6/10), mode.width*(4/10), 
        mode.height*(8/10), 'blue')

        mode.text1 = (mode.button1[0] + (mode.button1[2] - mode.button1[0])/2, 
                      mode.button1[1] + (mode.button1[3] - mode.button1[1])/2,
                      'Helvetica 17 bold')

        mode.button2 = (mode.width*(6/10), mode.height*(6/10), mode.width*(8/10), 
        mode.height*(8/10), 'green')

        mode.text2 = (mode.button2[0] + (mode.button2[2] - mode.button2[0])/2, 
                      mode.button2[1] + (mode.button2[3] - mode.button2[1])/2,
                      'Helvetica 17 bold')


    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.mainMode)


    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'

        ##############################

        # randColor = random.choice(['blue', 'green'])
        randColor = 'lightblue'

        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill = randColor)

        ##############################

        canvas.create_text(mode.width/2, 150, text = 'Instructions: ', font = font)
        canvas.create_text(mode.width/2, 200, text = 'Click the model type\nyou wish to proceed with!', 
                           font = font)

        canvas.create_rectangle(mode.button1[0], mode.button1[1], mode.button1[2], 
                                mode.button1[3], fill = mode.button1[-1]) # button #1

        canvas.create_text(mode.text1[0], mode.text1[1], text = 'Multiple\nLinear\nRegression',
                            font = mode.text1[-1]) # text #2

        canvas.create_rectangle(mode.button2[0], mode.button2[1], mode.button2[2], 
                                mode.button2[3], fill = mode.button2[-1]) # button #2

        canvas.create_text(mode.text2[0], mode.text2[1], text = 'Long\nShort-Term\nMemory\nModel',
                            font = mode.text2[-1]) # text #2

        # canvas.create_rectangle(mode.width/10, 0, 
        #                         mode.width/2 + 100, mode.height/2 + 200, 
        #                         fill = 'black')

    def mousePressed(mode, event):
        if mode.button1[0] <= event.x <= mode.button1[2] and \
            mode.button1[1] <= event.y <= mode.button1[3]:
            mode.app.setActiveMode(mode.app.button1mode)

        if mode.button2[0] <= event.x <= mode.button2[2] and \
            mode.button2[1] <= event.y <= mode.button2[3]:
            mode.app.setActiveMode(mode.app.button2mode)


class button1Mode(Mode):

    # def getData(app):
    #     stock = None
    #     while not isinstance(stock, str):
    #         stock = app.getUserInput("Enter your desired stock. Only alphanumeric characters please.")
    #         openingInp = app.getUserInput("Enter your desired opening date. (yyyy-mm-dd)") #'2016-01-01'
    #         closingInp = app.getUserInput("Enter your desired closing date. (yyyy-mm-dd)") # '2019-08-01'



    def appStarted(mode):
        # data = None
        # while True:
        #     data, stock = getData(app)
        # print('test')
        # inp = app.getUserInput("enter some input jawnson")
        # print(inp)

        # mode.data, mode.stock = getData(mode) 
        mode.data = None
        mode.dataExists = False

    def keyPressed(mode, event):
        # data, stock = getData()
        if event.key == 'd':
            # data = None
            # while True:
            mode.data, mode.stock = getData(mode)
            if type(mode.data) is not None:
                print("made it to dataExists")
                mode.dataExists = True

                # if None in pd.Series(mode.data): # mode.data != None:
                #     break

    


    #     data = yf.download(stock, openingInp, closingInp)
    #     return data, stock 

    

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, 
                                fill = 'green')

        canvas.create_text(mode.app.width/2, mode.app.height/3,
                         text = 'PRESS D TO BEGIN', font = 'helvetica 35 bold') # shortcut to prevent crashes

        canvas.create_text(mode.app.width/2, mode.app.height/2, text = 'Multiple Linear Regression:')

        # if mode.data != None:

        if mode.dataExists:
            print(mode.data)
            # mode.data = calcCCI(mode.data, 30)
            # mode.data = calcMA(mode.data, 5, 'simple')

            mlrRecommendation(mode.data, 5, 3, 5)
            mode.dataExists = False


class button2Mode(Mode):
    def keyPressed(mode, event):
        if event.key == 'd':
            # %run 15112TP_lstm_stuff.ipynb
            # from ipynb.fs.full.v1mainstockfile_notebookversion import *

            print('getting data...')
            # data, stock = getData(mode)
            ####

            # usingSavedModel = False

            data, stock = getData_LSTM(mode)

            x_train, x_test = mainFunc1(data)  # IMP!
            x_t, y_t, x_val, x_test_t, y_val, y_test_t = mainFunc2(x_test, x_train)  # IMP!


            if not usingSavedModel:
                history = trainModel(x_t, y_t, x_val, y_val, model, 300)  # IMP!
                f = open('history.pckl', 'wb')
                pickle.dump(history, f)
                f.close()
            else:
                f = open('history.pckl', 'rb')
                history = pickle.load(f)
                f.close()


            if not usingSavedModel:
                model = create_model(x_t)  # IMP!
                
                today = date.today()
                d4 = today.strftime("%b-%d-%Y")
                # ^Credit: https://www.programiz.com/python-programming/datetime/current-datetime

                fileName = f'{d4}_savedLSTM.h5' 
                model.save(fileName)
                print(f"Saved model `{fileName}` to disk")
            else:
                today = date.today()
                d4 = today.strftime("%b-%d-%Y")
                # ^Credit: https://www.programiz.com/python-programming/datetime/current-datetime

                fileName = f'{d4}_savedLSTM.h5' 
                model = load_model(fileName)


            # if not usingSavedModel:
            # history = trainModel(x_t, y_t, x_val, y_val, model, 300)  # IMP!

            y_pred_org, y_test_t_org = createPredictions_LSTM(model, x_test_t, y_test_t) #IMP!


            print('here is the loss for the model that was trained on this stock')
            plotLoss(history) #IMP!
            print("here's the error for that model")
            print(calcError(model, x_test_t, y_test_t, y_pred_org, y_test_t_org)) #IMP!
            print('here is the prediction using that model')
            plotPrediction(y_pred_org, y_test_t_org) # IMP!

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, 
                                fill = 'maroon')
        
        canvas.create_text(mode.app.width/2, mode.app.height/3,
                           text = 'PRESS D TO BEGIN', font = 'helvetica 35 bold')

        canvas.create_text(mode.app.width/2, mode.app.height/2, text = 'Long-Short Term Memory Model (LSTM)')


class mainMode(Mode):
    # data = getData()

    # showStock()
    # data = calcMA(data, 5, 'simple')

    # plotPrediction(data, 5)



    def appStarted(mode):
        root = tk.Tk() 

    def keyPressed(mode, event):
        pass

    # def mouseMoved(mode, event):
    #     mode.cursorPos = [event.x, event.y]

    def mousePressed(mode, event):
        pass

    def mouseReleased(mode, event):
        pass

    def mouseDragged(mode, event):
        pass

class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width / 2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width / 2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width / 2, 350, text='Press any key to return to the game!', font=font)


class MyModalApp(ModalApp):
    def appStarted(app):
        app.startMode = startMode()
        app.instructionsMode = instructionsMode()
        app.mainMode = mainMode()

        # buttons
        app.button1mode = button1Mode()
        app.button2mode = button2Mode()

        # do i need this help part?
        app.helpMode = HelpMode()
        app.setActiveMode(app.startMode)
        app.timerDelay = 50


# def runCreativeSideScroller():
MyModalApp(width=500, height=500)



####################################################################################

# TP-a-Thon Notes: 
# tkinter packing (geometrical packing for matplotlib overlay onto tkinter?) 
# (not sure if it works with matplotlib)

# add some kind of background 
# bouncing square, pattern in background 

########

# add purpose of game
# explanations/run modes within 

######

# 12/4
# labels to axes
# label for title of graph

####

# 3 different models
# explanations
# add fractals to UI


# important:

# help mode/actual instructions

# get UI working
# explanations
# metrics to show accuracy 
# improve LSTM

####################################

# For thursday:

# MAKE INSTRUCTIONS/EXPLANATIONS ASAP
# MAKE VIDEO ASAP!!!
# make MLR work with dialogue boxes, not in console
# MAKE SURE LSTM IS RUNNING FINE
# tweak code
# polish UI
# fractals