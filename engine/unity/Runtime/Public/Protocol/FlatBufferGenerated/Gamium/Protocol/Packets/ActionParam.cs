// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace Gamium.Protocol.Packets
{

public enum ActionParam : byte
{
  NONE = 0,
  Actions_SleepParam = 1,
  Actions_InputKeyParam = 2,
  Actions_InputMouseParam = 3,
  Actions_InputSetTextParam = 4,
  Actions_MovePlayerParam = 5,
  Actions_AppQuitParam = 6,
};

public class ActionParamUnion {
  public ActionParam Type { get; set; }
  public object Value { get; set; }

  public ActionParamUnion() {
    this.Type = ActionParam.NONE;
    this.Value = null;
  }

  public T As<T>() where T : class { return this.Value as T; }
  public Gamium.Protocol.Packets.Actions.SleepParamT AsActions_SleepParam() { return this.As<Gamium.Protocol.Packets.Actions.SleepParamT>(); }
  public static ActionParamUnion FromActions_SleepParam(Gamium.Protocol.Packets.Actions.SleepParamT _actions_sleepparam) { return new ActionParamUnion{ Type = ActionParam.Actions_SleepParam, Value = _actions_sleepparam }; }
  public Gamium.Protocol.Packets.Actions.InputKeyParamT AsActions_InputKeyParam() { return this.As<Gamium.Protocol.Packets.Actions.InputKeyParamT>(); }
  public static ActionParamUnion FromActions_InputKeyParam(Gamium.Protocol.Packets.Actions.InputKeyParamT _actions_inputkeyparam) { return new ActionParamUnion{ Type = ActionParam.Actions_InputKeyParam, Value = _actions_inputkeyparam }; }
  public Gamium.Protocol.Packets.Actions.InputMouseParamT AsActions_InputMouseParam() { return this.As<Gamium.Protocol.Packets.Actions.InputMouseParamT>(); }
  public static ActionParamUnion FromActions_InputMouseParam(Gamium.Protocol.Packets.Actions.InputMouseParamT _actions_inputmouseparam) { return new ActionParamUnion{ Type = ActionParam.Actions_InputMouseParam, Value = _actions_inputmouseparam }; }
  public Gamium.Protocol.Packets.Actions.InputSetTextParamT AsActions_InputSetTextParam() { return this.As<Gamium.Protocol.Packets.Actions.InputSetTextParamT>(); }
  public static ActionParamUnion FromActions_InputSetTextParam(Gamium.Protocol.Packets.Actions.InputSetTextParamT _actions_inputsettextparam) { return new ActionParamUnion{ Type = ActionParam.Actions_InputSetTextParam, Value = _actions_inputsettextparam }; }
  public Gamium.Protocol.Packets.Actions.MovePlayerParamT AsActions_MovePlayerParam() { return this.As<Gamium.Protocol.Packets.Actions.MovePlayerParamT>(); }
  public static ActionParamUnion FromActions_MovePlayerParam(Gamium.Protocol.Packets.Actions.MovePlayerParamT _actions_moveplayerparam) { return new ActionParamUnion{ Type = ActionParam.Actions_MovePlayerParam, Value = _actions_moveplayerparam }; }
  public Gamium.Protocol.Packets.Actions.AppQuitParamT AsActions_AppQuitParam() { return this.As<Gamium.Protocol.Packets.Actions.AppQuitParamT>(); }
  public static ActionParamUnion FromActions_AppQuitParam(Gamium.Protocol.Packets.Actions.AppQuitParamT _actions_appquitparam) { return new ActionParamUnion{ Type = ActionParam.Actions_AppQuitParam, Value = _actions_appquitparam }; }

  public static int Pack(Google.FlatBuffers.FlatBufferBuilder builder, ActionParamUnion _o) {
    switch (_o.Type) {
      default: return 0;
      case ActionParam.Actions_SleepParam: return Gamium.Protocol.Packets.Actions.SleepParam.Pack(builder, _o.AsActions_SleepParam()).Value;
      case ActionParam.Actions_InputKeyParam: return Gamium.Protocol.Packets.Actions.InputKeyParam.Pack(builder, _o.AsActions_InputKeyParam()).Value;
      case ActionParam.Actions_InputMouseParam: return Gamium.Protocol.Packets.Actions.InputMouseParam.Pack(builder, _o.AsActions_InputMouseParam()).Value;
      case ActionParam.Actions_InputSetTextParam: return Gamium.Protocol.Packets.Actions.InputSetTextParam.Pack(builder, _o.AsActions_InputSetTextParam()).Value;
      case ActionParam.Actions_MovePlayerParam: return Gamium.Protocol.Packets.Actions.MovePlayerParam.Pack(builder, _o.AsActions_MovePlayerParam()).Value;
      case ActionParam.Actions_AppQuitParam: return Gamium.Protocol.Packets.Actions.AppQuitParam.Pack(builder, _o.AsActions_AppQuitParam()).Value;
    }
  }
}


}
