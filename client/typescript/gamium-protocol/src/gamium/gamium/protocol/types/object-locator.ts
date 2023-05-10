// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from "flatbuffers";

import { ObjectLocatorBy } from "../../../gamium/protocol/types/object-locator-by.js";

export class ObjectLocator
  implements flatbuffers.IUnpackableObject<ObjectLocatorT>
{
  bb: flatbuffers.ByteBuffer | null = null;
  bb_pos = 0;
  __init(i: number, bb: flatbuffers.ByteBuffer): ObjectLocator {
    this.bb_pos = i;
    this.bb = bb;
    return this;
  }

  static getRootAsObjectLocator(
    bb: flatbuffers.ByteBuffer,
    obj?: ObjectLocator
  ): ObjectLocator {
    return (obj || new ObjectLocator()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  static getSizePrefixedRootAsObjectLocator(
    bb: flatbuffers.ByteBuffer,
    obj?: ObjectLocator
  ): ObjectLocator {
    bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
    return (obj || new ObjectLocator()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  by(): ObjectLocatorBy {
    const offset = this.bb!.__offset(this.bb_pos, 4);
    return offset
      ? this.bb!.readInt16(this.bb_pos + offset)
      : ObjectLocatorBy.Path;
  }

  str(): string | null;
  str(optionalEncoding: flatbuffers.Encoding): string | Uint8Array | null;
  str(optionalEncoding?: any): string | Uint8Array | null {
    const offset = this.bb!.__offset(this.bb_pos, 6);
    return offset
      ? this.bb!.__string(this.bb_pos + offset, optionalEncoding)
      : null;
  }

  static startObjectLocator(builder: flatbuffers.Builder) {
    builder.startObject(2);
  }

  static addBy(builder: flatbuffers.Builder, by: ObjectLocatorBy) {
    builder.addFieldInt16(0, by, ObjectLocatorBy.Path);
  }

  static addStr(builder: flatbuffers.Builder, strOffset: flatbuffers.Offset) {
    builder.addFieldOffset(1, strOffset, 0);
  }

  static endObjectLocator(builder: flatbuffers.Builder): flatbuffers.Offset {
    const offset = builder.endObject();
    return offset;
  }

  static createObjectLocator(
    builder: flatbuffers.Builder,
    by: ObjectLocatorBy,
    strOffset: flatbuffers.Offset
  ): flatbuffers.Offset {
    ObjectLocator.startObjectLocator(builder);
    ObjectLocator.addBy(builder, by);
    ObjectLocator.addStr(builder, strOffset);
    return ObjectLocator.endObjectLocator(builder);
  }

  unpack(): ObjectLocatorT {
    return new ObjectLocatorT(this.by(), this.str());
  }

  unpackTo(_o: ObjectLocatorT): void {
    _o.by = this.by();
    _o.str = this.str();
  }
}

export class ObjectLocatorT implements flatbuffers.IGeneratedObject {
  constructor(
    public by: ObjectLocatorBy = ObjectLocatorBy.Path,
    public str: string | Uint8Array | null = null
  ) {}

  pack(builder: flatbuffers.Builder): flatbuffers.Offset {
    const str = this.str !== null ? builder.createString(this.str!) : 0;

    return ObjectLocator.createObjectLocator(builder, this.by, str);
  }
}
