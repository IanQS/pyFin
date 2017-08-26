# coding: utf-8
# Handle the plotting
import matplotlib.pyplot as plt
from matplotlib import style
style.use("seaborn-deep")

# For data processing
import pandas as pd
import numpy as np

# For getting the data

import os


data_src = "S&P500_joined_adj-close.csv"


# In[ ]:


def visualize_corr(data_src, plot_parts=True, heatmap=False):
    """
    data_src:
        string
        string where the data is stored

    plot_parts:
        Bool
        whether to constrict the values of the graph when plotting
        - only used when heatmap is True

    heatmap:
        Bool
        whether to use a colored heatmap when plotting
    """

    df = pd.read_csv(data_src)
    corr = df.corr()

    if not os.path.exists("imgs/"):
        os.mkdir("imgs/")

    if heatmap:
        if not plot_parts:
            corr_dict = {"whole": [corr, (-1, 1)]}
        else:
            sP = corr.where(corr > 0.50, 0.5)
            wP = corr.where((corr <= 0.50) & (corr > 0), 0)
            sN = corr.where(corr <= -0.50, -0.5)
            wN = corr.where((corr > -0.50) & (corr <= 0), -0.5)
            corr_dict = {"sP": [sP, (0.5, 1)], "wP": [wP, (0, 0.5)],
                         "sN": [sN, (-1, -0.5)], "wN": [wN, (-0.5, 0)]}
        # We put the default as the min value since it's unlikely to happen

        for k, [corr_matrix, range_] in corr_dict.items():
            data = corr_matrix.values
            fig = plt.figure(figsize=(30, 30))
            ax = fig.add_subplot(1, 1, 1)

            heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
            fig.colorbar(heatmap)
            ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
            ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
            ax.invert_yaxis()
            ax.xaxis.tick_top()

            column_labels = corr_matrix.columns
            row_labels = corr_matrix.index

            ax.set_xticklabels(column_labels)
            ax.set_yticklabels(row_labels)
            plt.xticks(rotation=90)
            heatmap.set_clim(range_)
            plt.tight_layout()
            plt.savefig("imgs/{0}_heatmap.png".format(k), dpi=300)
            plt.close()

            # Upon inspection we see that there are some
            # correlations between the data, which means
            # we could probably try to predict things?
    else:
        sP = corr > 0.50
        wP = (corr <= 0.50) & (corr > 0)
        sN = corr <= -0.50
        wN = (corr > -0.50) & (corr <= 0)

        corr_dict = {"sP": sP, "wP": wP, "sN": sN, "wN": wN}

        for k, corr_matrix in corr_dict.items():
            data = corr_matrix.values
            fig = plt.figure(figsize=(30, 30))
            ax = fig.add_subplot(1, 1, 1)

            heatmap = ax.pcolor(data, cmap="Greys")
            ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
            ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
            ax.invert_yaxis()
            ax.xaxis.tick_top()

            column_labels = corr_matrix.columns
            row_labels = corr_matrix.index

            ax.set_xticklabels(column_labels)
            ax.set_yticklabels(row_labels)
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.title("Graph of {0}".format(k))
            plt.savefig("imgs/{0}_boolean.png".format(k), dpi=300)
            plt.close()


"""
I'm personally finding the grey maps of booleans to be easier to
interpret than the heatmaps so I added a flag to visualize either.
"""

print()
