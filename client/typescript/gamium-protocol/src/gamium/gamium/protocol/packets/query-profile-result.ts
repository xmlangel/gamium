// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from "flatbuffers";

export class QueryProfileResult
  implements flatbuffers.IUnpackableObject<QueryProfileResultT>
{
  bb: flatbuffers.ByteBuffer | null = null;
  bb_pos = 0;
  __init(i: number, bb: flatbuffers.ByteBuffer): QueryProfileResult {
    this.bb_pos = i;
    this.bb = bb;
    return this;
  }

  static getRootAsQueryProfileResult(
    bb: flatbuffers.ByteBuffer,
    obj?: QueryProfileResult
  ): QueryProfileResult {
    return (obj || new QueryProfileResult()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  static getSizePrefixedRootAsQueryProfileResult(
    bb: flatbuffers.ByteBuffer,
    obj?: QueryProfileResult
  ): QueryProfileResult {
    bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
    return (obj || new QueryProfileResult()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  fps(): number {
    const offset = this.bb!.__offset(this.bb_pos, 4);
    return offset ? this.bb!.readUint32(this.bb_pos + offset) : 0;
  }

  static startQueryProfileResult(builder: flatbuffers.Builder) {
    builder.startObject(1);
  }

  static addFps(builder: flatbuffers.Builder, fps: number) {
    builder.addFieldInt32(0, fps, 0);
  }

  static endQueryProfileResult(
    builder: flatbuffers.Builder
  ): flatbuffers.Offset {
    const offset = builder.endObject();
    return offset;
  }

  static createQueryProfileResult(
    builder: flatbuffers.Builder,
    fps: number
  ): flatbuffers.Offset {
    QueryProfileResult.startQueryProfileResult(builder);
    QueryProfileResult.addFps(builder, fps);
    return QueryProfileResult.endQueryProfileResult(builder);
  }

  unpack(): QueryProfileResultT {
    return new QueryProfileResultT(this.fps());
  }

  unpackTo(_o: QueryProfileResultT): void {
    _o.fps = this.fps();
  }
}

export class QueryProfileResultT implements flatbuffers.IGeneratedObject {
  constructor(public fps: number = 0) {}

  pack(builder: flatbuffers.Builder): flatbuffers.Offset {
    return QueryProfileResult.createQueryProfileResult(builder, this.fps);
  }
}
