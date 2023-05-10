// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace Gamium.Protocol.Packets
{

using global::System;
using global::System.Collections.Generic;
using global::Google.FlatBuffers;

public struct QueryScreenParam : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_22_10_26(); }
  public static QueryScreenParam GetRootAsQueryScreenParam(ByteBuffer _bb) { return GetRootAsQueryScreenParam(_bb, new QueryScreenParam()); }
  public static QueryScreenParam GetRootAsQueryScreenParam(ByteBuffer _bb, QueryScreenParam obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public QueryScreenParam __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }


  public static void StartQueryScreenParam(FlatBufferBuilder builder) { builder.StartTable(0); }
  public static Offset<Gamium.Protocol.Packets.QueryScreenParam> EndQueryScreenParam(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<Gamium.Protocol.Packets.QueryScreenParam>(o);
  }
  public QueryScreenParamT UnPack() {
    var _o = new QueryScreenParamT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(QueryScreenParamT _o) {
  }
  public static Offset<Gamium.Protocol.Packets.QueryScreenParam> Pack(FlatBufferBuilder builder, QueryScreenParamT _o) {
    if (_o == null) return default(Offset<Gamium.Protocol.Packets.QueryScreenParam>);
    StartQueryScreenParam(builder);
    return EndQueryScreenParam(builder);
  }
}

public class QueryScreenParamT
{

  public QueryScreenParamT() {
  }
}


}
