from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import Field, confloat, conint, constr

from mymodels._pydantic_v1.base_model import BaseModel


class StrEnum(str, Enum):
    def __repr__(self) -> str:
        return str.__repr__(self.value)


class Class1(StrEnum):
    field1 = "field1"
    field2 = "field2"
    field3 = "field3"
    field4 = "field4"


class Class2(StrEnum):
    field5 = "field5"
    field6 = "field6"


class Class3(StrEnum):
    field7 = "field7"
    field_8 = "field_8"
    field_9 = "field_9"
    field10 = "field10"
    field_11 = "field_11"
    field12 = "field12"
    field_13 = "field_13"


class Class4(StrEnum):
    field_14 = "field_14"
    field15 = "field15"
    field_16 = "field_16"


class Class5(StrEnum):
    field17 = "field17"
    field18 = "field18"


class Class6(StrEnum):
    field19 = "field19"
    field20 = "field20"


class Class7(StrEnum):
    field21 = "field21"
    field22 = "field22"
    field23 = "field23"
    field24 = "field24"


class Class8(StrEnum):
    field25 = "field25"
    field26 = "field26"
    field27 = "field27"
    field28 = "field28"


class Class9(StrEnum):
    field29 = "field29"
    field30 = "field30"
    field31 = "field31"
    field32 = "field32"
    field33 = "field33"
    field34 = "field34"
    field35 = "field35"
    field36 = "field36"


class Class10(StrEnum):
    field37 = "field37"
    field38 = "field38"
    field39 = "field39"
    field40 = "field40"
    field41 = "field41"
    field42 = "field42"


class Class11(StrEnum):
    field43 = "field43"
    field44 = "field44"
    field_45 = "field_45"
    field46 = "field46"
    field47 = "field47"
    field42 = "field42"
    field41 = "field41"
    field48 = "field48"


class Class12(StrEnum):
    field49 = "field49"
    field50 = "field50"
    field51 = "field51"
    field_52 = "field_52"
    field41 = "field41"
    field43 = "field43"
    field47 = "field47"
    field53 = "field53"


class Class13(StrEnum):
    field_54 = "field_54"
    field_55 = "field_55"
    field_56 = "field_56"
    field_57 = "field_57"
    field58 = "field58"
    field59 = "field59"


class Class14(BaseModel):
    __root__: Optional[Literal["DEGREES"]] = None


class Class15(StrEnum):
    field_60 = "field_60"
    field_61 = "field_61"
    field_62 = "field_62"
    field_63 = "field_63"


class Class16(StrEnum):
    field64 = "field64"
    field65 = "field65"
    field66 = "field66"
    field67 = "field67"
    field68 = "field68"
    field69 = "field69"


class Class17(StrEnum):
    field70 = "field70"
    field71 = "field71"
    field72 = "field72"
    field73 = "field73"
    field74 = "field74"
    field75 = "field75"
    field76 = "field76"
    field77 = "field77"
    field78 = "field78"
    field79 = "field79"
    field80 = "field80"
    field81 = "field81"
    field82 = "field82"
    field83 = "field83"
    field84 = "field84"
    field85 = "field85"


class Class18(StrEnum):
    field86 = "field86"
    field87 = "field87"


class Class19(StrEnum):
    field88 = "field88"
    field89 = "field89"


class Class20(StrEnum):
    field_90 = "field_90"
    field_91 = "field_91"
    field_92 = "field_92"
    field_93 = "field_93"
    field4 = "field4"


class Class21(StrEnum):
    field_94 = "field_94"
    field_95 = "field_95"
    field_96 = "field_96"
    field_97 = "field_97"


class Class22(StrEnum):
    field_98 = "field_98"
    field_99 = "field_99"
    field_100 = "field_100"


