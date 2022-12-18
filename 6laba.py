from dataclasses import dataclass

class Slot:
    # Имена системных слотов
    SYSTEMS_NAMES = ('Процедура')

    # УКАЗАТЕЛИ НАСЛЕДОВАНИЯ
    # Значение слота наследуется
    SAME = 'НАСЛЕДУЕТСЯ'
    # Значение слота не наследуется
    UNIQUE = 'НЕ_НАСЛЕДУЕТСЯ'
    # При отсутствии значения в текущем слоте оно наследуется из фрейма верхнего уровня,
    # однако в случае определения значения текущего слота оно может быть уникальным
    OVERRIDE = 'ПЕРЕОПРЕДЕЛЯЕТСЯ'
    # При наследовании значения из родителя слот не записывается в json
    FINAL = 'НЕ_ЗАПИСЫВАЕТСЯ'

    def __init__(self, name, value, inheritance_type, daemon = None):
        self._name = name
        self._type = value.__class__.__name__
        self._inheritance_type = inheritance_type
        self._value = value
        self._daemon = daemon

    def __getattr__(self, attr):
        return getattr(self._value, attr)

    def __iter__(self):
        return iter(self._value)

    @property
    def is_system(self):
        return self._name in self.SYSTEMS_NAMES

    @property
    def has_daemon(self):
        return self._daemon != None

    @property
    def daemon(self):
        return self._daemon

    @property
    def inheritance_type(self):
        return self._inheritance_type

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        # FIXME: TypeError: Object of type 'function' is not JSON serializable
        return self._value  # or self._daemon

    # noinspection PyCallingNonCallable
    @value.setter
    def value(self, value):
        self._value = value

    @daemon.setter
    def daemon(self, daemon):
        self._daemon = daemon

    @property
    def type(self):
        return self._type

    def print(self, depth):
        if not self.is_system and self._value != None:
            print(" "*depth + self.name + ": " + str(self._value))

@dataclass
class Frame:
    id: str
    relay: str
    infra: str
    photo: str

    def __init__(self, parent=None, name=None, **slot_values):
        self._name_ = name
        self._slots_ = {}
        self._children_ = {}
        self._parent_ = parent


    def loadFrame(data, parent=None): 
        frame = Frame(parent, data['name'])
        for element in data['slots']:
            slot_name = element.pop('name')
            slot_type = element.pop('type')
            slot_value = element.pop('value')
            if('daemon' in element):
                slot_daemon = element.pop('daemon')
            else:
                slot_daemon = None
            if(slot_name in frame._slots_):
                if(parent._slots_[slot_name].type == Slot.OVERRIDE and slot_value):
                    frame._slots_[slot_name].value = slot_value
                    frame._slots_[slot_name].inheritance_type = slot_type
                    frame._slots_[slot_name].daemon = slot_daemon
            else:
                slot = Slot(slot_name, slot_value, slot_type, slot_daemon)
                frame._slots_[slot_name] = slot
						 
			
        if "children" in data:
            for element in data['children']:
                child = Frame.loadFrame(element, frame)
                frame._children_[child.name] = child
        return frame


    def daemon_IF_NEEDED():
        pass

    def daemon_IF_ADDED():
        pass

    def daemin_IF_REMOVED():
        pass

