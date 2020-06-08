# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml_trade.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ml_trade.proto",
    package="fetch.aea.MlTrade",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0eml_trade.proto\x12\x11\x66\x65tch.aea.MlTrade"\xc0\x07\n\x0eMlTradeMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12G\n\x06\x61\x63\x63\x65pt\x18\x05 \x01(\x0b\x32\x35.fetch.aea.MlTrade.MlTradeMessage.Accept_PerformativeH\x00\x12\x41\n\x03\x63\x66p\x18\x06 \x01(\x0b\x32\x32.fetch.aea.MlTrade.MlTradeMessage.Cfp_PerformativeH\x00\x12\x43\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32\x33.fetch.aea.MlTrade.MlTradeMessage.Data_PerformativeH\x00\x12\x45\n\x05terms\x18\x08 \x01(\x0b\x32\x34.fetch.aea.MlTrade.MlTradeMessage.Terms_PerformativeH\x00\x1a"\n\x0b\x44\x65scription\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\x0c\x1a\x87\x01\n\x05Query\x12\x0f\n\x05\x62ytes\x18\x01 \x01(\x0cH\x00\x12\x42\n\x07nothing\x18\x02 \x01(\x0b\x32/.fetch.aea.MlTrade.MlTradeMessage.Query.NothingH\x00\x12\x15\n\x0bquery_bytes\x18\x03 \x01(\x0cH\x00\x1a\t\n\x07NothingB\x07\n\x05query\x1aJ\n\x10\x43\x66p_Performative\x12\x36\n\x05query\x18\x01 \x01(\x0b\x32\'.fetch.aea.MlTrade.MlTradeMessage.Query\x1aR\n\x12Terms_Performative\x12<\n\x05terms\x18\x01 \x01(\x0b\x32-.fetch.aea.MlTrade.MlTradeMessage.Description\x1a\x66\n\x13\x41\x63\x63\x65pt_Performative\x12<\n\x05terms\x18\x01 \x01(\x0b\x32-.fetch.aea.MlTrade.MlTradeMessage.Description\x12\x11\n\ttx_digest\x18\x02 \x01(\t\x1a\x62\n\x11\x44\x61ta_Performative\x12<\n\x05terms\x18\x01 \x01(\x0b\x32-.fetch.aea.MlTrade.MlTradeMessage.Description\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x42\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_MLTRADEMESSAGE_DESCRIPTION = _descriptor.Descriptor(
    name="Description",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Description",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Description.description",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=446,
    serialized_end=480,
)

_MLTRADEMESSAGE_QUERY_NOTHING = _descriptor.Descriptor(
    name="Nothing",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Query.Nothing",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=600,
    serialized_end=609,
)

_MLTRADEMESSAGE_QUERY = _descriptor.Descriptor(
    name="Query",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Query",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bytes",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Query.bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nothing",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Query.nothing",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="query_bytes",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Query.query_bytes",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MLTRADEMESSAGE_QUERY_NOTHING,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="query",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Query.query",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=483,
    serialized_end=618,
)

_MLTRADEMESSAGE_CFP_PERFORMATIVE = _descriptor.Descriptor(
    name="Cfp_Performative",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Cfp_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Cfp_Performative.query",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=620,
    serialized_end=694,
)

_MLTRADEMESSAGE_TERMS_PERFORMATIVE = _descriptor.Descriptor(
    name="Terms_Performative",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Terms_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Terms_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=696,
    serialized_end=778,
)

_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Accept_Performative",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Accept_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Accept_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tx_digest",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Accept_Performative.tx_digest",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=780,
    serialized_end=882,
)

_MLTRADEMESSAGE_DATA_PERFORMATIVE = _descriptor.Descriptor(
    name="Data_Performative",
    full_name="fetch.aea.MlTrade.MlTradeMessage.Data_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Data_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="fetch.aea.MlTrade.MlTradeMessage.Data_Performative.payload",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=884,
    serialized_end=982,
)

_MLTRADEMESSAGE = _descriptor.Descriptor(
    name="MlTradeMessage",
    full_name="fetch.aea.MlTrade.MlTradeMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.MlTrade.MlTradeMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.MlTrade.MlTradeMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.MlTrade.MlTradeMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.MlTrade.MlTradeMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accept",
            full_name="fetch.aea.MlTrade.MlTradeMessage.accept",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cfp",
            full_name="fetch.aea.MlTrade.MlTradeMessage.cfp",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="fetch.aea.MlTrade.MlTradeMessage.data",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="fetch.aea.MlTrade.MlTradeMessage.terms",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _MLTRADEMESSAGE_DESCRIPTION,
        _MLTRADEMESSAGE_QUERY,
        _MLTRADEMESSAGE_CFP_PERFORMATIVE,
        _MLTRADEMESSAGE_TERMS_PERFORMATIVE,
        _MLTRADEMESSAGE_ACCEPT_PERFORMATIVE,
        _MLTRADEMESSAGE_DATA_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.MlTrade.MlTradeMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=38,
    serialized_end=998,
)

_MLTRADEMESSAGE_DESCRIPTION.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_QUERY_NOTHING.containing_type = _MLTRADEMESSAGE_QUERY
_MLTRADEMESSAGE_QUERY.fields_by_name[
    "nothing"
].message_type = _MLTRADEMESSAGE_QUERY_NOTHING
_MLTRADEMESSAGE_QUERY.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _MLTRADEMESSAGE_QUERY.fields_by_name["bytes"]
)
_MLTRADEMESSAGE_QUERY.fields_by_name[
    "bytes"
].containing_oneof = _MLTRADEMESSAGE_QUERY.oneofs_by_name["query"]
_MLTRADEMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _MLTRADEMESSAGE_QUERY.fields_by_name["nothing"]
)
_MLTRADEMESSAGE_QUERY.fields_by_name[
    "nothing"
].containing_oneof = _MLTRADEMESSAGE_QUERY.oneofs_by_name["query"]
_MLTRADEMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _MLTRADEMESSAGE_QUERY.fields_by_name["query_bytes"]
)
_MLTRADEMESSAGE_QUERY.fields_by_name[
    "query_bytes"
].containing_oneof = _MLTRADEMESSAGE_QUERY.oneofs_by_name["query"]
_MLTRADEMESSAGE_CFP_PERFORMATIVE.fields_by_name[
    "query"
].message_type = _MLTRADEMESSAGE_QUERY
_MLTRADEMESSAGE_CFP_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_TERMS_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_TERMS_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_DATA_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_DATA_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE.fields_by_name[
    "accept"
].message_type = _MLTRADEMESSAGE_ACCEPT_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name["cfp"].message_type = _MLTRADEMESSAGE_CFP_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name["data"].message_type = _MLTRADEMESSAGE_DATA_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_TERMS_PERFORMATIVE
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["accept"]
)
_MLTRADEMESSAGE.fields_by_name[
    "accept"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["cfp"]
)
_MLTRADEMESSAGE.fields_by_name["cfp"].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name[
    "performative"
]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["data"]
)
_MLTRADEMESSAGE.fields_by_name[
    "data"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["terms"]
)
_MLTRADEMESSAGE.fields_by_name[
    "terms"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["MlTradeMessage"] = _MLTRADEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MlTradeMessage = _reflection.GeneratedProtocolMessageType(
    "MlTradeMessage",
    (_message.Message,),
    dict(
        Description=_reflection.GeneratedProtocolMessageType(
            "Description",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MLTRADEMESSAGE_DESCRIPTION,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Description)
            ),
        ),
        Query=_reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            dict(
                Nothing=_reflection.GeneratedProtocolMessageType(
                    "Nothing",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_MLTRADEMESSAGE_QUERY_NOTHING,
                        __module__="ml_trade_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Query.Nothing)
                    ),
                ),
                DESCRIPTOR=_MLTRADEMESSAGE_QUERY,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Query)
            ),
        ),
        Cfp_Performative=_reflection.GeneratedProtocolMessageType(
            "Cfp_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MLTRADEMESSAGE_CFP_PERFORMATIVE,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Cfp_Performative)
            ),
        ),
        Terms_Performative=_reflection.GeneratedProtocolMessageType(
            "Terms_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MLTRADEMESSAGE_TERMS_PERFORMATIVE,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Terms_Performative)
            ),
        ),
        Accept_Performative=_reflection.GeneratedProtocolMessageType(
            "Accept_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Accept_Performative)
            ),
        ),
        Data_Performative=_reflection.GeneratedProtocolMessageType(
            "Data_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MLTRADEMESSAGE_DATA_PERFORMATIVE,
                __module__="ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage.Data_Performative)
            ),
        ),
        DESCRIPTOR=_MLTRADEMESSAGE,
        __module__="ml_trade_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.MlTrade.MlTradeMessage)
    ),
)
_sym_db.RegisterMessage(MlTradeMessage)
_sym_db.RegisterMessage(MlTradeMessage.Description)
_sym_db.RegisterMessage(MlTradeMessage.Query)
_sym_db.RegisterMessage(MlTradeMessage.Query.Nothing)
_sym_db.RegisterMessage(MlTradeMessage.Cfp_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Terms_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Accept_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Data_Performative)


# @@protoc_insertion_point(module_scope)