class Class23(BaseModel):
    modelType: Literal["Class23"] = "Class23"
    field_101: Optional[constr(regex="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.__fields_set__.add("modelType")

    @property
    def model_type(self):
        return self.modelType


class Class24(BaseModel):
    field102: Optional[str] = None
    field103: Optional[str] = None


class Class25(BaseModel):
    field102: Optional[str] = None
    field103: Optional[float] = None


class Class26(Class23):
    modelType: Literal["Class26"] = "Class26"
    field104: Optional[Class1] = None
    field105: Optional[dict[str, Any]] = Field(None, description="")
    field_106: Optional[str] = Field(None, alias="field106", description="")
    field107: Optional[str] = Field(None, description="")
    field108: Optional[str] = Field(None, description="")
    field109: Optional[datetime] = Field(None, description="", example="")
    field_110: Optional[list[Class24]] = Field(
        [],
        alias="field110",
        description="",
        example=[{"key": "field-to-update", "value": "updated-value"}],
    )


class Class27(BaseModel):
    field102: Optional[str] = "id"
    field103: Any = None
    field111: Optional[Class13] = None


class Class28(BaseModel):
    field_112: Optional[Class3] = Field(None, alias="field112", description="", example="")
    field_113: Optional[str] = Field(None, alias="field113", description="")
    field_114: Optional[int] = Field(0, alias="field114", description="", example=2)
    field107: Optional[constr(min_length=1, max_length=36)] = Field(
        None, description="", example=""
    )
    field115: Optional[constr(min_length=0, max_length=64)] = Field(
        None, description="", example=""
    )


class Class29(Class23):
    modelType: Literal["Class29"] = "Class29"
    field_116: Optional[datetime] = Field(None, alias="field116")
    field117: Optional[str] = Field(None, example="")


class Class30(BaseModel):
    field118: Optional[str] = None
    field119: Optional[list[str]] = None


class Class31(BaseModel):
    field_120: Optional[float] = Field(None, alias="field120", description="", example=256)
    field_121: Optional[float] = Field(None, alias="field121", description="", example=256)
    field_122: Optional[float] = Field(None, alias="field122", description="", example=256)
    field_123: Optional[float] = Field(None, alias="field123", description="", example=256)
    field_124: Optional[float] = Field(None, alias="field124", description="", example=0.85)


class Class32(BaseModel):
    field_125: Optional[float] = Field(None, alias="field125", description="", example=256)
    field_126: Optional[float] = Field(None, alias="field126", description="", example=256)
    field_127: Optional[float] = Field(None, alias="field127", description="", example=1.1)
    field_128: Optional[float] = Field(None, alias="field128", description="", example=1.1)
    field_129: Optional[Class15] = Field(None, alias="field129", description="", example="")
    field_130: Optional[Class15] = Field(None, alias="field130", description="", example="")
    field_131: Optional[float] = Field(None, alias="field131", description="", example=1.1)
    field_132: Optional[float] = Field(None, alias="field132", description="", example=1.1)
    field_133: Optional[float] = Field(None, alias="field133", description="", example=1.1)
    field_134: Optional[float] = Field(None, alias="field134", description="", example=1.1)
    field_135: Optional[float] = Field(None, alias="field135", description="", example=512)
    field_136: Optional[float] = Field(None, alias="field136", description="", example=512)
    field_137: Optional[Class14] = Field(None, alias="field137", description="", example="")
    field_138: Optional[Class14] = Field(None, alias="field138", description="", example="")
    field_139: Optional[float] = Field(None, alias="field139", description="", example=512)


class Class33(BaseModel):
    __root__: Optional[Union[Class26, Class29]] = Field(None, discriminator="modelType")


class Class34(BaseModel):
    field140: Optional[Class19] = None
    field_141: Optional[list[str]] = Field(
        [], alias="field141", example=["createdAt", "currentStatus", "id"]
    )
    field142: Optional[list[Class27]] = None
    field143: Optional[int] = 0
    field_144: Optional[int] = Field(1, alias="field144")


class Class35(BaseModel):
    modelType: Literal["Class35"] = "Class35"
    id: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field_145: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field145"
    )
    field_101: Optional[constr(regex="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )
    field_146: Optional[datetime] = Field(None, alias="field146", description="", example="")
    field_147: Optional[datetime] = Field(None, alias="field147", description="", example="")
    field_148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", example=""
    )
    field_149: Optional[Class7] = Field(None, alias="field149")
    field_150: Optional[list[Class36]] = Field(None, alias="field150")
    field_151: Optional[list[AnyClass129]] = Field(None, alias="field151")
    field152: Optional[list[Class24]] = Field([], description="")

    def __init__(self, **data):
        super().__init__(**data)
        self.__fields_set__.add("modelType")

    @property
    def model_type(self):
        return self.modelType


class Class36(BaseModel):
    field153: Optional[AnyClass122] = None
    id: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field_154: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field154"
    )
    field_155: Optional[str] = Field(None, alias="field155")
    field_101: Optional[constr(regex="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )
    model_type: Optional[str] = Field(None, alias="modelType", description="")
    field_156: Optional[datetime] = Field(None, alias="field156", description="", example="")
    field_157: Optional[datetime] = Field(None, alias="field157", description="", example="")
    field_148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", example=""
    )
    field_149: Optional[Class7] = Field(None, alias="field149")


class Class37(BaseModel):
    modelType: Literal["Class37"] = "Class37"
    field153: Optional[AnyClass122] = None
    id: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field_145: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field145"
    )
    field_101: Optional[constr(regex="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )
    field_146: Optional[datetime] = Field(None, alias="field146", description="", example="")
    field_147: Optional[datetime] = Field(None, alias="field147", description="", example="")
    field_148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", example=""
    )
    field_149: Optional[Class7] = Field(None, alias="field149")
    field152: Optional[list[Class24]] = Field([], description="")
    field_158: Optional[constr(min_length=0, max_length=64)] = Field(
        None, alias="field158", description="", example=""
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.__fields_set__.add("modelType")

    @property
    def model_type(self):
        return self.modelType


class Class38(BaseModel):
    __root__: Optional[
        Union[
            Class49,
            Class50,
            Class78,
            Class79,
            Class80,
            Class81,
            Class82,
            Class83,
            Class84,
            Class85,
            Class86,
            Class87,
            Class88,
            Class89,
            Class90,
            Class91,
            Class92,
            Class93,
            Class94,
            Class95,
            Class96,
            Class97,
            Class98,
            Class99,
            Class100,
            Class101,
            Class102,
            Class103,
            Class104,
            Class105,
            Class106,
            Class107,
            Class121,
            Class108,
            Class109,
            Class110,
            Class111,
            Class112,
            Class113,
            Class114,
            Class115,
            Class116,
            Class117,
            Class118,
            Class119,
            Class120,
            Class60,
            Class61,
            Class62,
            Class63,
            Class64,
            Class65,
            Class67,
            Class66,
            Class68,
            Class69,
            Class70,
            Class71,
            Class72,
            Class73,
        ]
    ] = Field(None, discriminator="modelType")


class Class39(BaseModel):
    __root__: Optional[Union[Class78, Class79, Class80, Class81, Class82]] = Field(
        None, discriminator="modelType"
    )


class Class40(BaseModel):
    __root__: Optional[
        Union[
            Class83,
            Class84,
            Class85,
            Class86,
            Class87,
            Class88,
            Class89,
            Class90,
            Class91,
            Class92,
            Class93,
            Class94,
            Class95,
        ]
    ] = Field(None, discriminator="modelType")


class Class41(BaseModel):
    __root__: Optional[Union[Class96, Class97, Class98]] = Field(None, discriminator="modelType")


class Class42(BaseModel):
    __root__: Optional[
        Union[Class99, Class100, Class101, Class102, Class103, Class104, Class105, Class106]
    ] = Field(None, discriminator="modelType")


class Class43(BaseModel):
    __root__: Optional[Union[Class107, Class121, Class108]] = Field(
        None, discriminator="modelType"
    )


class Class44(BaseModel):
    __root__: Optional[Union[Class109, Class110]] = Field(None, discriminator="modelType")


class Class45(BaseModel):
    __root__: Optional[Union[Class74, Class75, Class76, Class77]] = Field(
        None, discriminator="modelType"
    )


class Class46(BaseModel):
    __root__: Optional[Union[Class111, Class112, Class113]] = Field(
        None, discriminator="modelType"
    )


class Class47(BaseModel):
    __root__: Optional[Union[Class114, Class115, Class116, Class117]] = Field(
        None, discriminator="modelType"
    )


class Class48(BaseModel):
    __root__: Optional[Union[Class118, Class119, Class120]] = Field(
        None, discriminator="modelType"
    )


class Class49(Class35, Class28):
    modelType: Literal["Class49"] = "Class49"
    field159: Optional[constr(min_length=0, max_length=128)] = Field(
        None, description="", example=""
    )
    field160: Optional[str] = Field(None, description="")
    field_161: Optional[int] = Field(None, alias="field161", description="")
    field_162: Optional[str] = Field(None, alias="field162", description="")
    field_163: Optional[str] = Field(None, alias="field163", description="")
    field164: Optional[int] = Field(None, description="")


class Class50(Class35):
    modelType: Literal["Class50"] = "Class50"


class Class51(Class35, Class28):
    modelType: Literal["Class51"] = "Class51"
    field_165: Optional[Class60] = Field(None, alias="field165")
    field_166: Optional[datetime] = Field(None, alias="field166", description="", example="")
    field_167: Optional[datetime] = Field(None, alias="field167", description="", example="")
    field_168: Optional[datetime] = Field(None, alias="field168", description="", example="")
    field_169: Optional[datetime] = Field(None, alias="field169", description="", example="")
    field170: Optional[constr(min_length=0, max_length=1024)] = Field(
        None, description="", example=""
    )


class Class52(Class35):
    modelType: Literal["Class52"] = "Class52"
    field171: Optional[Class61] = None
    field172: Optional[AnyClass130] = None


class Class53(Class35):
    modelType: Literal["Class53"] = "Class53"
    field_173: Optional[datetime] = Field(None, alias="field173", description="", example="")


class Class54(Class35):
    modelType: Literal["Class54"] = "Class54"
    field174: Optional[AnyClass128] = None
    field175: Optional[Class69] = Field(None, description="")


class Class55(Class35):
    modelType: Literal["Class55"] = "Class55"
    field171: Optional[Class61] = None
    field_176: Optional[float] = Field(None, alias="field176", description="")


class Class56(Class35, Class28):
    modelType: Literal["Class56"] = "Class56"
    field_173: Optional[datetime] = Field(None, alias="field173", description="", example="")
    field_177: Optional[list[AnyClass126]] = Field(None, alias="field177")
    field175: Optional[Class69] = Field(None, description="")
    field172: Optional[AnyClass130] = None
    field_178: Optional[list[AnyClass132]] = Field(None, alias="field178", description="")
    field_179: Optional[bool] = Field(None, alias="field179", description="", example=False)
    field_180: Optional[bool] = Field(None, alias="field180", description="", example=False)


class Class57(Class35, Class28):
    modelType: Literal["Class57"] = "Class57"
    field_181: Optional[Class18] = Field(None, alias="field181")
    field_182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field118: Optional[str] = Field(None, example="")
    field_183: Optional[list[AnyClass124]] = Field(None, alias="field183")
    field_184: Optional[Class16] = Field(None, alias="field184", description="")
    field_185: Optional[list[AnyClass131]] = Field(None, alias="field185", description="")


class Class58(Class35):
    modelType: Literal["Class58"] = "Class58"
    field118: Optional[str] = Field(None, example="")
    field_181: Optional[Class18] = Field(None, alias="field181")
    field_186: Optional[list[Class60]] = Field(None, alias="field186")
    field172: Optional[AnyClass130] = None


class Class59(Class35, Class28):
    modelType: Literal["Class59"] = "Class59"
    field_187: Optional[list[Class61]] = Field(None, alias="field187")
    field_182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field_186: Optional[list[Class60]] = Field(None, alias="field186")
    field175: Optional[Class69] = Field(None, description="")
    field118: Optional[str] = Field(None, description="", example="")


class Class60(Class35, Class28):
    modelType: Literal["Class60"] = "Class60"
    field_188: Optional[list[AnyClass123]] = Field(None, alias="field188")
    field_189: Optional[float] = Field(None, alias="field189", description="", example=11)
    field_190: Optional[datetime] = Field(None, alias="field190", description="", example="")
    field_191: Optional[datetime] = Field(None, alias="field191", description="", example="")
    field171: Optional[Class61] = None
    field192: Optional[float] = Field(None, description="", example=10.0)
    field193: Optional[AnyClass131] = None
    field_194: Optional[str] = Field(None, alias="field194", description="")
    field195: Optional[AnyClass132] = None
    field_196: Optional[list[Class70]] = Field(None, alias="field196")
    field197: Optional[int] = Field(None, description="", example=10)
    field_198: Optional[Class8] = Field(None, alias="field198")
    field_199: Optional[Class5] = Field(None, alias="field199")
    field_200: Optional[str] = Field(None, alias="field200")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class61(Class35, Class28):
    modelType: Literal["Class61"] = "Class61"
    field_186: Optional[list[Class60]] = Field(None, alias="field186")
    field_181: Optional[Class11] = Field(None, alias="field181")
    field_202: Optional[list[Class62]] = Field(None, alias="field202")
    field195: Optional[AnyClass132] = None
    field197: Optional[int] = Field(None, description="", example=1)
    field_203: Optional[AnyClass127] = Field(None, alias="field203")
    field_183: Optional[list[AnyClass124]] = Field(None, alias="field183")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class62(Class35):
    modelType: Literal["Class62"] = "Class62"
    field153: Optional[Class61] = None
    field204: Optional[Class11] = None
    field_205: Optional[Class12] = Field(None, alias="field205")
    field_206: Optional[str] = Field(None, alias="field206")


class Class63(Class35):
    modelType: Literal["Class63"] = "Class63"
    field118: Optional[str] = Field(None, description="")
    field_207: Optional[str] = Field(None, alias="field207", description="")
    field_208: Optional[str] = Field(None, alias="field208", description="")
    field_209: Optional[Class64] = Field(None, alias="field209")


class Class64(Class35):
    modelType: Literal["Class64"] = "Class64"
    field118: Optional[str] = Field(None, description="")
    field_210: Optional[Class63] = Field(None, alias="field210")
    field211: Optional[Class10] = Field(None, description="")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class65(Class35):
    modelType: Literal["Class65"] = "Class65"
    field_212: Optional[float] = Field(None, alias="field212")
    field_213: Optional[float] = Field(None, alias="field213")
    field_214: Optional[float] = Field(None, alias="field214")
    field_215: Optional[float] = Field(None, alias="field215")
    field_216: Optional[float] = Field(None, alias="field216")
    field_217: Optional[float] = Field(None, alias="field217")
    field_116: Optional[datetime] = Field(None, alias="field116", description="")
    field218: Optional[Class67] = None
    field195: Optional[Class118] = None


class Class66(Class35):
    modelType: Literal["Class66"] = "Class66"
    field219: Optional[Class67] = None
    field_220: Optional[conint(ge=0, le=5)] = Field(None, alias="field220", description="")
    field_221: Optional[list[float]] = Field(
        None, alias="field221", description="", max_items=6, min_items=6
    )


class Class67(Class35):
    modelType: Literal["Class67"] = "Class67"
    field_222: Optional[list[Class66]] = Field(
        None, alias="field222", description="", max_items=6, min_items=6
    )
    field_223: Optional[Class65] = Field(None, alias="field223")


class Class68(Class35):
    modelType: Literal["Class68"] = "Class68"
    field_224: Optional[Class6] = Field(None, alias="field224")
    field_116: Optional[datetime] = Field(None, alias="field116")
    field_225: Optional[float] = Field(None, alias="field225", description="", example=1.1)
    field_226: Optional[float] = Field(None, alias="field226", description="", example=1.1)
    field195: Optional[Class119] = None


class Class69(Class35):
    modelType: Literal["Class69"] = "Class69"
    field118: Optional[str] = Field(None, description="", example="")
    field_179: Optional[bool] = Field(False, alias="field179", description="")
    field_227: Optional[str] = Field(None, alias="field227", example=16908)
    field_228: Optional[confloat(ge=0.0)] = Field(
        None, alias="field228", description="", example=0.02
    )
    field_229: Optional[confloat(ge=0.0)] = Field(
        None, alias="field229", description="", example=500.0
    )
    field230: Optional[confloat(ge=0.0, le=1.0)] = Field(None, description="", example=0.21)
    field_231: Optional[confloat(ge=0.0)] = Field(
        None, alias="field231", description="", example=2.1
    )
    field_178: Optional[list[AnyClass132]] = Field(None, alias="field178")
    field_182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field_177: Optional[list[AnyClass126]] = Field(None, alias="field177")


class Class70(Class35, Class28):
    modelType: Literal["Class70"] = "Class70"
    field_165: Optional[Class60] = Field(None, alias="field165")
    field_182: Optional[list[Class109]] = Field(None, alias="field182")
    field_232: Optional[datetime] = Field(None, alias="field232", description="", example="")
    field_233: Optional[datetime] = Field(None, alias="field233", description="", example="")
    field_234: Optional[float] = Field(None, alias="field234", description="", example=1.0)
    field_198: Optional[Class8] = Field(None, alias="field198")
    field_235: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field235"
    )
    field159: Optional[constr(min_length=0, max_length=128)] = Field(
        None, description="", example=""
    )
    field236: Optional[int] = Field(None, description="", example=371945)
    field_237: Optional[float] = Field(None, alias="field237", description="", example=21.23)
    field_238: Optional[float] = Field(None, alias="field238", description="", example=21.23)
    field_239: Optional[int] = Field(None, alias="field239", description="", example=1)
    field_240: Optional[int] = Field(None, alias="field240", description="", example=1)
    field_241: Optional[Class9] = Field(None, alias="field241", description="")
    field_242: Optional[int] = Field(None, alias="field242", description="", example=16)
    field_243: Optional[float] = Field(None, alias="field243", description="", example=321.123)
    field_244: Optional[float] = Field(None, alias="field244", description="", example=321.123)
    field_245: Optional[float] = Field(None, alias="field245", description="", example=321.123)
    field_246: Optional[float] = Field(None, alias="field246", description="", example=321.123)
    field_247: Optional[int] = Field(None, alias="field247", description="", example=1)
    field172: Optional[AnyClass130] = None
    field_248: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field248", description=""
    )
    field_249: Optional[int] = Field(None, alias="field249", description="")
    field_250: Optional[bool] = Field(None, alias="field250", description="")
    field_251: Optional[Class71] = Field(None, alias="field251")


class Class71(Class35):
    modelType: Literal["Class71"] = "Class71"
    field153: Optional[Class70] = None
    field_252: Optional[list[Class31]] = Field(None, alias="field252", description="")


class Class72(Class35):
    modelType: Literal["Class72"] = "Class72"
    field253: Optional[Class96] = None
    field104: Optional[Class20] = None
    field_254: Optional[float] = Field(None, alias="field254")
    field_255: Optional[float] = Field(None, alias="field255")


class Class73(Class35):
    modelType: Literal["Class73"] = "Class73"
    field174: Optional[Class109] = None
    field_256: Optional[bool] = Field(False, alias="field256", description="")
    field_257: Optional[float] = Field(None, alias="field257", description="")
    field_258: Optional[float] = Field(None, alias="field258", description="")


class Class74(Class37):
    modelType: Literal["Class74"] = "Class74"
    field_259: Optional[bool] = Field(None, alias="field259", description="")
    field_260: Optional[float] = Field(None, alias="field260", description="")


class Class75(Class37):
    modelType: Literal["Class75"] = "Class75"
    field_235: Optional[constr(regex="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field235"
    )


class Class76(Class37):
    modelType: Literal["Class76"] = "Class76"
    field_261: Optional[float] = Field(None, alias="field261", description="")
    field_262: Optional[float] = Field(None, alias="field262", description="")


class Class77(Class37):
    modelType: Literal["Class77"] = "Class77"
    field_227: Optional[str] = Field(None, alias="field227")
    field_263: Optional[str] = Field(None, alias="field263")
    field_184: Optional[Class16] = Field(None, alias="field184", description="")
    field_212: Optional[float] = Field(None, alias="field212")
    field_213: Optional[float] = Field(None, alias="field213")
    field_214: Optional[float] = Field(None, alias="field214")
    field_116: Optional[datetime] = Field(None, alias="field116", description="")


class Class78(Class51):
    modelType: Literal["Class78"] = "Class78"


class Class79(Class51):
    modelType: Literal["Class79"] = "Class79"


class Class80(Class51):
    modelType: Literal["Class80"] = "Class80"


class Class81(Class51):
    modelType: Literal["Class81"] = "Class81"
    field_264: Optional[str] = Field(None, alias="field264", description="")


class Class82(Class51):
    modelType: Literal["Class82"] = "Class82"


class Class83(Class52):
    modelType: Literal["Class83"] = "Class83"
    field_265: Optional[confloat(ge=-90.0, le=90.0)] = Field(0, alias="field265", description="")
    field_266: Optional[confloat(ge=-90.0, le=90.0)] = Field(90, alias="field266", description="")


class Class84(Class52):
    modelType: Literal["Class84"] = "Class84"
    field_265: Optional[confloat(ge=0.0, le=360.0)] = Field(0, alias="field265", description="")
    field_266: Optional[confloat(ge=0.0, le=360.0)] = Field(360, alias="field266", description="")
    field_267: Optional[bool] = Field(False, alias="field267", description="")


class Class85(Class52):
    modelType: Literal["Class85"] = "Class85"
    field_265: Optional[confloat(ge=-90.0, le=90.0)] = Field(-90, alias="field265", description="")
    field_266: Optional[confloat(ge=-90.0, le=90.0)] = Field(90, alias="field266", description="")


class Class86(Class52):
    modelType: Literal["Class86"] = "Class86"
    field_268: Optional[confloat(ge=-90.0, le=0.0)] = Field(-6, alias="field268", description="")


class Class87(Class52):
    modelType: Literal["Class87"] = "Class87"


class Class88(Class52):
    modelType: Literal["Class88"] = "Class88"
    field_265: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field265", description=""
    )
    field_266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )
    field_269: Optional[bool] = Field(False, alias="field269", description="")


