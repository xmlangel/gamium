// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from "flatbuffers";

import { InputKeyPressType } from "../../../../gamium/protocol/types/input-key-press-type.js";

export class InputKeyParam
  implements flatbuffers.IUnpackableObject<InputKeyParamT>
{
  bb: flatbuffers.ByteBuffer | null = null;
  bb_pos = 0;
  __init(i: number, bb: flatbuffers.ByteBuffer): InputKeyParam {
    this.bb_pos = i;
    this.bb = bb;
    return this;
  }

  static getRootAsInputKeyParam(
    bb: flatbuffers.ByteBuffer,
    obj?: InputKeyParam
  ): InputKeyParam {
    return (obj || new InputKeyParam()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  static getSizePrefixedRootAsInputKeyParam(
    bb: flatbuffers.ByteBuffer,
    obj?: InputKeyParam
  ): InputKeyParam {
    bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
    return (obj || new InputKeyParam()).__init(
      bb.readInt32(bb.position()) + bb.position(),
      bb
    );
  }

  press(): InputKeyPressType {
    const offset = this.bb!.__offset(this.bb_pos, 4);
    return offset
      ? this.bb!.readInt16(this.bb_pos + offset)
      : InputKeyPressType.DOWN;
  }

  codes(index: number): string;
  codes(
    index: number,
    optionalEncoding: flatbuffers.Encoding
  ): string | Uint8Array;
  codes(index: number, optionalEncoding?: any): string | Uint8Array | null {
    const offset = this.bb!.__offset(this.bb_pos, 6);
    return offset
      ? this.bb!.__string(
          this.bb!.__vector(this.bb_pos + offset) + index * 4,
          optionalEncoding
        )
      : null;
  }

  codesLength(): number {
    const offset = this.bb!.__offset(this.bb_pos, 6);
    return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
  }

  static startInputKeyParam(builder: flatbuffers.Builder) {
    builder.startObject(2);
  }

  static addPress(builder: flatbuffers.Builder, press: InputKeyPressType) {
    builder.addFieldInt16(0, press, InputKeyPressType.DOWN);
  }

  static addCodes(
    builder: flatbuffers.Builder,
    codesOffset: flatbuffers.Offset
  ) {
    builder.addFieldOffset(1, codesOffset, 0);
  }

  static createCodesVector(
    builder: flatbuffers.Builder,
    data: flatbuffers.Offset[]
  ): flatbuffers.Offset {
    builder.startVector(4, data.length, 4);
    for (let i = data.length - 1; i >= 0; i--) {
      builder.addOffset(data[i]!);
    }
    return builder.endVector();
  }

  static startCodesVector(builder: flatbuffers.Builder, numElems: number) {
    builder.startVector(4, numElems, 4);
  }

  static endInputKeyParam(builder: flatbuffers.Builder): flatbuffers.Offset {
    const offset = builder.endObject();
    return offset;
  }

  static createInputKeyParam(
    builder: flatbuffers.Builder,
    press: InputKeyPressType,
    codesOffset: flatbuffers.Offset
  ): flatbuffers.Offset {
    InputKeyParam.startInputKeyParam(builder);
    InputKeyParam.addPress(builder, press);
    InputKeyParam.addCodes(builder, codesOffset);
    return InputKeyParam.endInputKeyParam(builder);
  }

  unpack(): InputKeyParamT {
    return new InputKeyParamT(
      this.press(),
      this.bb!.createScalarList<string>(
        this.codes.bind(this),
        this.codesLength()
      )
    );
  }

  unpackTo(_o: InputKeyParamT): void {
    _o.press = this.press();
    _o.codes = this.bb!.createScalarList<string>(
      this.codes.bind(this),
      this.codesLength()
    );
  }
}

export class InputKeyParamT implements flatbuffers.IGeneratedObject {
  constructor(
    public press: InputKeyPressType = InputKeyPressType.DOWN,
    public codes: string[] = []
  ) {}

  pack(builder: flatbuffers.Builder): flatbuffers.Offset {
    const codes = InputKeyParam.createCodesVector(
      builder,
      builder.createObjectOffsetList(this.codes)
    );

    return InputKeyParam.createInputKeyParam(builder, this.press, codes);
  }
}
