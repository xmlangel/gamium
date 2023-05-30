# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Packets

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InspectObjectWithIdResult(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InspectObjectWithIdResult()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsInspectObjectWithIdResult(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # InspectObjectWithIdResult
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InspectObjectWithIdResult
    def Info(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from gamium.protocol.generated.Types.ObjectInfo import ObjectInfo
            obj = ObjectInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def InspectObjectWithIdResultStart(builder): builder.StartObject(1)
def Start(builder):
    return InspectObjectWithIdResultStart(builder)
def InspectObjectWithIdResultAddInfo(builder, info): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(info), 0)
def AddInfo(builder, info):
    return InspectObjectWithIdResultAddInfo(builder, info)
def InspectObjectWithIdResultEnd(builder): return builder.EndObject()
def End(builder):
    return InspectObjectWithIdResultEnd(builder)
import gamium.protocol.generated.Types.ObjectInfo
try:
    from typing import Optional
except:
    pass

class InspectObjectWithIdResultT(object):

    # InspectObjectWithIdResultT
    def __init__(self):
        self.info = None  # type: Optional[gamium.protocol.generated.Types.ObjectInfo.ObjectInfoT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        inspectObjectWithIdResult = InspectObjectWithIdResult()
        inspectObjectWithIdResult.Init(buf, pos)
        return cls.InitFromObj(inspectObjectWithIdResult)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, inspectObjectWithIdResult):
        x = InspectObjectWithIdResultT()
        x._UnPack(inspectObjectWithIdResult)
        return x

    # InspectObjectWithIdResultT
    def _UnPack(self, inspectObjectWithIdResult):
        if inspectObjectWithIdResult is None:
            return
        if inspectObjectWithIdResult.Info() is not None:
            self.info = gamium.protocol.generated.Types.ObjectInfo.ObjectInfoT.InitFromObj(inspectObjectWithIdResult.Info())

    # InspectObjectWithIdResultT
    def Pack(self, builder):
        if self.info is not None:
            info = self.info.Pack(builder)
        InspectObjectWithIdResultStart(builder)
        if self.info is not None:
            InspectObjectWithIdResultAddInfo(builder, info)
        inspectObjectWithIdResult = InspectObjectWithIdResultEnd(builder)
        return inspectObjectWithIdResult
