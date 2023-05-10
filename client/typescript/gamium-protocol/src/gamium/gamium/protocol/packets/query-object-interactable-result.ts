// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from "flatbuffers";

export class QueryObjectInteractableResult
  implements flatbuffers.IUnpackableObject<QueryObjectInteractableResultT>
{
  bb: flatbuffers.ByteBuffer | null = null;
  bb_pos = 0;
  __init(i: number, bb: flatbuffers.ByteBuffer): QueryObjectInteractableResult {
    this.bb_pos = i;
    this.bb = bb;
    return this;
  }

  static getRootAsQueryObjectInteractableResult(
    bb: flatbuffers.ByteBuffer,
    obj?: QueryObjectInteractableResult
  ): QueryObjectInteractableResult {
    return (obj || new QueryObjectInteractableResult()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  static getSizePrefixedRootAsQueryObjectInteractableResult(
    bb: flatbuffers.ByteBuffer,
    obj?: QueryObjectInteractableResult
  ): QueryObjectInteractableResult {
    bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
    return (obj || new QueryObjectInteractableResult()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  isInteractable(): boolean {
    const offset = this.bb!.__offset(this.bb_pos, 4);
    return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
  }

  static startQueryObjectInteractableResult(builder: flatbuffers.Builder) {
    builder.startObject(1);
  }

  static addIsInteractable(
    builder: flatbuffers.Builder,
    isInteractable: boolean
  ) {
    builder.addFieldInt8(0, +isInteractable, +false);
  }

  static endQueryObjectInteractableResult(
    builder: flatbuffers.Builder
  ): flatbuffers.Offset {
    const offset = builder.endObject();
    return offset;
  }

  static createQueryObjectInteractableResult(
    builder: flatbuffers.Builder,
    isInteractable: boolean
  ): flatbuffers.Offset {
    QueryObjectInteractableResult.startQueryObjectInteractableResult(builder);
    QueryObjectInteractableResult.addIsInteractable(builder, isInteractable);
    return QueryObjectInteractableResult.endQueryObjectInteractableResult(
      builder
    );
  }

  unpack(): QueryObjectInteractableResultT {
    return new QueryObjectInteractableResultT(this.isInteractable());
  }

  unpackTo(_o: QueryObjectInteractableResultT): void {
    _o.isInteractable = this.isInteractable();
  }
}

export class QueryObjectInteractableResultT
  implements flatbuffers.IGeneratedObject
{
  constructor(public isInteractable: boolean = false) {}

  pack(builder: flatbuffers.Builder): flatbuffers.Offset {
    return QueryObjectInteractableResult.createQueryObjectInteractableResult(
      builder,
      this.isInteractable
    );
  }
}