class Class89(Class52):
    modelType: Literal["Class89"] = "Class89"
    field_265: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field265", description=""
    )
    field_266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )


class Class90(Class52):
    modelType: Literal["Class90"] = "Class90"
    field_265: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field265", description=""
    )
    field_266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )


class Class91(Class52):
    modelType: Literal["Class91"] = "Class91"
    field_270: Optional[list[str]] = Field(None, alias="field270", description="", min_items=1)


class Class92(Class52):
    modelType: Literal["Class92"] = "Class92"
    field_271: Optional[list[Class22]] = Field(None, alias="field271", description="")


class Class93(Class52):
    modelType: Literal["Class93"] = "Class93"
    field_272: Optional[list[str]] = Field(None, alias="field272", description="", min_items=1)


class Class94(Class52):
    modelType: Literal["Class94"] = "Class94"
    field_273: Optional[list[Class21]] = Field(None, alias="field273", description="")


class Class95(Class52):
    modelType: Literal["Class95"] = "Class95"
    field_274: Optional[datetime] = Field(None, alias="field274", description="", example="")
    field_275: Optional[datetime] = Field(None, alias="field275", description="", example="")


class Class96(Class53):
    modelType: Literal["Class96"] = "Class96"
    field_224: Optional[Class6] = Field(None, alias="field224")
    field276: Optional[Class72] = None
    field_277: Optional[Class109] = Field(None, alias="field277")
    field_278: Optional[Class110] = Field(None, alias="field278")
    field_184: Optional[Class16] = Field(None, alias="field184", description="")
    field_225: Optional[float] = Field(None, alias="field225", description="", example=1.1)
    field_279: Optional[float] = Field(None, alias="field279", description="", example=1.1)
    field_226: Optional[float] = Field(None, alias="field226", description="", example=1.1)
    field_280: Optional[float] = Field(None, alias="field280", description="", example=1.1)
    field_281: Optional[float] = Field(None, alias="field281", description="", example=1.1)
    field_282: Optional[float] = Field(None, alias="field282", description="", example=1.1)
    field_283: Optional[list[Class73]] = Field(None, alias="field283")


