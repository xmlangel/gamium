// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_CONFIGPACKET_GAMIUM_PROTOCOL_PACKETS_H_
#define FLATBUFFERS_GENERATED_CONFIGPACKET_GAMIUM_PROTOCOL_PACKETS_H_

#include "flatbuffers/flatbuffers.h"

// Ensure the included flatbuffers.h is the same version as when this file was
// generated, otherwise it may not be compatible.
static_assert(FLATBUFFERS_VERSION_MAJOR == 22 &&
              FLATBUFFERS_VERSION_MINOR == 10 &&
              FLATBUFFERS_VERSION_REVISION == 26,
             "Non-compatible flatbuffers version included");

#include "config_generated.h"

namespace Gamium {
namespace Protocol {
namespace Packets {

struct ChangeConfigurationParam;
struct ChangeConfigurationParamBuilder;
struct ChangeConfigurationParamT;

struct ChangeConfigurationResult;
struct ChangeConfigurationResultBuilder;
struct ChangeConfigurationResultT;

inline const flatbuffers::TypeTable *ChangeConfigurationParamTypeTable();

inline const flatbuffers::TypeTable *ChangeConfigurationResultTypeTable();

struct ChangeConfigurationParamT : public flatbuffers::NativeTable {
  typedef ChangeConfigurationParam TableType;
  std::unique_ptr<Gamium::Protocol::Types::ConfigurationT> config{};
  ChangeConfigurationParamT() = default;
  ChangeConfigurationParamT(const ChangeConfigurationParamT &o);
  ChangeConfigurationParamT(ChangeConfigurationParamT&&) FLATBUFFERS_NOEXCEPT = default;
  ChangeConfigurationParamT &operator=(ChangeConfigurationParamT o) FLATBUFFERS_NOEXCEPT;
};

struct ChangeConfigurationParam FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef ChangeConfigurationParamT NativeTableType;
  typedef ChangeConfigurationParamBuilder Builder;
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return ChangeConfigurationParamTypeTable();
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_CONFIG = 4
  };
  const Gamium::Protocol::Types::Configuration *config() const {
    return GetPointer<const Gamium::Protocol::Types::Configuration *>(VT_CONFIG);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_CONFIG) &&
           verifier.VerifyTable(config()) &&
           verifier.EndTable();
  }
  ChangeConfigurationParamT *UnPack(const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(ChangeConfigurationParamT *_o, const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static flatbuffers::Offset<ChangeConfigurationParam> Pack(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationParamT* _o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct ChangeConfigurationParamBuilder {
  typedef ChangeConfigurationParam Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_config(flatbuffers::Offset<Gamium::Protocol::Types::Configuration> config) {
    fbb_.AddOffset(ChangeConfigurationParam::VT_CONFIG, config);
  }
  explicit ChangeConfigurationParamBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<ChangeConfigurationParam> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<ChangeConfigurationParam>(end);
    return o;
  }
};

inline flatbuffers::Offset<ChangeConfigurationParam> CreateChangeConfigurationParam(
    flatbuffers::FlatBufferBuilder &_fbb,
    flatbuffers::Offset<Gamium::Protocol::Types::Configuration> config = 0) {
  ChangeConfigurationParamBuilder builder_(_fbb);
  builder_.add_config(config);
  return builder_.Finish();
}

flatbuffers::Offset<ChangeConfigurationParam> CreateChangeConfigurationParam(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationParamT *_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);

struct ChangeConfigurationResultT : public flatbuffers::NativeTable {
  typedef ChangeConfigurationResult TableType;
};

struct ChangeConfigurationResult FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef ChangeConfigurationResultT NativeTableType;
  typedef ChangeConfigurationResultBuilder Builder;
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return ChangeConfigurationResultTypeTable();
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           verifier.EndTable();
  }
  ChangeConfigurationResultT *UnPack(const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(ChangeConfigurationResultT *_o, const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static flatbuffers::Offset<ChangeConfigurationResult> Pack(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationResultT* _o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct ChangeConfigurationResultBuilder {
  typedef ChangeConfigurationResult Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  explicit ChangeConfigurationResultBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<ChangeConfigurationResult> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<ChangeConfigurationResult>(end);
    return o;
  }
};

inline flatbuffers::Offset<ChangeConfigurationResult> CreateChangeConfigurationResult(
    flatbuffers::FlatBufferBuilder &_fbb) {
  ChangeConfigurationResultBuilder builder_(_fbb);
  return builder_.Finish();
}

flatbuffers::Offset<ChangeConfigurationResult> CreateChangeConfigurationResult(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationResultT *_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);

inline ChangeConfigurationParamT::ChangeConfigurationParamT(const ChangeConfigurationParamT &o)
      : config((o.config) ? new Gamium::Protocol::Types::ConfigurationT(*o.config) : nullptr) {
}

inline ChangeConfigurationParamT &ChangeConfigurationParamT::operator=(ChangeConfigurationParamT o) FLATBUFFERS_NOEXCEPT {
  std::swap(config, o.config);
  return *this;
}

inline ChangeConfigurationParamT *ChangeConfigurationParam::UnPack(const flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<ChangeConfigurationParamT>(new ChangeConfigurationParamT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void ChangeConfigurationParam::UnPackTo(ChangeConfigurationParamT *_o, const flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = config(); if (_e) { if(_o->config) { _e->UnPackTo(_o->config.get(), _resolver); } else { _o->config = std::unique_ptr<Gamium::Protocol::Types::ConfigurationT>(_e->UnPack(_resolver)); } } else if (_o->config) { _o->config.reset(); } }
}

inline flatbuffers::Offset<ChangeConfigurationParam> ChangeConfigurationParam::Pack(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationParamT* _o, const flatbuffers::rehasher_function_t *_rehasher) {
  return CreateChangeConfigurationParam(_fbb, _o, _rehasher);
}

inline flatbuffers::Offset<ChangeConfigurationParam> CreateChangeConfigurationParam(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationParamT *_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const ChangeConfigurationParamT* __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _config = _o->config ? CreateConfiguration(_fbb, _o->config.get(), _rehasher) : 0;
  return Gamium::Protocol::Packets::CreateChangeConfigurationParam(
      _fbb,
      _config);
}

inline ChangeConfigurationResultT *ChangeConfigurationResult::UnPack(const flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<ChangeConfigurationResultT>(new ChangeConfigurationResultT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void ChangeConfigurationResult::UnPackTo(ChangeConfigurationResultT *_o, const flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
}

inline flatbuffers::Offset<ChangeConfigurationResult> ChangeConfigurationResult::Pack(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationResultT* _o, const flatbuffers::rehasher_function_t *_rehasher) {
  return CreateChangeConfigurationResult(_fbb, _o, _rehasher);
}

inline flatbuffers::Offset<ChangeConfigurationResult> CreateChangeConfigurationResult(flatbuffers::FlatBufferBuilder &_fbb, const ChangeConfigurationResultT *_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const ChangeConfigurationResultT* __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  return Gamium::Protocol::Packets::CreateChangeConfigurationResult(
      _fbb);
}

inline const flatbuffers::TypeTable *ChangeConfigurationParamTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SEQUENCE, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    Gamium::Protocol::Types::ConfigurationTypeTable
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 1, type_codes, type_refs, nullptr, nullptr, nullptr
  };
  return &tt;
}

inline const flatbuffers::TypeTable *ChangeConfigurationResultTypeTable() {
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 0, nullptr, nullptr, nullptr, nullptr, nullptr
  };
  return &tt;
}

}  // namespace Packets
}  // namespace Protocol
}  // namespace Gamium

#endif  // FLATBUFFERS_GENERATED_CONFIGPACKET_GAMIUM_PROTOCOL_PACKETS_H_
