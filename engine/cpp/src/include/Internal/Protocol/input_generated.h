// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_INPUT_GAMIUM_PROTOCOL_TYPES_H_
#define FLATBUFFERS_GENERATED_INPUT_GAMIUM_PROTOCOL_TYPES_H_

#include "flatbuffers/flatbuffers.h"

// Ensure the included flatbuffers.h is the same version as when this file was
// generated, otherwise it may not be compatible.
static_assert(FLATBUFFERS_VERSION_MAJOR == 22 &&
              FLATBUFFERS_VERSION_MINOR == 10 &&
              FLATBUFFERS_VERSION_REVISION == 26,
             "Non-compatible flatbuffers version included");

namespace Gamium {
namespace Protocol {
namespace Types {

enum class InputKeyPressType : int16_t {
  DOWN = 0,
  UP = 1,
  MIN = DOWN,
  MAX = UP
};

inline const InputKeyPressType (&EnumValuesInputKeyPressType())[2] {
  static const InputKeyPressType values[] = {
    InputKeyPressType::DOWN,
    InputKeyPressType::UP
  };
  return values;
}

inline const char * const *EnumNamesInputKeyPressType() {
  static const char * const names[3] = {
    "DOWN",
    "UP",
    nullptr
  };
  return names;
}

inline const char *EnumNameInputKeyPressType(InputKeyPressType e) {
  if (flatbuffers::IsOutRange(e, InputKeyPressType::DOWN, InputKeyPressType::UP)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesInputKeyPressType()[index];
}

enum class InputKeyBy : int16_t {
  UNITY_KEYCODE = 0,
  UNITY_KEYBOARD = 1,
  MIN = UNITY_KEYCODE,
  MAX = UNITY_KEYBOARD
};

inline const InputKeyBy (&EnumValuesInputKeyBy())[2] {
  static const InputKeyBy values[] = {
    InputKeyBy::UNITY_KEYCODE,
    InputKeyBy::UNITY_KEYBOARD
  };
  return values;
}

inline const char * const *EnumNamesInputKeyBy() {
  static const char * const names[3] = {
    "UNITY_KEYCODE",
    "UNITY_KEYBOARD",
    nullptr
  };
  return names;
}

inline const char *EnumNameInputKeyBy(InputKeyBy e) {
  if (flatbuffers::IsOutRange(e, InputKeyBy::UNITY_KEYCODE, InputKeyBy::UNITY_KEYBOARD)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesInputKeyBy()[index];
}

enum class InputMousePressType : int16_t {
  DOWN = 0,
  UP = 1,
  MOVE = 2,
  SCROLL = 3,
  MIN = DOWN,
  MAX = SCROLL
};

inline const InputMousePressType (&EnumValuesInputMousePressType())[4] {
  static const InputMousePressType values[] = {
    InputMousePressType::DOWN,
    InputMousePressType::UP,
    InputMousePressType::MOVE,
    InputMousePressType::SCROLL
  };
  return values;
}

inline const char * const *EnumNamesInputMousePressType() {
  static const char * const names[5] = {
    "DOWN",
    "UP",
    "MOVE",
    "SCROLL",
    nullptr
  };
  return names;
}

inline const char *EnumNameInputMousePressType(InputMousePressType e) {
  if (flatbuffers::IsOutRange(e, InputMousePressType::DOWN, InputMousePressType::SCROLL)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesInputMousePressType()[index];
}

enum class InputMouseButtonCode : int16_t {
  LEFT = 0,
  MIDDLE = 1,
  RIGHT = 2,
  MIN = LEFT,
  MAX = RIGHT
};

inline const InputMouseButtonCode (&EnumValuesInputMouseButtonCode())[3] {
  static const InputMouseButtonCode values[] = {
    InputMouseButtonCode::LEFT,
    InputMouseButtonCode::MIDDLE,
    InputMouseButtonCode::RIGHT
  };
  return values;
}

inline const char * const *EnumNamesInputMouseButtonCode() {
  static const char * const names[4] = {
    "LEFT",
    "MIDDLE",
    "RIGHT",
    nullptr
  };
  return names;
}

inline const char *EnumNameInputMouseButtonCode(InputMouseButtonCode e) {
  if (flatbuffers::IsOutRange(e, InputMouseButtonCode::LEFT, InputMouseButtonCode::RIGHT)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesInputMouseButtonCode()[index];
}

inline const flatbuffers::TypeTable *InputKeyPressTypeTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    Gamium::Protocol::Types::InputKeyPressTypeTypeTable
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 2, type_codes, type_refs, nullptr, nullptr, nullptr
  };
  return &tt;
}

inline const flatbuffers::TypeTable *InputKeyByTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    Gamium::Protocol::Types::InputKeyByTypeTable
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 2, type_codes, type_refs, nullptr, nullptr, nullptr
  };
  return &tt;
}

inline const flatbuffers::TypeTable *InputMousePressTypeTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    Gamium::Protocol::Types::InputMousePressTypeTypeTable
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 4, type_codes, type_refs, nullptr, nullptr, nullptr
  };
  return &tt;
}

inline const flatbuffers::TypeTable *InputMouseButtonCodeTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 },
    { flatbuffers::ET_SHORT, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    Gamium::Protocol::Types::InputMouseButtonCodeTypeTable
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 3, type_codes, type_refs, nullptr, nullptr, nullptr
  };
  return &tt;
}

}  // namespace Types
}  // namespace Protocol
}  // namespace Gamium

#endif  // FLATBUFFERS_GENERATED_INPUT_GAMIUM_PROTOCOL_TYPES_H_
