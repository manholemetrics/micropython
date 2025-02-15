"""ATTENTION! This module is autogenerated! Don't edit!"""

from protobuf.uprotobuf import Message, Field, Enum

PACKAGE='DeviceServerMessages'

class SetupMessage(Message):
    class Coordinates(Message):
        _fields=[
            Field(name='longitude', type='Float', id=1, required=True),
            Field(name='latitude', type='Float', id=2, required=True),
        ]

    _fields=[
        Field(name='coordinates', type='Message', id=1, required=True, cls=Coordinates),
        Field(name='company_id', type='String', id=2, required=True),
        Field(name='account_id', type='String', id=3, required=True),
        Field(name='max_distance_mm', type='UInt32', id=4, required=True),
        Field(name='setup_notes', type='String', id=5),
        Field(name='manhole_thickness_mm', type='UInt32', id=6, required=True),
    ]
