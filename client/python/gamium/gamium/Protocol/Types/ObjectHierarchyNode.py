# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObjectHierarchyNode(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObjectHierarchyNode()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsObjectHierarchyNode(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ObjectHierarchyNode
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ObjectHierarchyNode
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObjectHierarchyNode
    def Path(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObjectHierarchyNode
    def Children(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from gamium.Protocol.Types.ObjectHierarchyNode import ObjectHierarchyNode
            obj = ObjectHierarchyNode()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObjectHierarchyNode
    def ChildrenLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObjectHierarchyNode
    def ChildrenIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def ObjectHierarchyNodeStart(builder): builder.StartObject(3)
def Start(builder):
    return ObjectHierarchyNodeStart(builder)
def ObjectHierarchyNodeAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return ObjectHierarchyNodeAddName(builder, name)
def ObjectHierarchyNodeAddPath(builder, path): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def AddPath(builder, path):
    return ObjectHierarchyNodeAddPath(builder, path)
def ObjectHierarchyNodeAddChildren(builder, children): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(children), 0)
def AddChildren(builder, children):
    return ObjectHierarchyNodeAddChildren(builder, children)
def ObjectHierarchyNodeStartChildrenVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartChildrenVector(builder, numElems):
    return ObjectHierarchyNodeStartChildrenVector(builder, numElems)
def ObjectHierarchyNodeEnd(builder): return builder.EndObject()
def End(builder):
    return ObjectHierarchyNodeEnd(builder)
try:
    from typing import List
except:
    pass

class ObjectHierarchyNodeT(object):

    # ObjectHierarchyNodeT
    def __init__(self):
        self.name = None  # type: str
        self.path = None  # type: str
        self.children = None  # type: List[gamium.Protocol.Types.ObjectHierarchyNode.ObjectHierarchyNodeT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        objectHierarchyNode = ObjectHierarchyNode()
        objectHierarchyNode.Init(buf, pos)
        return cls.InitFromObj(objectHierarchyNode)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, objectHierarchyNode):
        x = ObjectHierarchyNodeT()
        x._UnPack(objectHierarchyNode)
        return x

    # ObjectHierarchyNodeT
    def _UnPack(self, objectHierarchyNode):
        if objectHierarchyNode is None:
            return
        self.name = objectHierarchyNode.Name()
        self.path = objectHierarchyNode.Path()
        if not objectHierarchyNode.ChildrenIsNone():
            self.children = []
            for i in range(objectHierarchyNode.ChildrenLength()):
                if objectHierarchyNode.Children(i) is None:
                    self.children.append(None)
                else:
                    objectHierarchyNode_ = gamium.Protocol.Types.ObjectHierarchyNode.ObjectHierarchyNodeT.InitFromObj(objectHierarchyNode.Children(i))
                    self.children.append(objectHierarchyNode_)

    # ObjectHierarchyNodeT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.path is not None:
            path = builder.CreateString(self.path)
        if self.children is not None:
            childrenlist = []
            for i in range(len(self.children)):
                childrenlist.append(self.children[i].Pack(builder))
            ObjectHierarchyNodeStartChildrenVector(builder, len(self.children))
            for i in reversed(range(len(self.children))):
                builder.PrependUOffsetTRelative(childrenlist[i])
            children = builder.EndVector()
        ObjectHierarchyNodeStart(builder)
        if self.name is not None:
            ObjectHierarchyNodeAddName(builder, name)
        if self.path is not None:
            ObjectHierarchyNodeAddPath(builder, path)
        if self.children is not None:
            ObjectHierarchyNodeAddChildren(builder, children)
        objectHierarchyNode = ObjectHierarchyNodeEnd(builder)
        return objectHierarchyNode
