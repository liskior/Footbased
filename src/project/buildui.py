from pyxley.charts.mg import Figure, Histogram, LineChart, ScatterPlot
from pyxley.filters import SelectButton
from pyxley import UILayout, register_layouts
import pandas as pd
from os import path

from collections import OrderedDict
from flask import request, jsonify


def create_line_plot(df, i, name):
    """ create a mg line plot

        Args:
            df (pandas.DataFrame): data to plot
    """
    fig = Figure("/mg/line_plot" + str(i), "mg_line_plot")
    fig.graphics.transition_on_update(True)
    fig.graphics.animate_on_load()
    fig.graphics.point_size(2.0)
    fig.layout.set_size(width=450 + 10*i, height=210)
    fig.layout.set_margin(left=40, right=40)
    fig.axes.set_min_y_from_data(True)
    fig.axes.set_inflator(1.005)
    fig.axes.set_xticks_count(3)
    return LineChart(df=df, figure=fig, x="Year", y=["value"],
                     init_params={"Data": name},
                     timeseries=True)


def make_mg_layout(filename):
    # load a dataframe
    df = pd.read_csv(filename)
    # Make a UI
    ui = UILayout("FilterChart")
    # Make a Button
    cols = [c for c in df.columns if c != "Year"]
    btn = SelectButton("Abschlussprüfungsleistungen", cols, "Data", "Abschlussprüfungsleistungen")

    # add the button to the UI
    ui.add_filter(btn)

    # stack the dataframe
    _stack = df.set_index("Year").stack().reset_index()
    _stack = _stack.rename(columns={"level_1": "Data", 0: "value"})

    # Make a Figure, add some settings, make a line plot
    ui.add_chart(create_line_plot(_stack, i=0, name="Abschlussprüfungsleistungen"))

    here = path.abspath(path.dirname(__file__))

    df1 = pd.read_csv(here + "/file")
    # Make a Button
    cols1 = [c for c in df1.columns if c != "Year"]
    btn1 = SelectButton("Professionals", cols1, "Data", "Professionals")

    # add the button to the UI
    ui.add_filter(btn1)
    _stack1 = df1.set_index("Year").stack().reset_index()
    _stack1 = _stack1.rename(columns={"level_1": "Data", 0: "value"})

    # Make a Figure, add some settings, make a line plot
    ui.add_chart(create_line_plot(_stack1, i=1, name="Professionals"))

    # stack the dataframe


    return ui


def get_layouts(mod, filename):
    # metrics graphics
    mg_ui = make_mg_layout(filename)
    mg_ui.assign_routes(mod)
    mg_props = mg_ui.build_props()

    _layouts = OrderedDict()
    _layouts["mg"] = {"layout": [mg_props], "title": "metrics-graphics"}

    register_layouts(_layouts, mod)
