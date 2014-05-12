#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput

import sys
import re

import prettyplotlib as ppl
import numpy as np
from prettyplotlib import plt

"""
sample,ng/ul,Title
value1
value2
"""

y = []
for line in fileinput.input():
    line = line.strip()

    res = re.search("[0-9]", line)
    if not res:
        line = line.split(",")
        x_lab = line[0]
        y_lab = line[1]
        main = line[2]
    else:
        y.append(float(line))
        print line

x = range(1, len(y) + 1)

plt.rc('font', **{'family': 'DejaVu Sans'})
fig, ax = plt.subplots(1, figsize=(8, 6))

width = 0.2
ind = np.arange(len(y))
xdata = ind + 0.05 + width
ax.bar(ind, y)
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(x)
ax.autoscale()
ax.set_title(
    main,
    fontdict={'fontsize': 20}
)

plt.ylabel(y_lab, fontdict={'fontsize': 15})
plt.xlabel(x_lab, fontdict={'fontsize': 15})
plt.tick_params(axis="y", which="major", labelsize=10)
plt.tick_params(axis="x", which="major", labelsize=10)

ppl.bar(ax, np.arange(len(y)), y, grid="y")


plt.tight_layout()
fig.savefig("out.png")
