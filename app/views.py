import calendar
import logging

from flask_appbuilder.charts.views import DirectByChartView
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Data

log = logging.getLogger(__name__)

class DataView(ModelView):
    datamodel = SQLAInterface(Data)
    list_columns = ["id", "cislo"]

class DataChartView(DirectByChartView):
    datamodel = SQLAInterface(Data)
    chart_title = "Data"
    definitions = [
        {
            "group": "id",
            "series": ["cislo"],
        }
    ]


db.create_all()
appbuilder.add_view(
    DataView,
    "Data",
    icon="fa-folder-open-o",
    category="Data",
)
appbuilder.add_view(
    DataChartView,
    "Chart",
    icon="fa-folder-open-o",
    category="Data",
)