class Class97(Class53):
    modelType: Literal["Class97"] = "Class97"
    field_224: Optional[Class6] = Field(None, alias="field224")
    field_284: Optional[float] = Field(None, alias="field284", description="", example=1.1)
    field_285: Optional[float] = Field(None, alias="field285", description="", example=1.1)
    field_286: Optional[float] = Field(None, alias="field286", description="", example=1.1)
    field_287: Optional[float] = Field(None, alias="field287", description="", example=1.1)
    field_281: Optional[float] = Field(None, alias="field281", description="", example=1.1)
    field_282: Optional[float] = Field(None, alias="field282", description="", example=1.1)


class Class98(Class53):
    modelType: Literal["Class98"] = "Class98"
    field174: Optional[Class109] = None
    field_288: Optional[float] = Field(None, alias="field288", description="", example=10.0)
    field_289: Optional[float] = Field(None, alias="field289", description="", example=10.0)
    field_290: Optional[float] = Field(None, alias="field290", description="", example=10.0)
    field_291: Optional[float] = Field(None, alias="field291", description="", example=10.0)
    field_292: Optional[float] = Field(None, alias="field292", description="", example=10.0)
    field_293: Optional[float] = Field(None, alias="field293", description="", example=10.0)


class Class99(Class54):
    modelType: Literal["Class99"] = "Class99"
    field118: Optional[str] = Field("Missed Observation", description="")


