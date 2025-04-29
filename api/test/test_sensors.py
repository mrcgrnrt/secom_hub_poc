import unittest
import sensors as sensors

class TestSensors(unittest.TestCase):


    def test_get_type(self):
        type_from_int = sensors.get_type(1068175924) # -> 0x3fab1234
        self.assertEqual(type_from_int, sensors.Type.MIC)

        type_from_hex = sensors.get_type(0x2fab1234)
        self.assertEqual(type_from_hex, sensors.Type.MOTOR)

        type_from_hex = sensors.get_type(0x80000000)
        self.assertEqual(type_from_hex, sensors.Type.INVALID)

    def test_get_model(self):
        model_from_int = sensors.get_model(2148187358) # -> 0x800abcde
        self.assertEqual(model_from_int, sensors.Model.RESERVED)

        model_from_hex = sensors.get_model(0xa03abcde)
        self.assertEqual(model_from_hex, sensors.Model.ST_IIS3DWB_2)


    def test_get_value_type(self):
        value_type_from_int = sensors.get_value_type(2989515589) # -> 0xb2306345
        self.assertEqual(value_type_from_int, sensors.Value_Type.V_BETA)

        value_type_from_hex = sensors.get_value_type(0xa0305fa1)
        self.assertEqual(value_type_from_hex, sensors.Value_Type.V_ALPHA)


    def test_get_conversion_type(self):
        conversion_type_from_int = sensors.get_conversion_type(654016586) # -> 0x26fb804a
        self.assertEqual(conversion_type_from_int, sensors.Conversion_Type.UNDEF)

        conversion_type_from_hex = sensors.get_conversion_type(0xfe10021f)
        self.assertEqual(conversion_type_from_hex, sensors.Conversion_Type.VELOCITY)


    def test_get_operations_type(self):
        operations_type_from_int = sensors.get_operations_type(4278264577) # -> 0xff012301
        self.assertEqual(operations_type_from_int, sensors.Operations_Type.RMS)

        operations_type_from_hex = sensors.get_operations_type(0x12ab0103)
        self.assertEqual(operations_type_from_hex, sensors.Operations_Type.CREST_FACTOR)


    def test_get_param(self):
        param_from_int = sensors.get_param(67793)
        self.assertEqual(param_from_int, sensors.Param.ZG_OFFSET)
        
        param_from_int = sensors.get_param(67794)
        self.assertEqual(param_from_int, sensors.Param.VIB_SENS)
        
        param_from_int = sensors.get_param(67794)
        self.assertEqual(param_from_int, sensors.Param.VIB_SENS)
        
        
    def test_decode_cap(self):
        type, model, value_type, conversion_type, operations_type = sensors.decode_cap(0x20502301)
        self.assertEqual(sensors.Type.MOTOR, type)
        self.assertEqual(sensors.Model.IFX_IMOTION, model)
        self.assertEqual(sensors.Value_Type.IV, value_type)
        self.assertEqual(sensors.Conversion_Type.RAW, conversion_type)
        self.assertEqual(sensors.Operations_Type.RMS, operations_type)

        type, model, value_type, conversion_type, operations_type = sensors.decode_cap(0xffffffff)
        self.assertEqual(type, sensors.Type.INVALID)
        self.assertEqual(model, sensors.Model.INVALID)
        self.assertEqual(value_type, sensors.Value_Type.INVALID)
        self.assertEqual(conversion_type, sensors.Conversion_Type.INVALID)
        self.assertEqual(operations_type, sensors.Operations_Type.INVALID)
        
        type, model, value_type, conversion_type, operations_type = sensors.decode_cap(0x4080b308)
        self.assertEqual(type, sensors.Type.AIR)
        self.assertEqual(model, sensors.Model.SHT35)
        self.assertEqual(value_type, sensors.Value_Type.TEMP)
        self.assertEqual(conversion_type, sensors.Conversion_Type.RAW)
        self.assertEqual(operations_type, sensors.Operations_Type.INVALID)


    def test_encode_cap(self):
        try:
            sensors.encode_cap(sensors.Model.IFX_IMOTION, sensors.Type.INVALID, None, None, None)
        except Exception as ex:
            self.assertIsInstance(ex, TypeError)
        
        cap_desc = sensors.encode_cap(sensors.Type.VIBRATION, sensors.Model.ST_IIS3DWB_1, sensors.Value_Type.X, sensors.Conversion_Type.ACCELERATION, sensors.Operations_Type.PEAK2PEAK)
        self.assertEqual(0x10207102, cap_desc)

        cap_desc = sensors.encode_cap(sensors.Type.MOTOR, sensors.Model.IFX_IMOTION, sensors.Value_Type.IV, sensors.Conversion_Type.RAW, sensors.Operations_Type.RMS)
        self.assertEqual(0x20502301, cap_desc)