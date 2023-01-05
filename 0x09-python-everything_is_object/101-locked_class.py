class LockedClass:
    def setattr(self, name, value):
        if name == "first_name":
            self.dict[name] = value
        else:
            raise AttributeError("Cannot set attribute '{}'".format(name))