class Class100(Class54):
    modelType: Literal["Class100"] = "Class100"
    field118: Optional[str] = Field("Maneuver Detection", description="")


class Class101(Class54):
    modelType: Literal["Class101"] = "Class101"
    field118: Optional[str] = Field("New Launch", description="")


class Class102(Class54):
    modelType: Literal["Class102"] = "Class102"
    field118: Optional[str] = Field("Deployment", description="")
    field294: Optional[int] = Field(None, description="")


class Class103(Class54):
    modelType: Literal["Class103"] = "Class103"
    field118: Optional[str] = Field("Articulation", description="")
    field170: Optional[str] = Field(None, description="")


class Class104(Class54):
    modelType: Literal["Class104"] = "Class104"
    field118: Optional[str] = Field("Orientation Change", description="")
    field_295: Optional[float] = Field(None, alias="field295")
    field_296: Optional[float] = Field(None, alias="field296")
    field_297: Optional[float] = Field(None, alias="field297")


class Class105(Class54):
    modelType: Literal["Class105"] = "Class105"
    field118: Optional[str] = Field("Transmission", description="")
    field_298: Optional[bool] = Field(None, alias="field298", description="")
    field_299: Optional[bool] = Field(None, alias="field299", description="")
    field_300: Optional[float] = Field(None, alias="field300")
    field_301: Optional[float] = Field(None, alias="field301")
    field_302: Optional[float] = Field(None, alias="field302", description="")
    field_303: Optional[float] = Field(None, alias="field303", description="")


