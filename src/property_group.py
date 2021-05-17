from bpy.types import PropertyGroup

class PG(PropertyGroup):
    @staticmethod
    def prop_methods(call, prop=None):
        def getter(self):
            try:
                value = self[prop] if self[prop] else self.defaults[prop]
            except:
                value = self.defaults[prop]
                self[prop] = value
                if hasattr(self, "on_load"):
                    self.on_load()
            finally:
                return value

        def setter(self, value):
            self[prop] = value

        def updater(self, context):
            self.update(context)

        methods = {
            "GET": getter,
            "SET": setter,
            "UPDATE": updater,
            }

        return methods[call]
