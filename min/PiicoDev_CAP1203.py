_E='single'
_D=b'\x00'
_C=None
_B='NaN'
_A='big'
from PiicoDev_Unified import *
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
_CAP1203Address=b'('
_MAIN_CONTROL=_D
_GENERAL_STATUS=b'\x02'
_SENSOR_INPUT_STATUS=b'\x03'
_SENSOR_INPUT_1_DELTA_COUNT=b'\x10'
_SENSOR_INPUT_2_DELTA_COUNT=b'\x11'
_SENSOR_INPUT_3_DELTA_COUNT=b'\x12'
_SENSITIVITY_CONTROL=b'\x1f'
_CONFIG=b' '
_INTERRUPT_ENABLE=b"'"
_REPEAT_RATE_ENABLE=b'('
_MULTIPLE_TOUCH_CONFIG=b'*'
_MULTIPLE_TOUCH_PATTERN_CONFIG=b'+'
_MULTIPLE_TOUCH_PATTERN=b'-'
_PRODUCT_ID=b'\xfd'
_PROD_ID_VALUE=b'm'
class PiicoDev_CAP1203:
	def __init__(self,bus=_C,freq=_C,sda=_C,scl=_C,addr=int.from_bytes(_CAP1203Address,_A),touchmode=_E,sensitivity=6):
		A=b'\x80'
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
		for i in range(0,1):
			sleep_ms(1000)
			try:
				product_ID_value=self.i2c.readfrom_mem(self.addr,int.from_bytes(_PRODUCT_ID,_A),1)
				if product_ID_value==_PROD_ID_VALUE:print('product ID match');print('connected...')
			except:print('connection failed')
			if touchmode==_E:self.setBits(_MULTIPLE_TOUCH_CONFIG,A,A)
			if touchmode=='multi':self.setBits(_MULTIPLE_TOUCH_CONFIG,_D,A)
			if sensitivity>=0 and sensitivity<=7:self.setBits(_SENSITIVITY_CONTROL,bytes([sensitivity*16]),b'p')
	def setBits(self,address,byte,mask):
		old_byte=int.from_bytes(self.i2c.readfrom_mem(self.addr,int.from_bytes(address,_A),1),_A);temp_byte=old_byte;int_byte=int.from_bytes(byte,_A);int_mask=int.from_bytes(mask,_A)
		for n in range(8):
			bit_mask=int_mask>>n&1
			if bit_mask==1:
				if int_byte>>n&1==1:temp_byte=temp_byte|1<<n
				else:temp_byte=temp_byte&~(1<<n)
		new_byte=temp_byte;self.i2c.writeto_mem(self.addr,int.from_bytes(address,_A),bytes([new_byte]))
	def getSensitivity(self):sensitivity_control=self.i2c.readfrom_mem(self.addr,int.from_bytes(_SENSITIVITY_CONTROL,_A),1)
	def setSensitivity(self):self.i2c.writeto_mem(self.addr,int.from_bytes(_SENSITIVITY_CONTROL,_A),111)
	def clearInterrupt(self):self.i2c.writeto_mem(self.addr,int.from_bytes(_MAIN_CONTROL,_A),bytes([0]));main_control_value=self.i2c.readfrom_mem(self.addr,int.from_bytes(_MAIN_CONTROL,_A),1)
	def read(self):
		CS1return=0;CS2return=0;CS3return=0
		try:self.clearInterrupt();general_status_value=self.i2c.readfrom_mem(self.addr,int.from_bytes(_GENERAL_STATUS,_A),1)
		except:print(i2c_err_str.format(self.addr));return float(_B),float(_B),float(_B)
		mask=1;value=mask&int.from_bytes(general_status_value,_A);sensor_input_status=self.i2c.readfrom_mem(self.addr,int.from_bytes(_SENSOR_INPUT_STATUS,_A),1);CS1=1&int.from_bytes(sensor_input_status,_A);CS2=2&int.from_bytes(sensor_input_status,_A);CS3=4&int.from_bytes(sensor_input_status,_A)
		if CS1>0:CS1return=1
		if CS2>0:CS2return=1
		if CS3>0:CS3return=1
		return CS1return,CS2return,CS3return
	def readDeltaCounts(self):
		DC1return=0;DC2return=0;DC3return=0
		try:DC1=self.i2c.readfrom_mem(self.addr,int.from_bytes(_SENSOR_INPUT_1_DELTA_COUNT,_A),1);DC2=self.i2c.readfrom_mem(self.addr,int.from_bytes(_SENSOR_INPUT_2_DELTA_COUNT,_A),1);DC3=self.i2c.readfrom_mem(self.addr,int.from_bytes(_SENSOR_INPUT_3_DELTA_COUNT,_A),1)
		except:print(i2c_err_str.format(self.addr));return float(_B),float(_B),float(_B)
		return DC1,DC2,DC3