class Class106(Class54):
    modelType: Literal["Class106"] = "Class106"
    field118: Optional[str] = Field("Breakup Event", description="")
    field_304: Optional[bool] = Field(None, alias="field304", description="")
    field_305: Optional[bool] = Field(None, alias="field305", description="")


class Class107(Class55):
    modelType: Literal["Class107"] = "Class107"
    field_198: Optional[Class8] = Field("LIGHT", alias="field198")
    field_306: Optional[str] = Field(None, alias="field306", description="", example="")
    field_307: Optional[int] = Field(None, alias="field307", example=6)
    field_234: Optional[float] = Field(None, alias="field234", description="")
    field_308: Optional[float] = Field(None, alias="field308", description="", example=15.0)
    field309: Optional[int] = Field(None, description="", example=4)
    field_310: Optional[Class4] = Field("RATE_TRACK_SIDEREAL", alias="field310")


class Class108(Class55):
    modelType: Literal["Class108"] = "Class108"
    field_311: Optional[float] = Field(None, alias="field311", description="")


class Class109(Class56):
    modelType: Literal["Class109"] = "Class109"
    field_312: Optional[Class70] = Field(None, alias="field312")
    field_313: Optional[list[Class72]] = Field(None, alias="field313")
    field_314: Optional[Class32] = Field(None, alias="field314")
    field315: Optional[Class96] = None
    field_316: Optional[Class98] = Field(None, alias="field316")


class Class110(Class56):
    modelType: Literal["Class110"] = "Class110"
    field315: Optional[Class96] = None


class Class111(Class57):
    modelType: Literal["Class111"] = "Class111"
    field_317: Optional[float] = Field(None, alias="field317", description="", example=1.0)
    field_318: Optional[float] = Field(None, alias="field318", description="", example=30.0)
    field_319: Optional[float] = Field(0.0, alias="field319", description="", example=20.0)
    field_320: Optional[float] = Field(None, alias="field320", description="")
    field_321: Optional[float] = Field(None, alias="field321", description="")
    field_322: Optional[float] = Field(None, alias="field322", description="")
    field_323: Optional[list[Class70]] = Field(None, alias="field323")


class Class112(Class57):
    modelType: Literal["Class112"] = "Class112"
    field_320: Optional[float] = Field(None, alias="field320", description="")
    field_321: Optional[float] = Field(None, alias="field321", description="")
    field_322: Optional[float] = Field(None, alias="field322", description="")
    field_317: Optional[float] = Field(None, alias="field317", description="", example=1.0)
    field_318: Optional[float] = Field(None, alias="field318", description="", example=30.0)
    field_319: Optional[float] = Field(0.0, alias="field319", description="", example=20.0)
    field_324: Optional[float] = Field(None, alias="field324", description="", example=0.01)
    field_325: Optional[float] = Field(None, alias="field325", description="", example=0.01)


class Class113(Class57):
    modelType: Literal["Class113"] = "Class113"
    field_320: Optional[float] = Field(None, alias="field320", description="")
    field_321: Optional[float] = Field(None, alias="field321", description="")
    field_322: Optional[float] = Field(None, alias="field322", description="")
    field_317: Optional[float] = Field(None, alias="field317", description="", example=1.0)
    field_318: Optional[float] = Field(None, alias="field318", description="", example=30.0)
    field_319: Optional[float] = Field(0.0, alias="field319", description="", example=20.0)
    field_324: Optional[float] = Field(None, alias="field324", description="", example=0.01)
    field_325: Optional[float] = Field(None, alias="field325", description="", example=0.01)
    field_326: Optional[bool] = Field(None, alias="field326", description="")


