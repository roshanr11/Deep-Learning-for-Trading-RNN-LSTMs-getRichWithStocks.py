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
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.mainMode)

    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text = 'Instructions: ', font = font)
        canvas.create_text(mode.width/2, 200, text = 'Click the jawn you wish to jawn! \n\n   Happy stockJawning.', 
                           font = font)

class mainMode(Mode):
    # data = getData()
    showStock()
    data = calcMA(data, 5, 'simple')
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
        app.helpMode = HelpMode()
        app.setActiveMode(app.startMode)
        app.timerDelay = 50


# def runCreativeSideScroller():
MyModalApp(width=500, height=500)
