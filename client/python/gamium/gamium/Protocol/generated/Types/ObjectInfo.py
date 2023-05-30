# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObjectInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObjectInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsObjectInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ObjectInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ObjectInfo
    def Path(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObjectInfo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObjectInfo
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # ObjectInfo
    def Tag(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ObjectInfo
    def TagLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObjectInfo
    def TagIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ObjectInfo
    def IsActive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ObjectInfo
    def ScreenPosition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = o + self._tab.Pos
            from gamium.protocol.generated.Types.Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObjectInfo
    def ScreenRectSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = o + self._tab.Pos
            from gamium.protocol.generated.Types.Vector2 import Vector2
            obj = Vector2()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObjectInfo
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = o + self._tab.Pos
            from gamium.protocol.generated.Types.Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObjectInfo
    def Rotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = o + self._tab.Pos
            from gamium.protocol.generated.Types.Vector4 import Vector4
            obj = Vector4()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObjectInfo
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ObjectInfoStart(builder): builder.StartObject(10)
def Start(builder):
    return ObjectInfoStart(builder)
def ObjectInfoAddPath(builder, path): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def AddPath(builder, path):
    return ObjectInfoAddPath(builder, path)
def ObjectInfoAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return ObjectInfoAddName(builder, name)
def ObjectInfoAddType(builder, type): builder.PrependInt16Slot(2, type, 0)
def AddType(builder, type):
    return ObjectInfoAddType(builder, type)
def ObjectInfoAddTag(builder, tag): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(tag), 0)
def AddTag(builder, tag):
    return ObjectInfoAddTag(builder, tag)
def ObjectInfoStartTagVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTagVector(builder, numElems):
    return ObjectInfoStartTagVector(builder, numElems)
def ObjectInfoAddIsActive(builder, isActive): builder.PrependBoolSlot(4, isActive, 0)
def AddIsActive(builder, isActive):
    return ObjectInfoAddIsActive(builder, isActive)
def ObjectInfoAddScreenPosition(builder, screenPosition): builder.PrependStructSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(screenPosition), 0)
def AddScreenPosition(builder, screenPosition):
    return ObjectInfoAddScreenPosition(builder, screenPosition)
def ObjectInfoAddScreenRectSize(builder, screenRectSize): builder.PrependStructSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(screenRectSize), 0)
def AddScreenRectSize(builder, screenRectSize):
    return ObjectInfoAddScreenRectSize(builder, screenRectSize)
def ObjectInfoAddPosition(builder, position): builder.PrependStructSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def AddPosition(builder, position):
    return ObjectInfoAddPosition(builder, position)
def ObjectInfoAddRotation(builder, rotation): builder.PrependStructSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def AddRotation(builder, rotation):
    return ObjectInfoAddRotation(builder, rotation)
def ObjectInfoAddText(builder, text): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def AddText(builder, text):
    return ObjectInfoAddText(builder, text)
def ObjectInfoEnd(builder): return builder.EndObject()
def End(builder):
    return ObjectInfoEnd(builder)
import gamium.protocol.generated.Types.Vector2
import gamium.protocol.generated.Types.Vector3
import gamium.protocol.generated.Types.Vector4
try:
    from typing import List, Optional
except:
    pass

class ObjectInfoT(object):

    # ObjectInfoT
    def __init__(self):
        self.path = None  # type: str
        self.name = None  # type: str
        self.type = 0  # type: int
        self.tag = None  # type: List[str]
        self.isActive = False  # type: bool
        self.screenPosition = None  # type: Optional[gamium.protocol.generated.Types.Vector3.Vector3T]
        self.screenRectSize = None  # type: Optional[gamium.protocol.generated.Types.Vector2.Vector2T]
        self.position = None  # type: Optional[gamium.protocol.generated.Types.Vector3.Vector3T]
        self.rotation = None  # type: Optional[gamium.protocol.generated.Types.Vector4.Vector4T]
        self.text = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        objectInfo = ObjectInfo()
        objectInfo.Init(buf, pos)
        return cls.InitFromObj(objectInfo)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, objectInfo):
        x = ObjectInfoT()
        x._UnPack(objectInfo)
        return x

    # ObjectInfoT
    def _UnPack(self, objectInfo):
        if objectInfo is None:
            return
        self.path = objectInfo.Path()
        self.name = objectInfo.Name()
        self.type = objectInfo.Type()
        if not objectInfo.TagIsNone():
            self.tag = []
            for i in range(objectInfo.TagLength()):
                self.tag.append(objectInfo.Tag(i))
        self.isActive = objectInfo.IsActive()
        if objectInfo.ScreenPosition() is not None:
            self.screenPosition = gamium.protocol.generated.Types.Vector3.Vector3T.InitFromObj(objectInfo.ScreenPosition())
        if objectInfo.ScreenRectSize() is not None:
            self.screenRectSize = gamium.protocol.generated.Types.Vector2.Vector2T.InitFromObj(objectInfo.ScreenRectSize())
        if objectInfo.Position() is not None:
            self.position = gamium.protocol.generated.Types.Vector3.Vector3T.InitFromObj(objectInfo.Position())
        if objectInfo.Rotation() is not None:
            self.rotation = gamium.protocol.generated.Types.Vector4.Vector4T.InitFromObj(objectInfo.Rotation())
        self.text = objectInfo.Text()

    # ObjectInfoT
    def Pack(self, builder):
        if self.path is not None:
            path = builder.CreateString(self.path)
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.tag is not None:
            taglist = []
            for i in range(len(self.tag)):
                taglist.append(builder.CreateString(self.tag[i]))
            ObjectInfoStartTagVector(builder, len(self.tag))
            for i in reversed(range(len(self.tag))):
                builder.PrependUOffsetTRelative(taglist[i])
            tag = builder.EndVector()
        if self.text is not None:
            text = builder.CreateString(self.text)
        ObjectInfoStart(builder)
        if self.path is not None:
            ObjectInfoAddPath(builder, path)
        if self.name is not None:
            ObjectInfoAddName(builder, name)
        ObjectInfoAddType(builder, self.type)
        if self.tag is not None:
            ObjectInfoAddTag(builder, tag)
        ObjectInfoAddIsActive(builder, self.isActive)
        if self.screenPosition is not None:
            screenPosition = self.screenPosition.Pack(builder)
            ObjectInfoAddScreenPosition(builder, screenPosition)
        if self.screenRectSize is not None:
            screenRectSize = self.screenRectSize.Pack(builder)
            ObjectInfoAddScreenRectSize(builder, screenRectSize)
        if self.position is not None:
            position = self.position.Pack(builder)
            ObjectInfoAddPosition(builder, position)
        if self.rotation is not None:
            rotation = self.rotation.Pack(builder)
            ObjectInfoAddRotation(builder, rotation)
        if self.text is not None:
            ObjectInfoAddText(builder, text)
        objectInfo = ObjectInfoEnd(builder)
        return objectInfo
