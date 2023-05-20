# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Protocol

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Response(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Response()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsResponse(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Response
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Response
    def Seq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Response
    def Error(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from gamium.Protocol.Types.ErrorResult import ErrorResult
            obj = ErrorResult()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Response
    def ResultType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Response
    def Result(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def ResponseStart(builder): builder.StartObject(4)
def Start(builder):
    return ResponseStart(builder)
def ResponseAddSeq(builder, seq): builder.PrependUint32Slot(0, seq, 0)
def AddSeq(builder, seq):
    return ResponseAddSeq(builder, seq)
def ResponseAddError(builder, error): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(error), 0)
def AddError(builder, error):
    return ResponseAddError(builder, error)
def ResponseAddResultType(builder, resultType): builder.PrependUint8Slot(2, resultType, 0)
def AddResultType(builder, resultType):
    return ResponseAddResultType(builder, resultType)
def ResponseAddResult(builder, result): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(result), 0)
def AddResult(builder, result):
    return ResponseAddResult(builder, result)
def ResponseEnd(builder): return builder.EndObject()
def End(builder):
    return ResponseEnd(builder)
import gamium.Protocol.Packets.ActionsResult
import gamium.Protocol.Packets.ChangeConfigurationResult
import gamium.Protocol.Packets.DumpObjectsHierarchyResult
import gamium.Protocol.Packets.ExecuteRpcResult
import gamium.Protocol.Packets.FindObjectsResult
import gamium.Protocol.Packets.HelloResult
import gamium.Protocol.Packets.InspectObjectOnScreenResult
import gamium.Protocol.Packets.InspectObjectWithIdResult
import gamium.Protocol.Packets.QueryObjectInteractableResult
import gamium.Protocol.Packets.QueryProfileResult
import gamium.Protocol.Packets.QueryScreenResult
import gamium.Protocol.Result
import gamium.Protocol.Types.ErrorResult
try:
    from typing import Optional, Union
except:
    pass

class ResponseT(object):

    # ResponseT
    def __init__(self):
        self.seq = 0  # type: int
        self.error = None  # type: Optional[gamium.Protocol.Types.ErrorResult.ErrorResultT]
        self.resultType = 0  # type: int
        self.result = None  # type: Union[None, gamium.Protocol.Packets.HelloResult.HelloResultT, gamium.Protocol.Packets.QueryScreenResult.QueryScreenResultT, gamium.Protocol.Packets.FindObjectsResult.FindObjectsResultT, gamium.Protocol.Packets.QueryObjectInteractableResult.QueryObjectInteractableResultT, gamium.Protocol.Packets.ActionsResult.ActionsResultT, gamium.Protocol.Packets.ExecuteRpcResult.ExecuteRpcResultT, gamium.Protocol.Packets.InspectObjectOnScreenResult.InspectObjectOnScreenResultT, gamium.Protocol.Packets.InspectObjectWithIdResult.InspectObjectWithIdResultT, gamium.Protocol.Packets.DumpObjectsHierarchyResult.DumpObjectsHierarchyResultT, gamium.Protocol.Packets.ChangeConfigurationResult.ChangeConfigurationResultT, gamium.Protocol.Packets.QueryProfileResult.QueryProfileResultT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        response = Response()
        response.Init(buf, pos)
        return cls.InitFromObj(response)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, response):
        x = ResponseT()
        x._UnPack(response)
        return x

    # ResponseT
    def _UnPack(self, response):
        if response is None:
            return
        self.seq = response.Seq()
        if response.Error() is not None:
            self.error = gamium.Protocol.Types.ErrorResult.ErrorResultT.InitFromObj(response.Error())
        self.resultType = response.ResultType()
        self.result = gamium.Protocol.Result.ResultCreator(self.resultType, response.Result())

    # ResponseT
    def Pack(self, builder):
        if self.error is not None:
            error = self.error.Pack(builder)
        if self.result is not None:
            result = self.result.Pack(builder)
        ResponseStart(builder)
        ResponseAddSeq(builder, self.seq)
        if self.error is not None:
            ResponseAddError(builder, error)
        ResponseAddResultType(builder, self.resultType)
        if self.result is not None:
            ResponseAddResult(builder, result)
        response = ResponseEnd(builder)
        return response
