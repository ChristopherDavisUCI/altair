# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T
from ..baseobject import BaseObject
from .scaleconfig import ScaleConfig
from .legendconfig import LegendConfig
from .axisconfig import AxisConfig
from .facetconfig import FacetConfig
from .cellconfig import CellConfig
from .markconfig import MarkConfig


class Config(BaseObject):
    scale = T.Instance(ScaleConfig, default_value=None, allow_none=True)
    timeFormat = T.Unicode(default_value=None, allow_none=True, help="""Default datetime format for axis and legend labels.""")
    legend = T.Instance(LegendConfig, default_value=None, allow_none=True)
    background = T.Unicode(default_value=None, allow_none=True, help="""CSS color property to use as background of visualization.""")
    viewport = T.CFloat(default_value=None, allow_none=True, help="""The width and height of the on-screen viewport, in pixels.""")
    axis = T.Instance(AxisConfig, default_value=None, allow_none=True)
    facet = T.Instance(FacetConfig, default_value=None, allow_none=True)
    cell = T.Instance(CellConfig, default_value=None, allow_none=True)
    numberFormat = T.Unicode(default_value=None, allow_none=True, help="""D3 Number format for axis labels and text tables.""")
    mark = T.Instance(MarkConfig, default_value=None, allow_none=True)
