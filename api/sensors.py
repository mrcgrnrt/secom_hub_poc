from enum import Enum

""" Structure of the compressed capabilities description

Represented by a 32 bit integer. The following bits are mapped to the
given parameters.

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
|-----| |-------------| |-------------| |-----| |-------------|
   |            |              |           |            +------- operations type
   |            |              |           +-------------------- conversation type
   |            |              +-------------------------------- value type
   |            +----------------------------------------------- model
   +------------------------------------------------------------ type

The values for the five parameters are described in the enums below. 

This module has two responsibilities:
  * provide the types for each capability in the form of Enums
  * provide methods to convert between the different forms of
    capability descriptions (types based on the Enums, compressed integer/hex)
"""

def decode_cap(cap_desc: int):
    """ Decode a capability description (given integer/hex value)
    
    If a given capability is not valid then it will be set to the Enum
    value *.INVALID.
    """
    return get_type(cap_desc), get_model(cap_desc), get_value_type(cap_desc), get_conversion_type(cap_desc), get_operations_type(cap_desc)


def encode_cap(type, model, value_type, conversion_type, operations_type):
    """ Encode a capability description from the given Enum values.
    
    Types of the single capabilities will be checked. If the are not valid 
    an exception will be raised.
    """
    if not isinstance(type, Type):
        raise TypeError("parameter 'type' must be of type Type")
    if not isinstance(model, Model):
        raise TypeError("parameter 'model' must be of type Model")
    if not isinstance(value_type, Value_Type):
        raise TypeError("parameter 'value_type' must be of type Value_Type")
    if not isinstance(conversion_type, Conversion_Type):
        raise TypeError("parameter 'conversion_type' must be of type Conversion_Type")
    if not isinstance(operations_type, Operations_Type):
        raise TypeError("parameter 'operations_type' must be of type Operations_Type")

    return (type.value << 28) + (model.value << 20) + (value_type.value << 12) + (conversion_type.value << 8) + (operations_type.value)



def decode_param(param_desc: int):
    """ Decode a parameter description (given integer/hex value)
    
    If a given parameter is not valid then it will be set to the Enum
    value *.INVALID.
    """
    return get_type(param_desc), get_model(param_desc), get_param(param_desc)


def encode_param(type, model, param):
    """ Encode a parameter description from the given Enum values.
    
    Types of the single capabilities will be checked. If the are not valid 
    an exception will be raised.
    """
    if not isinstance(type, Type):
        raise TypeError("parameter 'type' must be of type Type")
    if not isinstance(model, Model):
        raise TypeError("parameter 'model' must be of type Model")
    if not isinstance(param, Param):
        raise TypeError("parameter 'param' must be of type Param")
    
    return (type.value << 12) + (model.value << 4) + (param.value)


def get_type(cap_desc: int):
    try:
        type = Type((cap_desc >> 28) & 0x0000000f)
    except ValueError as vEr:
        type = Type.INVALID
    return type


def get_types():
    return [e.name for e in Type]


class Type(Enum):
    RESERVED  = 0x00
    VIBRATION = 0x01
    MOTOR     = 0x02
    MIC       = 0x03
    AIR       = 0x04
    INVALID   = 0x0f
    

def get_model(cap_desc: int):
    try:
        model = Model((cap_desc >> 20) & 0x000000ff)
    except ValueError as vEr:
        model = Model.INVALID
    return model


def get_models():
    return [e.name for e in Model]


class Model(Enum):
    RESERVED     = 0x00
    ST_IIS3DWB_0 = 0x01
    ST_IIS3DWB_1 = 0x02
    ST_IIS3DWB_2 = 0x03
    ST_IIS3DWB_3 = 0x04
    IFX_IMOTION  = 0x05
    IFX_X3D      = 0x06
    IFX_TLXXXXX  = 0x07
    SHT35        = 0x08
    INVALID      = 0xff
    
    
def get_value_type(cap_desc: int):
    try:
        value_type = Value_Type((cap_desc >> 12) & 0x000000ff)
    except ValueError as vEr:
        value_type = Value_Type.INVALID
    return value_type


def get_value_types():
    return [e.name for e in Value_Type]


class Value_Type(Enum):
    RESERVED  = 0x00
    IU        = 0x01 # imotion - Iu
    IV        = 0x02 # imotion - Iv
    VDC_RAW   = 0x03 # imotion - Vdc Raw
    ROT_ANG   = 0x04 # imotion - Rotor Angle
    V_ALPHA   = 0x05 # imotion - Valpha
    V_BETA    = 0x06 # imotion - Vbeta
    X         = 0x07 # ST IIS3DWB - X coordinate acceleration
    Y         = 0x08 # ST IIS3DWB - Y coordinate acceleration
    Z         = 0x09 # ST IIS3DWB - Z coordinate acceleration
    TS        = 0x0a # Timestamp
    TEMP      = 0x0b # Temperature
    HUMI      = 0x0c # Humidity
    INVALID   = 0xff


def get_conversion_type(cap_desc: int):
    try:
        conversion_type = Conversion_Type((cap_desc >> 8) & 0x0000000f)
    except ValueError as vEr:
        conversion_type = Conversion_Type.INVALID
    return conversion_type


def get_conversion_types():
    return [e.name for e in Conversion_Type]


class Conversion_Type(Enum):
    UNDEF        = 0x00
    ACCELERATION = 0x01
    VELOCITY     = 0x02
    RAW          = 0x03
    INVALID      = 0x0f


def get_operations_type(cap_desc: int):
    try:
        operations_type = Operations_Type((cap_desc >> 0) & 0x000000ff)
    except ValueError as vEr:
        operations_type = Operations_Type.INVALID
    return operations_type


def get_operations_types():
    return [e.name for e in Operations_Type]


class Operations_Type(Enum): 
    UNDEF                    = 0x00
    RMS                      = 0x01
    PEAK2PEAK                = 0x02
    CREST_FACTOR             = 0x03
    OCTAVE_SPECTRUM          = 0x04
    FREQUENCY_BAND           = 0x05
    ENVELOPE_OCTAVE_SPECTRUM = 0x06
    ENVELOPE_FREQ_BANDS      = 0x07
    PASSTHROUGH              = 0x08
    INVALID                  = 0xff


def get_param(param_desc: int):
    try:
        param = Param((param_desc >> 0) & 0x0000000f)
    except ValueError as vEr:
        param = Param.INVALID
    return param


def get_params():
    return [e.name for e in Param]

        
class Param(Enum):
    RESERVED  = 0x00
    ZG_OFFSET = 0x01
    VIB_SENS  = 0x02
    INTERVAL  = 0x03
    INVALID   = 0xff


