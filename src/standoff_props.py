from bpy.props import PointerProperty, FloatProperty
from bpy.types import Mesh, Scene
from bpy.utils import register_class, unregister_class
from .standoff_mesh import Standoff
from .property_group import PG

class PG_Standoff(PG):
    metric_diameter: FloatProperty(
        name="Inner Diameter (Metric)",
        min=2,
        max=5,
        step=50,
        precision=1,
        set=PG.prop_methods("SET", "metric_diameter"),
        get=PG.prop_methods("GET", "metric_diameter"),
        update=PG.prop_methods("UPDATE"))
    height: FloatProperty(
        name="Standoff Height",
        min=2,
        max=6,
        step=25,
        precision=2,
        set=PG.prop_methods("SET", "height"),
        get=PG.prop_methods("GET", "height"),
        update=PG.prop_methods("UPDATE"))
    mesh: PointerProperty(type=Mesh)

    defaults = { "metric_diameter": 2.5, "height": 3 }

    standoff = Standoff()

    def on_load(self):
        if hasattr(self, "height") and hasattr(self, "metric_diameter"):
            self.__set_mesh()

    def update(self, context):
        self.__set_mesh()

    def __set_mesh(self):
        self.mesh = self.standoff.mesh(self.height, self.metric_diameter)

def register():
    register_class(PG_Standoff)
    Scene.Standoff = PointerProperty(type=PG_Standoff)

def unregister():
    unregister_class(PG_Standoff)
    del Scene.Standoff
