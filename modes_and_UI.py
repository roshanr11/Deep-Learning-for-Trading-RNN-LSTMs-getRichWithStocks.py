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

from ipynb.fs.full.v1mainstockfile_notebookversion import *

# source: https://datatofish.com/matplotlib-charts-tkinter-gui/
#####


class startMode(Mode):
    def redrawAll(mode, canvas):
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
        mode.data = None

    def keyPressed(mode, event):
        # data, stock = getData()
        if event.key == 'd':
            # data = None
            while True:
                mode.data, mode.stock = getData(mode)
                if mode.data != None:
                    break

    


    #     data = yf.download(stock, openingInp, closingInp)
    #     return data, stock 

    

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, 
                                fill = 'green')

        canvas.create_text(mode.app.width/2, mode.app.height/2, text = 'MLR to be implemented here')

        if mode.data != None:

            mode.data = calcCCI(mode.data, 30)
            mode.data = calcMA(mode.data, 5, 'simple')

            mlrRecommendation(mode.data, 5, 3, 5)


class button2Mode(Mode):
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, 
                                fill = 'maroon')

        canvas.create_text(mode.app.width/2, mode.app.height/2, text = 'LSTMM to be implemented here')


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

    # def redrawAll(mode, canvas):
    #     # root = Tk()
    #     # figure = plt.Figure(figsize=(6,5), dpi=100)
    #     # ax = figure.add_subplot(111)
    #     # chart_type = FigureCanvasTkAgg(figure, root)
    #     # chart_type.get_tk_widget().pack()
    #     # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    #     # ax.set_title('The Title of your chart')
    #     Data1 = {'Country': ['US','CA','GER','UK','FR'],
    #     'GDP_Per_Capita': [45000,42000,52000,49000,47000]}

    #     df1 = DataFrame(Data1, columns= ['Country', 'GDP_Per_Capita'])
    #     df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()



    #     Data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
    #             'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    #         }
        
    #     df2 = DataFrame(Data2,columns=['Year','Unemployment_Rate'])
    #     df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()



    #     Data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
    #             'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
    #         }
        
    #     df3 = DataFrame(Data3,columns=['Interest_Rate','Stock_Index_Price'])
        

    #     figure1 = plt.Figure(figsize=(6,5), dpi=100)
    #     ax1 = figure1.add_subplot(111)
    #     bar1 = FigureCanvasTkAgg(figure1, root)
    #     bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     df1.plot(kind='bar', legend=True, ax=ax1)
    #     ax1.set_title('Country Vs. GDP Per Capita')


    #     figure2 = plt.Figure(figsize=(5,4), dpi=100)
    #     ax2 = figure2.add_subplot(111)
    #     line2 = FigureCanvasTkAgg(figure2, root)
    #     line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    #     ax2.set_title('Year Vs. Unemployment Rate')


    #     figure3 = plt.Figure(figsize=(5,4), dpi=100)
    #     ax3 = figure3.add_subplot(111)
    #     ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
    #     scatter3 = FigureCanvasTkAgg(figure3, root) 
    #     scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     ax3.legend() 
    #     ax3.set_xlabel('Interest Rate')
    #     ax3.set_title('Interest Rate Vs. Stock Index Price')

    #     root.mainloop()


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
