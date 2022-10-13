# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=bad-mcs-classmethod-argument
# pylint: disable=bad-super-call
# pylint: disable=redefined-builtin
# pylint: disable=unused-argument


class Meta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        for k in tuple(classdict.keys()):
            if not (k.startswith("__") and k.endswith("__")):
                classdict[f"custom_{k}"] = classdict.pop(k)

        def setattr(self, key, value):
            return super(cls, self).__setattr__(f"custom_{key}", value)

        classdict["__setattr__"] = setattr
        cls = super().__new__(mcs, name, bases, classdict)
        return cls