class Class114(Class58):
    modelType: Literal["Class114"] = "Class114"
    field_327: Optional[int] = Field(0, alias="field327", description="")
    field_328: Optional[list[str]] = Field(None, alias="field328")
    field_329: Optional[float] = Field(None, alias="field329", description="")
    field_330: Optional[float] = Field(None, alias="field330")
    field_331: Optional[float] = Field(None, alias="field331")
    field_332: Optional[float] = Field(None, alias="field332")
    field_333: Optional[float] = Field(None, alias="field333")
    field_334: Optional[float] = Field(None, alias="field334", description="", example=4.0)
    field_335: Optional[float] = Field(None, alias="field335", description="", example=4.0)
    field_336: Optional[float] = Field(None, alias="field336", example=200.0)
    field_337: Optional[float] = Field(None, alias="field337", description="", example=4.0)
    field_338: Optional[confloat(ge=0.0)] = Field(
        None, alias="field338", description="", example=1e-06
    )
    field_339: Optional[float] = Field(None, alias="field339", description="", example=3600.0)
    field_340: Optional[float] = Field(None, alias="field340", description="", example=4.0)
    field_341: Optional[float] = Field(None, alias="field341", description="", example=1)
    field_342: Optional[float] = Field(None, alias="field342", description="", example=3.0)
    field_343: Optional[float] = Field(None, alias="field343", description="", example=700.0)
    field_344: Optional[float] = Field(None, alias="field344", description="", example=5.0)
    field_345: Optional[float] = Field(None, alias="field345", example=1.0)
    field_346: Optional[float] = Field(None, alias="field346", description="", example=10.0)
    field_347: Optional[bool] = Field(False, alias="field347", description="")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class115(Class58):
    modelType: Literal["Class115"] = "Class115"
    field_329: Optional[float] = Field(None, alias="field329", description="")
    field_330: Optional[float] = Field(None, alias="field330")
    field_331: Optional[float] = Field(None, alias="field331")
    field_332: Optional[float] = Field(None, alias="field332")
    field_333: Optional[float] = Field(None, alias="field333")
    field_334: Optional[float] = Field(None, alias="field334", description="", example=4.0)
    field_336: Optional[float] = Field(None, alias="field336", example=200.0)
    field_338: Optional[float] = Field(None, alias="field338", description="", example=1e-06)
    field_339: Optional[float] = Field(None, alias="field339", description="", example=3600.0)
    field_341: Optional[float] = Field(None, alias="field341", description="", example=1)
    field_342: Optional[float] = Field(None, alias="field342", description="", example=3.0)
    field_348: Optional[float] = Field(None, alias="field348", description="", example=420.0)
    field_349: Optional[float] = Field(None, alias="field349", description="", example=870.0)
    field_343: Optional[float] = Field(None, alias="field343", description="", example=700.0)
    field_344: Optional[float] = Field(None, alias="field344", description="", example=5.0)
    field_345: Optional[float] = Field(None, alias="field345", example=1.0)
    field350: Optional[float] = Field(None, description="", example=1)
    field_351: Optional[float] = Field(None, alias="field351", description="")
    field_347: Optional[bool] = Field(False, alias="field347", description="")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class116(Class58):
    modelType: Literal["Class116"] = "Class116"
    field_329: Optional[float] = Field(None, alias="field329", description="")
    field_330: Optional[float] = Field(None, alias="field330")
    field_331: Optional[float] = Field(None, alias="field331")
    field_332: Optional[float] = Field(None, alias="field332")
    field_333: Optional[float] = Field(None, alias="field333")
    field_334: Optional[float] = Field(None, alias="field334", description="", example=4.0)
    field_336: Optional[float] = Field(None, alias="field336", example=200.0)
    field_338: Optional[float] = Field(None, alias="field338", description="", example=1e-06)
    field_339: Optional[float] = Field(None, alias="field339", description="", example=3600.0)
    field_341: Optional[float] = Field(None, alias="field341", description="", example=1)
    field_342: Optional[float] = Field(None, alias="field342", description="", example=3.0)
    field_348: Optional[float] = Field(None, alias="field348", description="", example=420.0)
    field_349: Optional[float] = Field(None, alias="field349", description="", example=870.0)
    field_343: Optional[float] = Field(None, alias="field343", description="", example=700.0)
    field_344: Optional[float] = Field(None, alias="field344", description="", example=5.0)
    field_345: Optional[float] = Field(None, alias="field345", example=1.0)
    field350: Optional[float] = Field(None, description="", example=1)
    field_351: Optional[float] = Field(None, alias="field351", description="", example=16.0)
    field_352: Optional[list[bool]] = Field(
        None, alias="field352", description="", max_items=4, min_items=4
    )
    field_347: Optional[bool] = Field(False, alias="field347", description="")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class117(Class58):
    modelType: Literal["Class117"] = "Class117"
    field_342: Optional[float] = Field(None, alias="field342", description="", example=3.0)
    field_353: Optional[float] = Field(None, alias="field353", description="")
    field_354: Optional[float] = Field(None, alias="field354", description="")
    field_355: Optional[float] = Field(None, alias="field355", description="")
    field_356: Optional[float] = Field(None, alias="field356", description="")
    field_357: Optional[float] = Field(None, alias="field357", description="")
    field_176: Optional[float] = Field(None, alias="field176", description="")
    field_358: Optional[list[confloat(ge=0.0, le=360.0)]] = Field(
        None, alias="field358", description=""
    )
    field_359: Optional[list[confloat(ge=0.0, le=360.0)]] = Field(
        None, alias="field359", description=""
    )
    field_360: Optional[int] = Field(None, alias="field360", description="")
    field_361: Optional[str] = Field(None, alias="field361", description="", example="")
    field_362: Optional[list[str]] = Field(None, alias="field362", description="")
    field_363: Optional[float] = Field(None, alias="field363", description="")
    field_364: Optional[list[Class24]] = Field(None, alias="field364", description="")
    field_365: Optional[float] = Field(None, alias="field365", description="")
    field_201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class118(Class59):
    modelType: Literal["Class118"] = "Class118"
    field_366: Optional[Class16] = Field("ICRF", alias="field366")
    field_367: Optional[list[Class65]] = Field(None, alias="field367", description="", min_items=1)


class Class119(Class59):
    modelType: Literal["Class119"] = "Class119"
    field_224: Optional[Class6] = Field(None, alias="field224")
    field_368: Optional[list[Class68]] = Field(None, alias="field368", description="")


class Class120(Class59):
    modelType: Literal["Class120"] = "Class120"
    field369: Optional[constr(min_length=0, max_length=69)] = Field(
        None, description="", example=""
    )
    field370: Optional[constr(min_length=0, max_length=69)] = Field(
        None, description="", example=""
    )
    field371: Optional[constr(min_length=0, max_length=69)] = Field(
        None, description="", example=""
    )


