// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

export class GetPageSourceParam implements flatbuffers.IUnpackableObject<GetPageSourceParamT> {
  bb: flatbuffers.ByteBuffer | null = null;
  bb_pos = 0;
  __init(i: number, bb: flatbuffers.ByteBuffer): GetPageSourceParam {
    this.bb_pos = i;
    this.bb = bb;
    return this;
  }

  static getRootAsGetPageSourceParam(bb: flatbuffers.ByteBuffer, obj?: GetPageSourceParam): GetPageSourceParam {
    return (obj || new GetPageSourceParam()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
  }

  static getSizePrefixedRootAsGetPageSourceParam(bb: flatbuffers.ByteBuffer, obj?: GetPageSourceParam): GetPageSourceParam {
    bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
    return (obj || new GetPageSourceParam()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
  }

  static startGetPageSourceParam(builder: flatbuffers.Builder) {
    builder.startObject(0);
  }

  static endGetPageSourceParam(builder: flatbuffers.Builder): flatbuffers.Offset {
    const offset = builder.endObject();
    return offset;
  }

  static createGetPageSourceParam(builder: flatbuffers.Builder): flatbuffers.Offset {
    GetPageSourceParam.startGetPageSourceParam(builder);
    return GetPageSourceParam.endGetPageSourceParam(builder);
  }

  unpack(): GetPageSourceParamT {
    return new GetPageSourceParamT();
  }

  unpackTo(_o: GetPageSourceParamT): void {}
}

export class GetPageSourceParamT implements flatbuffers.IGeneratedObject {
  constructor() {}

  pack(builder: flatbuffers.Builder): flatbuffers.Offset {
    return GetPageSourceParam.createGetPageSourceParam(builder);
  }
}
