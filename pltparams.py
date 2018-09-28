#!/usr/bin/env python
#
import numpy as np
import matplotlib
matplotlib.use('pgf') # change to ps in case one wants to save as eps (?)
import matplotlib.pyplot as plt
#
def initfig(width = 246.0, ar = (np.sqrt(5)-1.0)/2.0, scl = 0.95):
    fig_width_pt  = width                                # \showthe\columnwidth
    inches_per_pt = 1.0/72.27                            # pt to in
    aspect_ratio  = ar                                   # aspect ratio
    fig_scale     = scl                                  # scale factor
    fig_width     = fig_width_pt*inches_per_pt*fig_scale # width in in
    fig_height    = fig_width*aspect_ratio               # height in in
    fig_size      = [fig_width,fig_height]               # final dimensions
    #
    pgf_with_latex = {                  # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "font.size": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": fig_size,
    "pgf.preamble": [
    r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
    r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
                    ]
    }
    matplotlib.rcParams.update(pgf_with_latex)
initfig()
#
def format(x, pos):
    'The two args are the value and tick position'
    return '%1.2g' % (x)
#
def newfig():
    plt.cla()
    plt.clf()
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    formatter = matplotlib.ticker.FuncFormatter(format)
    return fig, ax, formatter
#
def set_axis(ax,xmin, xmax, ymin, ymax,
             formatter, isformatx = True, isformaty = True):
    if(isformatx):
        ax.xaxis.set_major_formatter(formatter)
    if(isformaty):
        ax.yaxis.set_major_formatter(formatter)
    #
    offset = 1.0e-8
    ax.axis([xmin,xmax*(1.+offset),ymin,ymax*(1.+offset)])
#
def set_ticks(ax, isminorx=True, isminory=True,tw=0.8,tp=2,tl=4,tmw=0.3,tml=2,lw = 0.8):
    ax.tick_params(axis='x', width=tw, pad=tp, length=tl)
    ax.tick_params(axis='y', width=tw, pad=tp, length=tl)
    ax.tick_params(which='minor', width=tmw, length=tml)
    ax.tick_params(direction='in')
    #
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.get_xaxis().tick_bottom()
    ax.spines['bottom'].set_linewidth(lw)
    ax.spines['left'].set_linewidth(lw)
    #
    if(isminorx):
        ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    if(isminory):
        ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
#
def set_ticks_inset(ax, tw = 0.4, tp = 2, tl = 3, lw = 0.7):
    ax.tick_params(axis='x', width=tw, pad=tp, length=tl)
    ax.tick_params(axis='y', width=tw, pad=tp, length=tl)
    ax.tick_params(direction='in')
    #
    ax.spines['top'].set_visible(True )
    ax.spines['right'].set_visible(True )
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.get_xaxis().tick_bottom()
    #
    ax.spines['bottom'].set_linewidth(lw)
    ax.spines['top'].set_linewidth(lw)
    ax.spines['left'].set_linewidth(lw)
    ax.spines['right'].set_linewidth(lw)