class Class121(Class107):
    modelType: Literal["Class121"] = "Class121"
    field_372: Optional[conint(ge=0, le=2)] = Field(0, alias="field372", description="")
    field_373: Optional[conint(ge=0, le=2)] = Field(0, alias="field373", description="")
    field_374: Optional[conint(ge=0, le=1)] = Field(0, alias="field374", description="")
    field_375: Optional[conint(ge=0, le=2)] = Field(0, alias="field375", description="")
    field_376: Optional[confloat(ge=0.0, le=600.0)] = Field(0.0, alias="field376", description="")
    field_377: Optional[conint(ge=1, le=99)] = Field(1, alias="field377", description="")
    field_378: Optional[conint(ge=0, le=64)] = Field(0, alias="field378", description="")
    field_379: Optional[conint(ge=0, le=1)] = Field(1, alias="field379", description="")
    field_380: Optional[conint(ge=0, le=1)] = Field(0, alias="field380", description="")
    field_381: Optional[conint(ge=0, le=1)] = Field(0, alias="field381", description="")
    field_382: Optional[conint(ge=0, le=1)] = Field(0, alias="field382", description="")
    field_383: Optional[conint(ge=0, le=1)] = Field(0, alias="field383", description="")
    field_384: Optional[conint(ge=0, le=1)] = Field(0, alias="field384", description="")
    field_385: Optional[conint(ge=0, le=1)] = Field(1, alias="field385", description="")
    field386: Optional[conint(ge=0, le=1)] = Field(0, description="")
    field387: Optional[conint(ge=0, le=4)] = Field(0, description="")


AnyClass122 = Annotated[
    Union[
        Class49,
        Class50,
        Class78,
        Class79,
        Class80,
        Class81,
        Class82,
        Class83,
        Class84,
        Class85,
        Class86,
        Class87,
        Class88,
        Class89,
        Class90,
        Class91,
        Class92,
        Class93,
        Class94,
        Class95,
        Class96,
        Class97,
        Class98,
        Class99,
        Class100,
        Class101,
        Class102,
        Class103,
        Class104,
        Class105,
        Class106,
        Class107,
        Class121,
        Class108,
        Class109,
        Class110,
        Class111,
        Class112,
        Class113,
        Class114,
        Class115,
        Class116,
        Class117,
        Class118,
        Class119,
        Class120,
        Class60,
        Class61,
        Class62,
        Class63,
        Class64,
        Class65,
        Class67,
        Class66,
        Class68,
        Class69,
        Class70,
        Class71,
        Class72,
        Class73,
        Class74,
        Class75,
        Class76,
    ],
    Field(discriminator="modelType"),
]
AnyClass123 = Annotated[
    Union[Class78, Class79, Class80, Class81, Class82], Field(discriminator="modelType")
]
AnyClass124 = Annotated[
    Union[
        Class83,
        Class84,
        Class85,
        Class86,
        Class87,
        Class88,
        Class89,
        Class90,
        Class91,
        Class92,
        Class93,
        Class94,
        Class95,
    ],
    Field(discriminator="modelType"),
]
AnyClass125 = Annotated[Union[Class96, Class97, Class98], Field(discriminator="modelType")]
AnyClass126 = Annotated[
    Union[Class99, Class100, Class101, Class102, Class103, Class104, Class105, Class106],
    Field(discriminator="modelType"),
]
AnyClass127 = Annotated[Union[Class107, Class121, Class108], Field(discriminator="modelType")]
AnyClass128 = Annotated[Union[Class109, Class110], Field(discriminator="modelType")]
AnyClass129 = Annotated[
    Union[Class74, Class75, Class76, Class77], Field(discriminator="modelType")
]
AnyClass130 = Annotated[Union[Class111, Class112, Class113], Field(discriminator="modelType")]
AnyClass131 = Annotated[
    Union[Class114, Class115, Class116, Class117], Field(discriminator="modelType")
]
AnyClass132 = Annotated[Union[Class118, Class119, Class120], Field(discriminator="modelType")]
Class35.update_forward_refs()
Class36.update_forward_refs()
Class37.update_forward_refs()
Class38.update_forward_refs()
Class39.update_forward_refs()
Class40.update_forward_refs()
Class41.update_forward_refs()
Class42.update_forward_refs()
Class43.update_forward_refs()
Class44.update_forward_refs()
Class45.update_forward_refs()
Class46.update_forward_refs()
Class47.update_forward_refs()
Class48.update_forward_refs()
Class49.update_forward_refs()
Class50.update_forward_refs()
Class51.update_forward_refs()
Class52.update_forward_refs()
Class53.update_forward_refs()
Class54.update_forward_refs()
Class55.update_forward_refs()
Class56.update_forward_refs()
Class57.update_forward_refs()
Class58.update_forward_refs()
Class59.update_forward_refs()
Class60.update_forward_refs()
Class61.update_forward_refs()
Class62.update_forward_refs()
Class63.update_forward_refs()
Class64.update_forward_refs()
Class65.update_forward_refs()
Class67.update_forward_refs()
Class66.update_forward_refs()
Class68.update_forward_refs()
Class69.update_forward_refs()
Class70.update_forward_refs()
Class71.update_forward_refs()
Class72.update_forward_refs()
Class73.update_forward_refs()
Class74.update_forward_refs()
Class75.update_forward_refs()
Class76.update_forward_refs()
Class77.update_forward_refs()
Class78.update_forward_refs()
Class79.update_forward_refs()
Class80.update_forward_refs()
Class81.update_forward_refs()
Class82.update_forward_refs()
Class83.update_forward_refs()
Class84.update_forward_refs()
Class85.update_forward_refs()
Class86.update_forward_refs()
Class87.update_forward_refs()
Class88.update_forward_refs()
Class89.update_forward_refs()
Class90.update_forward_refs()
Class91.update_forward_refs()
Class92.update_forward_refs()
Class93.update_forward_refs()
Class94.update_forward_refs()
Class95.update_forward_refs()
Class96.update_forward_refs()
Class97.update_forward_refs()
Class98.update_forward_refs()
Class99.update_forward_refs()
Class100.update_forward_refs()
Class101.update_forward_refs()
Class102.update_forward_refs()
Class103.update_forward_refs()
Class104.update_forward_refs()
Class105.update_forward_refs()
Class106.update_forward_refs()
Class107.update_forward_refs()
Class108.update_forward_refs()
Class109.update_forward_refs()
Class110.update_forward_refs()
Class111.update_forward_refs()
Class112.update_forward_refs()
Class113.update_forward_refs()
Class114.update_forward_refs()
Class115.update_forward_refs()
Class116.update_forward_refs()
Class117.update_forward_refs()
Class118.update_forward_refs()
Class119.update_forward_refs()
Class120.update_forward_refs()
Class121.update_forward_refs()
