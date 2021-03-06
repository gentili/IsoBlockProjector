#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class IBPdVector:
  """
  Attributes:
   - x
   - y
   - z
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'x', None, None, ), # 1
    (2, TType.DOUBLE, 'y', None, None, ), # 2
    (3, TType.DOUBLE, 'z', None, None, ), # 3
  )

  def __init__(self, x=None, y=None, z=None,):
    self.x = x
    self.y = y
    self.z = z

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.x = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.y = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.z = iprot.readDouble();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IBPdVector')
    if self.x is not None:
      oprot.writeFieldBegin('x', TType.DOUBLE, 1)
      oprot.writeDouble(self.x)
      oprot.writeFieldEnd()
    if self.y is not None:
      oprot.writeFieldBegin('y', TType.DOUBLE, 2)
      oprot.writeDouble(self.y)
      oprot.writeFieldEnd()
    if self.z is not None:
      oprot.writeFieldBegin('z', TType.DOUBLE, 3)
      oprot.writeDouble(self.z)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.x is None:
      raise TProtocol.TProtocolException(message='Required field x is unset!')
    if self.y is None:
      raise TProtocol.TProtocolException(message='Required field y is unset!')
    if self.z is None:
      raise TProtocol.TProtocolException(message='Required field z is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IBPiVector:
  """
  Attributes:
   - x
   - y
   - z
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'x', None, None, ), # 1
    (2, TType.I32, 'y', None, None, ), # 2
    (3, TType.I32, 'z', None, None, ), # 3
  )

  def __init__(self, x=None, y=None, z=None,):
    self.x = x
    self.y = y
    self.z = z

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.x = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.y = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.z = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IBPiVector')
    if self.x is not None:
      oprot.writeFieldBegin('x', TType.I32, 1)
      oprot.writeI32(self.x)
      oprot.writeFieldEnd()
    if self.y is not None:
      oprot.writeFieldBegin('y', TType.I32, 2)
      oprot.writeI32(self.y)
      oprot.writeFieldEnd()
    if self.z is not None:
      oprot.writeFieldBegin('z', TType.I32, 3)
      oprot.writeI32(self.z)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.x is None:
      raise TProtocol.TProtocolException(message='Required field x is unset!')
    if self.y is None:
      raise TProtocol.TProtocolException(message='Required field y is unset!')
    if self.z is None:
      raise TProtocol.TProtocolException(message='Required field z is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IBPPlayer:
  """
  Attributes:
   - id
   - name
   - worldid
   - location
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'worldid', None, None, ), # 3
    (4, TType.STRUCT, 'location', (IBPdVector, IBPdVector.thrift_spec), None, ), # 4
  )

  def __init__(self, id=None, name=None, worldid=None, location=None,):
    self.id = id
    self.name = name
    self.worldid = worldid
    self.location = location

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.worldid = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.location = IBPdVector()
          self.location.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IBPPlayer')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.worldid is not None:
      oprot.writeFieldBegin('worldid', TType.I32, 3)
      oprot.writeI32(self.worldid)
      oprot.writeFieldEnd()
    if self.location is not None:
      oprot.writeFieldBegin('location', TType.STRUCT, 4)
      self.location.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.worldid is None:
      raise TProtocol.TProtocolException(message='Required field worldid is unset!')
    if self.location is None:
      raise TProtocol.TProtocolException(message='Required field location is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IBPProjectionFrame:
  """
  Attributes:
   - size
   - blockdata
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'size', (IBPiVector, IBPiVector.thrift_spec), None, ), # 1
    (2, TType.STRING, 'blockdata', None, None, ), # 2
  )

  def __init__(self, size=None, blockdata=None,):
    self.size = size
    self.blockdata = blockdata

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.size = IBPiVector()
          self.size.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.blockdata = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IBPProjectionFrame')
    if self.size is not None:
      oprot.writeFieldBegin('size', TType.STRUCT, 1)
      self.size.write(oprot)
      oprot.writeFieldEnd()
    if self.blockdata is not None:
      oprot.writeFieldBegin('blockdata', TType.STRING, 2)
      oprot.writeString(self.blockdata)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.size is None:
      raise TProtocol.TProtocolException(message='Required field size is unset!')
    if self.blockdata is None:
      raise TProtocol.TProtocolException(message='Required field blockdata is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
