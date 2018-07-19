from pyxley.charts.mg import Figure, Histogram, LineChart, ScatterPlot
from pyxley.filters import SelectButton
from pyxley import UILayout, register_layouts
import pandas as pd

from collections import OrderedDict
from flask import request, jsonify


def create_line_plot(df):
    """ create a mg line plot

        Args:
            df (pandas.DataFrame): data to plot
    """
    fig = Figure("/mg/line_plot/", "mg_line_plot")
    fig.graphics.transition_on_update(True)
    fig.graphics.animate_on_load()
    fig.graphics.x_rug()
    fig.graphics.y_rug()
    fig.graphics.point_size(2.0)
    fig.layout.set_size(width=450, height=210)
    fig.layout.set_margin(left=40, right=40)
    fig.axes.set_min_y_from_data(True)
    fig.axes.set_inflator(1.005)
    fig.axes.set_xticks_count(3)
    return LineChart(df=df, figure=fig, x="Year", y=["value"],
                     init_params={"Data": "Abschlussprüfungsleistungen"},
                     timeseries=True,
                     title="Boring Data of boring firm")


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
    ui.add_chart(create_line_plot(_stack))

    return ui


def get_layouts(mod, filename):
    # metrics graphics
    mg_ui = make_mg_layout(filename)
    mg_ui.assign_routes(mod)
    mg_props = mg_ui.build_props()

    _layouts = OrderedDict()
    _layouts["mg"] = {"layout": [mg_props], "title": "metrics-graphics"}

    register_layouts(_layouts, mod)
