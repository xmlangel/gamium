# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Packets

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GetPageSourceResult(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GetPageSourceResult()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGetPageSourceResult(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GetPageSourceResult
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GetPageSourceResult
    def PageSource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def GetPageSourceResultStart(builder): builder.StartObject(1)
def Start(builder):
    return GetPageSourceResultStart(builder)
def GetPageSourceResultAddPageSource(builder, pageSource): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pageSource), 0)
def AddPageSource(builder, pageSource):
    return GetPageSourceResultAddPageSource(builder, pageSource)
def GetPageSourceResultEnd(builder): return builder.EndObject()
def End(builder):
    return GetPageSourceResultEnd(builder)

class GetPageSourceResultT(object):

    # GetPageSourceResultT
    def __init__(self):
        self.pageSource = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        getPageSourceResult = GetPageSourceResult()
        getPageSourceResult.Init(buf, pos)
        return cls.InitFromObj(getPageSourceResult)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, getPageSourceResult):
        x = GetPageSourceResultT()
        x._UnPack(getPageSourceResult)
        return x

    # GetPageSourceResultT
    def _UnPack(self, getPageSourceResult):
        if getPageSourceResult is None:
            return
        self.pageSource = getPageSourceResult.PageSource()

    # GetPageSourceResultT
    def Pack(self, builder):
        if self.pageSource is not None:
            pageSource = builder.CreateString(self.pageSource)
        GetPageSourceResultStart(builder)
        if self.pageSource is not None:
            GetPageSourceResultAddPageSource(builder, pageSource)
        getPageSourceResult = GetPageSourceResultEnd(builder)
        return getPageSourceResult
