from numpy import asarray

from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from chaco.api import ArrayPlotData
from enable.api import ComponentEditor

from tn.model.date import date_dt_list_1
from tn.model.float import float_list_1
from chaco.shell.scaly_plot import ScalyPlot
from chaco.scales.api import CalendarScaleSystem


class LinePlot(HasTraits):
    plot = Instance(ScalyPlot)

    traits_view = View(
        Item('plot', editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def _plot_default(self):
        x = asarray(date_dt_list_1)
        y = asarray(float_list_1)
        plotdata = ArrayPlotData(x=x, y=y)

        plot = ScalyPlot(plotdata, linear_scale_factory=CalendarScaleSystem)
        plot.plot(("x", "y"), type="line", color="blue")
        plot.title = "demo"

        return plot


if __name__ == "__main__":
    LinePlot().configure_traits()
