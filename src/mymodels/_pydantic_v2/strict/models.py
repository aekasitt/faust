from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import AwareDatetime, Field, RootModel, confloat, conint, constr

from mymodels._pydantic_v2.base_model import BaseModel


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
    field8 = "field8"
    field9 = "field9"
    field10 = "field10"
    field11 = "field11"
    field12 = "field12"
    field13 = "field13"


class Class4(StrEnum):
    field14 = "field14"
    field15 = "field15"
    field16 = "field16"


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
    field45 = "field45"
    field46 = "field46"
    field47 = "field47"
    field42 = "field42"
    field41 = "field41"
    field48 = "field48"


class Class12(StrEnum):
    field49 = "field49"
    field50 = "field50"
    field51 = "field51"
    field52 = "field52"
    field41 = "field41"
    field43 = "field43"
    field47 = "field47"
    field53 = "field53"


class Class13(StrEnum):
    field54 = "field54"
    field55 = "field55"
    field56 = "field56"
    field57 = "field57"
    field58 = "field58"
    field59 = "field59"


class Class14(RootModel):
    root: Literal["Class14"] = "Class14"


class Class15(StrEnum):
    field60 = "field60"
    field61 = "field61"
    field62 = "field62"
    field63 = "field63"


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
    field90 = "field90"
    field91 = "field91"
    field92 = "field92"
    field93 = "field93"
    field4 = "field4"


class Class21(StrEnum):
    field94 = "field94"
    field95 = "field95"
    field96 = "field96"
    field97 = "field97"


class Class22(StrEnum):
    field98 = "field98"
    field99 = "field99"
    field100 = "field100"


class Class23(BaseModel):
    model_type: Literal["Class23"] = "Class23"
    field101: Optional[constr(pattern="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.model_fields_set.add("model_type")


class Class24(BaseModel):
    field102: str
    field103: Optional[str] = None


class Class25(BaseModel):
    field102: Optional[str] = None
    field103: Optional[float] = None


class Class26(Class23):
    model_type: Literal["Class26"] = "Class26"
    field104: Optional[Class1] = None
    field105: dict[str, Any] = Field(..., description="")
    field106: str = Field(..., alias="field106", description="")
    field107: str = Field(..., description="")
    field108: str = Field(..., description="")
    field109: AwareDatetime = Field(..., description="", examples=["2018-01-01T18:00:00.123Z"])
    field110: list[Class24] = Field(
        ...,
        alias="field110",
        description="",
        examples=[[{"key": "field-to-update", "value": "updated-value"}]],
    )


class Class27(BaseModel):
    field102: str
    field103: Any = None
    field111: Class13


class Class28(BaseModel):
    field112: Optional[Class3] = Field(None, alias="field112", description="", examples=["U"])
    field113: Optional[str] = Field(None, alias="field113", description="")
    field114: Optional[int] = Field(0, alias="field114", description="", examples=[2])
    field107: Optional[constr(min_length=1, max_length=36)] = Field(
        None, description="", examples=["Bluestaq"]
    )
    field115: Optional[constr(min_length=0, max_length=64)] = Field(
        None, description="", examples=["THIRD_PARTY_DATASOURCE"]
    )


class Class29(Class23):
    model_type: Literal["Class29"] = "Class29"
    field116: Optional[AwareDatetime] = Field(None, alias="field116")
    field117: Optional[str] = Field(None, examples=["executive.agent3.sda"])


class Class30(BaseModel):
    field118: Optional[str] = None
    field119: Optional[list[str]] = None


class Class31(BaseModel):
    field120: Optional[float] = Field(None, alias="field120", description="", examples=[256])
    field121: Optional[float] = Field(None, alias="field121", description="", examples=[256])
    field122: Optional[float] = Field(None, alias="field122", description="", examples=[256])
    field123: Optional[float] = Field(None, alias="field123", description="", examples=[256])
    field124: Optional[float] = Field(None, alias="field124", description="", examples=[0.85])


class Class32(BaseModel):
    field125: Optional[float] = Field(None, alias="field125", description="", examples=[256])
    field126: Optional[float] = Field(None, alias="field126", description="", examples=[256])
    field127: Optional[float] = Field(None, alias="field127", description="", examples=[1.1])
    field128: Optional[float] = Field(None, alias="field128", description="", examples=[1.1])
    field129: Optional[Class15] = Field(
        None, alias="field129", description="", examples=["RA---TAN-SIP"]
    )
    field130: Optional[Class15] = Field(
        None, alias="field130", description="", examples=["DEC---TAN-SIP"]
    )
    field131: Optional[float] = Field(None, alias="field131", description="", examples=[1.1])
    field132: Optional[float] = Field(None, alias="field132", description="", examples=[1.1])
    field133: Optional[float] = Field(None, alias="field133", description="", examples=[1.1])
    field134: Optional[float] = Field(None, alias="field134", description="", examples=[1.1])
    field135: Optional[float] = Field(None, alias="field135", description="", examples=[512])
    field136: Optional[float] = Field(None, alias="field136", description="", examples=[512])
    field137: Optional[Class14] = Field(None, alias="field137", description="", examples=["deg"])
    field138: Optional[Class14] = Field(
        None, alias="field138", description="", examples=["DEGREE"]
    )
    field139: Optional[float] = Field(None, alias="field139", description="", examples=[512])


class Class33(RootModel):
    root: Union[Class26, Class29] = Field(..., discriminator="model_type")


class Class34(BaseModel):
    field140: Optional[Class19] = None
    field141: Optional[list[str]] = Field(
        [], alias="field141", examples=[["createdAt", "currentStatus", "id"]]
    )
    field142: list[Class27]
    field143: int
    field144: int = Field(..., alias="field144")


class Class35(BaseModel):
    model_type: Literal["Class35"] = "Class35"
    id: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field145: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field145"
    )
    field101: Optional[constr(pattern="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )
    field146: Optional[AwareDatetime] = Field(
        None, alias="field146", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field147: Optional[AwareDatetime] = Field(
        None, alias="field147", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", examples=["some.user"]
    )
    field149: Optional[Class7] = Field(None, alias="field149")
    field150: Optional[list[Class36]] = Field(None, alias="field150")
    field151: Optional[list[AnyClass129]] = Field(None, alias="field151")
    field152: Optional[list[Class24]] = Field([], description="")

    def __init__(self, **data):
        super().__init__(**data)
        self.model_fields_set.add("model_type")


class Class36(BaseModel):
    field153: Optional[AnyClass122] = None
    id: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field154: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field154"
    )
    field155: Optional[str] = Field(None, alias="field155")
    field101: constr(pattern="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?") = Field(..., alias="field101")
    model_type: str = Field(..., alias="modelType", description="")
    field156: Optional[AwareDatetime] = Field(
        None, alias="field156", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field157: Optional[AwareDatetime] = Field(
        None, alias="field157", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", examples=["some.user"]
    )
    field149: Optional[Class7] = Field(None, alias="field149")


class Class37(BaseModel):
    model_type: Literal["Class37"] = "Class37"
    field153: Optional[AnyClass122] = None
    id: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = None
    field145: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field145"
    )
    field101: Optional[constr(pattern="^([0-9]+\\.){2}(\\*|[0-9]+)(-.*)?")] = Field(
        "0.50.1", alias="field101"
    )
    field146: Optional[AwareDatetime] = Field(
        None, alias="field146", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field147: Optional[AwareDatetime] = Field(
        None, alias="field147", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field148: Optional[constr(min_length=1, max_length=64)] = Field(
        None, alias="field148", description="", examples=["some.user"]
    )
    field149: Optional[Class7] = Field(None, alias="field149")
    field152: Optional[list[Class24]] = Field([], description="")
    field158: Optional[constr(min_length=0, max_length=64)] = Field(
        None, alias="field158", description="", examples=["some.user"]
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.model_fields_set.add("model_type")


class Class38(RootModel):
    root: Union[
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
    ] = Field(..., discriminator="model_type")


class Class39(RootModel):
    root: Union[Class78, Class79, Class80, Class81, Class82] = Field(
        ..., discriminator="model_type"
    )


class Class40(RootModel):
    root: Union[
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
    ] = Field(..., discriminator="model_type")


class Class41(RootModel):
    root: Union[Class96, Class97, Class98] = Field(..., discriminator="model_type")


class Class42(RootModel):
    root: Union[Class99, Class100, Class101, Class102, Class103, Class104, Class105, Class106] = (
        Field(..., discriminator="model_type")
    )


class Class43(RootModel):
    root: Union[Class107, Class121, Class108] = Field(..., discriminator="model_type")


class Class44(RootModel):
    root: Union[Class109, Class110] = Field(..., discriminator="model_type")


class Class45(RootModel):
    root: Union[Class74, Class75, Class76, Class77] = Field(..., discriminator="model_type")


class Class46(RootModel):
    root: Union[Class111, Class112, Class113] = Field(..., discriminator="model_type")


class Class47(RootModel):
    root: Union[Class114, Class115, Class116, Class117] = Field(..., discriminator="model_type")


class Class48(RootModel):
    root: Union[Class118, Class119, Class120] = Field(..., discriminator="model_type")


class Class49(Class35, Class28):
    model_type: Literal["Class49"] = "Class49"
    field159: constr(min_length=0, max_length=128) = Field(
        ..., description="", examples=["filename.jpg"]
    )
    field160: Optional[str] = Field(None, description="")
    field161: Optional[int] = Field(None, alias="field161", description="")
    field162: Optional[str] = Field(None, alias="field162", description="")
    field163: Optional[str] = Field(None, alias="field163", description="")
    field164: Optional[int] = Field(None, description="")


class Class50(Class35):
    model_type: Literal["Class50"] = "Class50"


class Class51(Class35, Class28):
    model_type: Literal["Class51"] = "Class51"
    field165: Optional[Class60] = Field(None, alias="field165")
    field166: Optional[AwareDatetime] = Field(
        None, alias="field166", description="", examples=["2018-01-01T18:00:00.123Z"]
    )
    field167: Optional[AwareDatetime] = Field(
        None, alias="field167", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field168: Optional[AwareDatetime] = Field(
        None, alias="field168", description="", examples=["2018-01-01T18:00:00.123Z"]
    )
    field169: Optional[AwareDatetime] = Field(
        None, alias="field169", description="", examples=["2018-01-01T16:00:00.123Z"]
    )
    field170: Optional[constr(min_length=0, max_length=1024)] = Field(
        None, description="", examples=["Example notes"]
    )


class Class52(Class35):
    model_type: Literal["Class52"] = "Class52"
    field171: Optional[Class61] = None
    field172: Optional[AnyClass130] = None


class Class53(Class35):
    model_type: Literal["Class53"] = "Class53"
    field173: AwareDatetime = Field(
        ..., alias="field173", description="", examples=["2018-01-01T16:00:00.123456Z"]
    )


class Class54(Class35):
    model_type: Literal["Class54"] = "Class54"
    field174: Optional[AnyClass128] = None
    field175: Optional[Class69] = Field(None, description="")


class Class55(Class35):
    model_type: Literal["Class55"] = "Class55"
    field171: Optional[Class61] = None
    field176: Optional[float] = Field(None, alias="field176", description="")


class Class56(Class35, Class28):
    model_type: Literal["Class56"] = "Class56"
    field173: AwareDatetime = Field(
        ..., alias="field173", description="", examples=["2018-01-01T16:00:00.123456Z"]
    )
    field177: Optional[list[AnyClass126]] = Field(None, alias="field177")
    field175: Optional[Class69] = Field(None, description="")
    field172: Optional[AnyClass130] = None
    field178: Optional[list[AnyClass132]] = Field(None, alias="field178", description="")
    field179: Optional[bool] = Field(None, alias="field179", description="", examples=[False])
    field180: Optional[bool] = Field(None, alias="field180", description="", examples=[False])


class Class57(Class35, Class28):
    model_type: Literal["Class57"] = "Class57"
    field181: Optional[Class18] = Field(None, alias="field181")
    field182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field118: str = Field(..., examples=["PDS-RME03"])
    field183: Optional[list[AnyClass124]] = Field(None, alias="field183")
    field184: Optional[Class16] = Field(None, alias="field184", description="")
    field185: Optional[list[AnyClass131]] = Field(None, alias="field185", description="")


class Class58(Class35):
    model_type: Literal["Class58"] = "Class58"
    field118: str = Field(..., examples=["CCD 1"])
    field181: Optional[Class18] = Field(None, alias="field181")
    field186: Optional[list[Class60]] = Field(None, alias="field186")
    field172: Optional[AnyClass130] = None


class Class59(Class35, Class28):
    model_type: Literal["Class59"] = "Class59"
    field187: Optional[list[Class61]] = Field(None, alias="field187")
    field182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field186: Optional[list[Class60]] = Field(None, alias="field186")
    field175: Optional[Class69] = Field(None, description="")
    field118: str = Field(..., description="", examples=["Galaxy 15"])


class Class60(Class35, Class28):
    model_type: Literal["Class60"] = "Class60"
    field188: Optional[list[AnyClass123]] = Field(None, alias="field188")
    field189: Optional[float] = Field(None, alias="field189", description="", examples=[11])
    field190: AwareDatetime = Field(
        ..., alias="field190", description="", examples=["2018-01-01T16:00:00.123456Z"]
    )
    field191: AwareDatetime = Field(
        ..., alias="field191", description="", examples=["2018-01-01T18:00:00.123Z"]
    )
    field171: Class61
    field192: Optional[float] = Field(None, description="", examples=[10.0])
    field193: Optional[AnyClass131] = None
    field194: Optional[str] = Field(None, alias="field194", description="")
    field195: Optional[AnyClass132] = None
    field196: Optional[list[Class70]] = Field(None, alias="field196")
    field197: Optional[int] = Field(None, description="", examples=[10])
    field198: Optional[Class8] = Field(None, alias="field198")
    field199: Optional[Class5] = Field(None, alias="field199")
    field200: Optional[str] = Field(None, alias="field200")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class61(Class35, Class28):
    model_type: Literal["Class61"] = "Class61"
    field186: Optional[list[Class60]] = Field(None, alias="field186")
    field181: Class11 = Field(..., alias="field181")
    field202: Optional[list[Class62]] = Field(None, alias="field202")
    field195: AnyClass132
    field197: int = Field(..., description="", examples=[1])
    field203: AnyClass127 = Field(..., alias="field203")
    field183: Optional[list[AnyClass124]] = Field(None, alias="field183")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class62(Class35):
    model_type: Literal["Class62"] = "Class62"
    field153: Optional[Class61] = None
    field204: Optional[Class11] = None
    field205: Optional[Class12] = Field(None, alias="field205")
    field206: Optional[str] = Field(None, alias="field206")


class Class63(Class35):
    model_type: Literal["Class63"] = "Class63"
    field118: Optional[str] = Field(None, description="")
    field207: Optional[str] = Field(None, alias="field207", description="")
    field208: Optional[str] = Field(None, alias="field208", description="")
    field209: Optional[Class64] = Field(None, alias="field209")


class Class64(Class35):
    model_type: Literal["Class64"] = "Class64"
    field118: Optional[str] = Field(None, description="")
    field210: Optional[Class63] = Field(None, alias="field210")
    field211: Optional[Class10] = Field(None, description="")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class65(Class35):
    model_type: Literal["Class65"] = "Class65"
    field212: float = Field(..., alias="field212")
    field213: float = Field(..., alias="field213")
    field214: float = Field(..., alias="field214")
    field215: float = Field(..., alias="field215")
    field216: float = Field(..., alias="field216")
    field217: float = Field(..., alias="field217")
    field116: AwareDatetime = Field(..., alias="field116", description="")
    field218: Optional[Class67] = None
    field195: Optional[Class118] = None


class Class67(Class35):
    model_type: Literal["Class67"] = "Class67"
    field222: list[Class66] = Field(
        ..., alias="field222", description="", max_length=6, min_length=6
    )
    field223: Class65 = Field(..., alias="field223")


class Class66(Class35):
    model_type: Literal["Class66"] = "Class66"
    field219: Optional[Class67] = None
    field220: conint(ge=0, le=5) = Field(..., alias="field220", description="")
    field221: list[float] = Field(
        ..., alias="field221", description="", max_length=6, min_length=6
    )


class Class68(Class35):
    model_type: Literal["Class68"] = "Class68"
    field224: Optional[Class6] = Field(None, alias="field224")
    field116: AwareDatetime = Field(..., alias="field116")
    field225: float = Field(..., alias="field225", description="", examples=[1.1])
    field226: float = Field(..., alias="field226", description="", examples=[1.1])
    field195: Optional[Class119] = None


class Class69(Class35):
    model_type: Literal["Class69"] = "Class69"
    field118: Optional[str] = Field(None, description="", examples=["Galaxy 15"])
    field179: Optional[bool] = Field(False, alias="field179", description="")
    field227: str = Field(..., alias="field227", examples=[16908])
    field228: Optional[confloat(ge=0.0)] = Field(
        None, alias="field228", description="", examples=[0.02]
    )
    field229: Optional[confloat(ge=0.0)] = Field(
        None, alias="field229", description="", examples=[500.0]
    )
    field230: Optional[confloat(ge=0.0, le=1.0)] = Field(None, description="", examples=[0.21])
    field231: Optional[confloat(ge=0.0)] = Field(
        None, alias="field231", description="", examples=[2.1]
    )
    field178: Optional[list[AnyClass132]] = Field(None, alias="field178")
    field182: Optional[list[AnyClass128]] = Field(None, alias="field182")
    field177: Optional[list[AnyClass126]] = Field(None, alias="field177")


class Class70(Class35, Class28):
    model_type: Literal["Class70"] = "Class70"
    field165: Optional[Class60] = Field(None, alias="field165")
    field182: Optional[list[Class109]] = Field(None, alias="field182")
    field232: Optional[AwareDatetime] = Field(
        None, alias="field232", description="", examples=["2021-01-01T01:01:01.123456Z"]
    )
    field233: AwareDatetime = Field(
        ..., alias="field233", description="", examples=["2021-01-01T01:01:01.123456Z"]
    )
    field234: float = Field(..., alias="field234", description="", examples=[1.0])
    field198: Optional[Class8] = Field(None, alias="field198")
    field235: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field235"
    )
    field159: Optional[constr(min_length=0, max_length=128)] = Field(
        None, description="", examples=["filename.fits"]
    )
    field236: Optional[int] = Field(None, description="", examples=[371945])
    field237: Optional[float] = Field(None, alias="field237", description="", examples=[21.23])
    field238: Optional[float] = Field(None, alias="field238", description="", examples=[21.23])
    field239: Optional[int] = Field(None, alias="field239", description="", examples=[1])
    field240: Optional[int] = Field(None, alias="field240", description="", examples=[1])
    field241: Class9 = Field(..., alias="field241", description="")
    field242: Optional[int] = Field(None, alias="field242", description="", examples=[16])
    field243: Optional[float] = Field(None, alias="field243", description="", examples=[321.123])
    field244: Optional[float] = Field(None, alias="field244", description="", examples=[321.123])
    field245: Optional[float] = Field(None, alias="field245", description="", examples=[321.123])
    field246: Optional[float] = Field(None, alias="field246", description="", examples=[321.123])
    field247: int = Field(..., alias="field247", description="", examples=[1])
    field172: Optional[AnyClass130] = None
    field248: constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}") = Field(
        ..., alias="field248", description=""
    )
    field249: int = Field(..., alias="field249", description="")
    field250: Optional[bool] = Field(None, alias="field250", description="")
    field251: Optional[Class71] = Field(None, alias="field251")
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class71(Class35):
    model_type: Literal["Class71"] = "Class71"
    field153: Optional[Class70] = None
    field252: Optional[list[Class31]] = Field(None, alias="field252", description="")


class Class72(Class35):
    model_type: Literal["Class72"] = "Class72"
    field253: Optional[Class96] = None
    field104: Class20
    field254: Optional[float] = Field(None, alias="field254")
    field255: Optional[float] = Field(None, alias="field255")


class Class73(Class35):
    model_type: Literal["Class73"] = "Class73"
    field174: Optional[Class109] = None
    field256: Optional[bool] = Field(False, alias="field256", description="")
    field257: Optional[float] = Field(None, alias="field257", description="")
    field258: Optional[float] = Field(None, alias="field258", description="")


class Class74(Class37):
    model_type: Literal["Class74"] = "Class74"
    field259: Optional[bool] = Field(None, alias="field259", description="")
    field260: Optional[float] = Field(None, alias="field260", description="")


class Class75(Class37):
    model_type: Literal["Class75"] = "Class75"
    field235: Optional[constr(pattern="[a-f0-9]{8}(?:-[a-f0-9]{4}){4}[a-f0-9]{8}")] = Field(
        None, alias="field235"
    )


class Class76(Class37):
    model_type: Literal["Class76"] = "Class76"
    field261: Optional[float] = Field(None, alias="field261", description="")
    field262: Optional[float] = Field(None, alias="field262", description="")


class Class77(Class37):
    model_type: Literal["Class77"] = "Class77"
    field227: str = Field(..., alias="field227")
    field263: Optional[str] = Field(None, alias="field263")
    field184: Class16 = Field(..., alias="field184", description="")
    field212: float = Field(..., alias="field212")
    field213: float = Field(..., alias="field213")
    field214: float = Field(..., alias="field214")
    field116: AwareDatetime = Field(..., alias="field116", description="")


class Class78(Class51):
    model_type: Literal["Class78"] = "Class78"
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class79(Class51):
    model_type: Literal["Class79"] = "Class79"
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class80(Class51):
    model_type: Literal["Class80"] = "Class80"
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class81(Class51):
    model_type: Literal["Class81"] = "Class81"
    field264: Optional[str] = Field(None, alias="field264", description="")
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class82(Class51):
    model_type: Literal["Class82"] = "Class82"
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class83(Class52):
    model_type: Literal["Class83"] = "Class83"
    field265: Optional[confloat(ge=-90.0, le=90.0)] = Field(0, alias="field265", description="")
    field266: Optional[confloat(ge=-90.0, le=90.0)] = Field(90, alias="field266", description="")


class Class84(Class52):
    model_type: Literal["Class84"] = "Class84"
    field265: Optional[confloat(ge=0.0, le=360.0)] = Field(0, alias="field265", description="")
    field266: Optional[confloat(ge=0.0, le=360.0)] = Field(360, alias="field266", description="")
    field267: Optional[bool] = Field(False, alias="field267", description="")


class Class85(Class52):
    model_type: Literal["Class85"] = "Class85"
    field265: Optional[confloat(ge=-90.0, le=90.0)] = Field(-90, alias="field265", description="")
    field266: Optional[confloat(ge=-90.0, le=90.0)] = Field(90, alias="field266", description="")


class Class86(Class52):
    model_type: Literal["Class86"] = "Class86"
    field268: Optional[confloat(ge=-90.0, le=0.0)] = Field(-6, alias="field268", description="")


class Class87(Class52):
    model_type: Literal["Class87"] = "Class87"


class Class88(Class52):
    model_type: Literal["Class88"] = "Class88"
    field265: confloat(ge=-360.0, le=360.0) = Field(..., alias="field265", description="")
    field266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )
    field269: bool = Field(..., alias="field269", description="")


class Class89(Class52):
    model_type: Literal["Class89"] = "Class89"
    field265: confloat(ge=-360.0, le=360.0) = Field(..., alias="field265", description="")
    field266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )


class Class90(Class52):
    model_type: Literal["Class90"] = "Class90"
    field265: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field265", description=""
    )
    field266: Optional[confloat(ge=-360.0, le=360.0)] = Field(
        None, alias="field266", description=""
    )


class Class91(Class52):
    model_type: Literal["Class91"] = "Class91"
    field270: list[str] = Field(..., alias="field270", description="", min_length=1)


class Class92(Class52):
    model_type: Literal["Class92"] = "Class92"
    field271: list[Class22] = Field(..., alias="field271", description="")


class Class93(Class52):
    model_type: Literal["Class93"] = "Class93"
    field272: list[str] = Field(..., alias="field272", description="", min_length=1)


class Class94(Class52):
    model_type: Literal["Class94"] = "Class94"
    field273: list[Class21] = Field(..., alias="field273", description="")


class Class95(Class52):
    model_type: Literal["Class95"] = "Class95"
    field274: Optional[AwareDatetime] = Field(
        None, alias="field274", description="", examples=["1950-01-01T16:00:00.123Z"]
    )
    field275: AwareDatetime = Field(
        ..., alias="field275", description="", examples=["2120-01-01T16:00:00.123Z"]
    )


class Class96(Class53):
    model_type: Literal["Class96"] = "Class96"
    field224: Optional[Class6] = Field(None, alias="field224")
    field276: Optional[Class72] = None
    field277: Optional[Class109] = Field(None, alias="field277")
    field278: Optional[Class110] = Field(None, alias="field278")
    field184: Optional[Class16] = Field(None, alias="field184", description="")
    field225: float = Field(..., alias="field225", description="", examples=[1.1])
    field279: Optional[float] = Field(None, alias="field279", description="", examples=[1.1])
    field226: float = Field(..., alias="field226", description="", examples=[1.1])
    field280: Optional[float] = Field(None, alias="field280", description="", examples=[1.1])
    field281: Optional[float] = Field(None, alias="field281", description="", examples=[1.1])
    field282: Optional[float] = Field(None, alias="field282", description="", examples=[1.1])
    field283: Optional[list[Class73]] = Field(None, alias="field283")


class Class97(Class53):
    model_type: Literal["Class97"] = "Class97"
    field224: Optional[Class6] = Field(None, alias="field224")
    field284: float = Field(..., alias="field284", description="", examples=[1.1])
    field285: Optional[float] = Field(None, alias="field285", description="", examples=[1.1])
    field286: float = Field(..., alias="field286", description="", examples=[1.1])
    field287: Optional[float] = Field(None, alias="field287", description="", examples=[1.1])
    field281: Optional[float] = Field(None, alias="field281", description="", examples=[1.1])
    field282: Optional[float] = Field(None, alias="field282", description="", examples=[1.1])


class Class98(Class53):
    model_type: Literal["Class98"] = "Class98"
    field174: Optional[Class109] = None
    field288: Optional[float] = Field(None, alias="field288", description="", examples=[10.0])
    field289: Optional[float] = Field(None, alias="field289", description="", examples=[10.0])
    field290: Optional[float] = Field(None, alias="field290", description="", examples=[10.0])
    field291: Optional[float] = Field(None, alias="field291", description="", examples=[10.0])
    field292: Optional[float] = Field(None, alias="field292", description="", examples=[10.0])
    field293: Optional[float] = Field(None, alias="field293", description="", examples=[10.0])


class Class99(Class54):
    model_type: Literal["Class99"] = "Class99"
    field118: Optional[str] = Field("Missed Observation", description="")


class Class100(Class54):
    model_type: Literal["Class100"] = "Class100"
    field118: Optional[str] = Field("Maneuver Detection", description="")
    field174: AnyClass128


class Class101(Class54):
    model_type: Literal["Class101"] = "Class101"
    field118: Optional[str] = Field("New Launch", description="")


class Class102(Class54):
    model_type: Literal["Class102"] = "Class102"
    field118: Optional[str] = Field("Deployment", description="")
    field294: Optional[int] = Field(None, description="")


class Class103(Class54):
    model_type: Literal["Class103"] = "Class103"
    field118: Optional[str] = Field("Articulation", description="")
    field170: str = Field(..., description="")


class Class104(Class54):
    model_type: Literal["Class104"] = "Class104"
    field118: Optional[str] = Field("Orientation Change", description="")
    field295: Optional[float] = Field(None, alias="field295")
    field296: Optional[float] = Field(None, alias="field296")
    field297: Optional[float] = Field(None, alias="field297")


class Class105(Class54):
    model_type: Literal["Class105"] = "Class105"
    field118: Optional[str] = Field("Transmission", description="")
    field298: bool = Field(..., alias="field298", description="")
    field299: Optional[bool] = Field(None, alias="field299", description="")
    field300: Optional[float] = Field(None, alias="field300")
    field301: Optional[float] = Field(None, alias="field301")
    field302: Optional[float] = Field(None, alias="field302", description="")
    field303: Optional[float] = Field(None, alias="field303", description="")


class Class106(Class54):
    model_type: Literal["Class106"] = "Class106"
    field118: Optional[str] = Field("Breakup Event", description="")
    field304: Optional[bool] = Field(None, alias="field304", description="")
    field305: Optional[bool] = Field(None, alias="field305", description="")


class Class107(Class55):
    model_type: Literal["Class107"] = "Class107"
    field198: Optional[Class8] = Field("LIGHT", alias="field198")
    field306: Optional[str] = Field(
        None, alias="field306", description="", examples=["OPEN or BLUE"]
    )
    field307: int = Field(..., alias="field307", examples=[6])
    field234: float = Field(..., alias="field234", description="")
    field308: Optional[float] = Field(None, alias="field308", description="", examples=[15.0])
    field309: Optional[int] = Field(None, description="", examples=[4])
    field310: Class4 = Field(..., alias="field310")


class Class108(Class55):
    model_type: Literal["Class108"] = "Class108"
    field311: Optional[float] = Field(None, alias="field311", description="")


class Class109(Class56):
    model_type: Literal["Class109"] = "Class109"
    field312: Optional[Class70] = Field(None, alias="field312")
    field313: Optional[list[Class72]] = Field(None, alias="field313")
    field314: Class32 = Field(..., alias="field314")
    field315: Class96
    field316: Optional[Class98] = Field(None, alias="field316")
    field107: constr(min_length=1, max_length=36) = Field(
        ..., description="", examples=["Bluestaq"]
    )


class Class110(Class56):
    model_type: Literal["Class110"] = "Class110"
    field315: Class96


class Class111(Class57):
    model_type: Literal["Class111"] = "Class111"
    field317: float = Field(..., alias="field317", description="", examples=[1.0])
    field318: float = Field(..., alias="field318", description="", examples=[30.0])
    field319: float = Field(..., alias="field319", description="", examples=[20.0])
    field320: float = Field(..., alias="field320", description="")
    field321: float = Field(..., alias="field321", description="")
    field322: float = Field(..., alias="field322", description="")
    field323: Optional[list[Class70]] = Field(None, alias="field323")
    field185: list[AnyClass131] = Field(..., alias="field185", description="")


class Class112(Class57):
    model_type: Literal["Class112"] = "Class112"
    field320: float = Field(..., alias="field320", description="")
    field321: float = Field(..., alias="field321", description="")
    field322: float = Field(..., alias="field322", description="")
    field317: float = Field(..., alias="field317", description="", examples=[1.0])
    field318: float = Field(..., alias="field318", description="", examples=[30.0])
    field319: float = Field(..., alias="field319", description="", examples=[20.0])
    field324: Optional[float] = Field(None, alias="field324", description="", examples=[0.01])
    field325: Optional[float] = Field(None, alias="field325", description="", examples=[0.01])


class Class113(Class57):
    model_type: Literal["Class113"] = "Class113"
    field320: float = Field(..., alias="field320", description="")
    field321: float = Field(..., alias="field321", description="")
    field322: float = Field(..., alias="field322", description="")
    field317: float = Field(..., alias="field317", description="", examples=[1.0])
    field318: float = Field(..., alias="field318", description="", examples=[30.0])
    field319: float = Field(..., alias="field319", description="", examples=[20.0])
    field324: Optional[float] = Field(None, alias="field324", description="", examples=[0.01])
    field325: Optional[float] = Field(None, alias="field325", description="", examples=[0.01])
    field326: Optional[bool] = Field(None, alias="field326", description="")


class Class114(Class58):
    model_type: Literal["Class114"] = "Class114"
    field327: Optional[int] = Field(0, alias="field327", description="")
    field328: Optional[list[str]] = Field(None, alias="field328")
    field329: Optional[float] = Field(None, alias="field329", description="")
    field330: Optional[float] = Field(None, alias="field330")
    field331: Optional[float] = Field(None, alias="field331")
    field332: Optional[float] = Field(None, alias="field332")
    field333: Optional[float] = Field(None, alias="field333")
    field334: Optional[float] = Field(None, alias="field334", description="", examples=[4.0])
    field335: Optional[float] = Field(None, alias="field335", description="", examples=[4.0])
    field336: Optional[float] = Field(None, alias="field336", examples=[200.0])
    field337: Optional[float] = Field(None, alias="field337", description="", examples=[4.0])
    field338: Optional[confloat(ge=0.0)] = Field(
        None, alias="field338", description="", examples=[1e-06]
    )
    field339: Optional[float] = Field(None, alias="field339", description="", examples=[3600.0])
    field340: Optional[float] = Field(None, alias="field340", description="", examples=[4.0])
    field341: Optional[float] = Field(None, alias="field341", description="", examples=[1])
    field342: float = Field(..., alias="field342", description="", examples=[3.0])
    field343: Optional[float] = Field(None, alias="field343", description="", examples=[700.0])
    field344: Optional[float] = Field(None, alias="field344", description="", examples=[5.0])
    field345: Optional[float] = Field(None, alias="field345", examples=[1.0])
    field346: Optional[float] = Field(None, alias="field346", description="", examples=[10.0])
    field347: Optional[bool] = Field(False, alias="field347", description="")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class115(Class58):
    model_type: Literal["Class115"] = "Class115"
    field329: Optional[float] = Field(None, alias="field329", description="")
    field330: Optional[float] = Field(None, alias="field330")
    field331: Optional[float] = Field(None, alias="field331")
    field332: Optional[float] = Field(None, alias="field332")
    field333: Optional[float] = Field(None, alias="field333")
    field334: Optional[float] = Field(None, alias="field334", description="", examples=[4.0])
    field336: Optional[float] = Field(None, alias="field336", examples=[200.0])
    field338: Optional[float] = Field(None, alias="field338", description="", examples=[1e-06])
    field339: Optional[float] = Field(None, alias="field339", description="", examples=[3600.0])
    field341: Optional[float] = Field(None, alias="field341", description="", examples=[1])
    field342: float = Field(..., alias="field342", description="", examples=[3.0])
    field348: Optional[float] = Field(None, alias="field348", description="", examples=[420.0])
    field349: Optional[float] = Field(None, alias="field349", description="", examples=[870.0])
    field343: Optional[float] = Field(None, alias="field343", description="", examples=[700.0])
    field344: Optional[float] = Field(None, alias="field344", description="", examples=[5.0])
    field345: Optional[float] = Field(None, alias="field345", examples=[1.0])
    field350: Optional[float] = Field(None, description="", examples=[1])
    field351: Optional[float] = Field(None, alias="field351", description="")
    field347: Optional[bool] = Field(False, alias="field347", description="")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class116(Class58):
    model_type: Literal["Class116"] = "Class116"
    field329: Optional[float] = Field(None, alias="field329", description="")
    field330: Optional[float] = Field(None, alias="field330")
    field331: Optional[float] = Field(None, alias="field331")
    field332: Optional[float] = Field(None, alias="field332")
    field333: Optional[float] = Field(None, alias="field333")
    field334: Optional[float] = Field(None, alias="field334", description="", examples=[4.0])
    field336: Optional[float] = Field(None, alias="field336", examples=[200.0])
    field338: Optional[float] = Field(None, alias="field338", description="", examples=[1e-06])
    field339: Optional[float] = Field(None, alias="field339", description="", examples=[3600.0])
    field341: Optional[float] = Field(None, alias="field341", description="", examples=[1])
    field342: float = Field(..., alias="field342", description="", examples=[3.0])
    field348: Optional[float] = Field(None, alias="field348", description="", examples=[420.0])
    field349: Optional[float] = Field(None, alias="field349", description="", examples=[870.0])
    field343: Optional[float] = Field(None, alias="field343", description="", examples=[700.0])
    field344: Optional[float] = Field(None, alias="field344", description="", examples=[5.0])
    field345: Optional[float] = Field(None, alias="field345", examples=[1.0])
    field350: Optional[float] = Field(None, description="", examples=[1])
    field351: Optional[float] = Field(None, alias="field351", description="", examples=[16.0])
    field352: Optional[list[bool]] = Field(
        None, alias="field352", description="", max_length=4, min_length=4
    )
    field347: Optional[bool] = Field(False, alias="field347", description="")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class117(Class58):
    model_type: Literal["Class117"] = "Class117"
    field342: float = Field(..., alias="field342", description="", examples=[3.0])
    field353: Optional[float] = Field(None, alias="field353", description="")
    field354: Optional[float] = Field(None, alias="field354", description="")
    field355: Optional[float] = Field(None, alias="field355", description="")
    field356: Optional[float] = Field(None, alias="field356", description="")
    field357: Optional[float] = Field(None, alias="field357", description="")
    field176: Optional[float] = Field(None, alias="field176", description="")
    field358: Optional[list[confloat(ge=0.0, le=360.0)]] = Field(
        None, alias="field358", description=""
    )
    field359: Optional[list[confloat(ge=0.0, le=360.0)]] = Field(
        None, alias="field359", description=""
    )
    field360: Optional[int] = Field(None, alias="field360", description="")
    field361: Optional[str] = Field(None, alias="field361", description="", examples=["cf32_le"])
    field362: Optional[list[str]] = Field(None, alias="field362", description="")
    field363: Optional[float] = Field(None, alias="field363", description="")
    field364: Optional[list[Class24]] = Field(None, alias="field364", description="")
    field365: Optional[float] = Field(None, alias="field365", description="")
    field201: Optional[list[Class24]] = Field(None, alias="field201", description="")


class Class118(Class59):
    model_type: Literal["Class118"] = "Class118"
    field366: Class16 = Field(..., alias="field366")
    field367: list[Class65] = Field(..., alias="field367", description="", min_length=1)


class Class119(Class59):
    model_type: Literal["Class119"] = "Class119"
    field224: Class6 = Field(..., alias="field224")
    field368: list[Class68] = Field(..., alias="field368", description="")


class Class120(Class59):
    model_type: Literal["Class120"] = "Class120"
    field369: Optional[constr(min_length=0, max_length=69)] = Field(
        None, description="", examples=["0 Galaxy 15"]
    )
    field370: constr(min_length=0, max_length=69) = Field(
        ...,
        description="",
        examples=["1 28884U 05041A   23120.48400991  .00000122  00000-0  00000-0 0  9998"],
    )
    field371: constr(min_length=0, max_length=69) = Field(
        ...,
        description="",
        examples=["2 28884   0.6218  91.7729 0002021 322.8147 190.2545  0.99731372 64126"],
    )


class Class121(Class107):
    model_type: Literal["Class121"] = "Class121"
    field372: Optional[conint(ge=0, le=2)] = Field(0, alias="field372", description="")
    field373: Optional[conint(ge=0, le=2)] = Field(0, alias="field373", description="")
    field374: Optional[conint(ge=0, le=1)] = Field(0, alias="field374", description="")
    field375: Optional[conint(ge=0, le=2)] = Field(0, alias="field375", description="")
    field376: Optional[confloat(ge=0.0, le=600.0)] = Field(0.0, alias="field376", description="")
    field377: Optional[conint(ge=1, le=99)] = Field(1, alias="field377", description="")
    field378: Optional[conint(ge=0, le=64)] = Field(0, alias="field378", description="")
    field379: Optional[conint(ge=0, le=1)] = Field(1, alias="field379", description="")
    field380: Optional[conint(ge=0, le=1)] = Field(0, alias="field380", description="")
    field381: Optional[conint(ge=0, le=1)] = Field(0, alias="field381", description="")
    field382: Optional[conint(ge=0, le=1)] = Field(0, alias="field382", description="")
    field383: Optional[conint(ge=0, le=1)] = Field(0, alias="field383", description="")
    field384: Optional[conint(ge=0, le=1)] = Field(0, alias="field384", description="")
    field385: Optional[conint(ge=0, le=1)] = Field(1, alias="field385", description="")
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
    ],
    Field(discriminator="model_type"),
]
AnyClass123 = Annotated[
    Union[Class78, Class79, Class80, Class81, Class82], Field(discriminator="model_type")
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
    Field(discriminator="model_type"),
]
AnyClass125 = Annotated[Union[Class96, Class97, Class98], Field(discriminator="model_type")]
AnyClass126 = Annotated[
    Union[Class99, Class100, Class101, Class102, Class103, Class104, Class105, Class106],
    Field(discriminator="model_type"),
]
AnyClass127 = Annotated[Union[Class107, Class121, Class108], Field(discriminator="model_type")]
AnyClass128 = Annotated[Union[Class109, Class110], Field(discriminator="model_type")]
AnyClass129 = Annotated[
    Union[Class74, Class75, Class76, Class77], Field(discriminator="model_type")
]
AnyClass130 = Annotated[Union[Class111, Class112, Class113], Field(discriminator="model_type")]
AnyClass131 = Annotated[
    Union[Class114, Class115, Class116, Class117], Field(discriminator="model_type")
]
AnyClass132 = Annotated[Union[Class118, Class119, Class120], Field(discriminator="model_type")]
Class35.model_rebuild()
Class36.model_rebuild()
Class37.model_rebuild()
Class38.model_rebuild()
Class39.model_rebuild()
Class40.model_rebuild()
Class41.model_rebuild()
Class42.model_rebuild()
Class43.model_rebuild()
Class44.model_rebuild()
Class45.model_rebuild()
Class46.model_rebuild()
Class47.model_rebuild()
Class48.model_rebuild()
Class49.model_rebuild()
Class50.model_rebuild()
Class51.model_rebuild()
Class52.model_rebuild()
Class53.model_rebuild()
Class54.model_rebuild()
Class55.model_rebuild()
Class56.model_rebuild()
Class57.model_rebuild()
Class58.model_rebuild()
Class59.model_rebuild()
Class60.model_rebuild()
Class61.model_rebuild()
Class62.model_rebuild()
Class63.model_rebuild()
Class64.model_rebuild()
Class65.model_rebuild()
Class67.model_rebuild()
Class66.model_rebuild()
Class68.model_rebuild()
Class69.model_rebuild()
Class70.model_rebuild()
Class71.model_rebuild()
Class72.model_rebuild()
Class73.model_rebuild()
Class74.model_rebuild()
Class75.model_rebuild()
Class76.model_rebuild()
Class77.model_rebuild()
Class78.model_rebuild()
Class79.model_rebuild()
Class80.model_rebuild()
Class81.model_rebuild()
Class82.model_rebuild()
Class83.model_rebuild()
Class84.model_rebuild()
Class85.model_rebuild()
Class86.model_rebuild()
Class87.model_rebuild()
Class88.model_rebuild()
Class89.model_rebuild()
Class90.model_rebuild()
Class91.model_rebuild()
Class92.model_rebuild()
Class93.model_rebuild()
Class94.model_rebuild()
Class95.model_rebuild()
Class96.model_rebuild()
Class97.model_rebuild()
Class98.model_rebuild()
Class99.model_rebuild()
Class100.model_rebuild()
Class101.model_rebuild()
Class102.model_rebuild()
Class103.model_rebuild()
Class104.model_rebuild()
Class105.model_rebuild()
Class106.model_rebuild()
Class107.model_rebuild()
Class108.model_rebuild()
Class109.model_rebuild()
Class110.model_rebuild()
Class111.model_rebuild()
Class112.model_rebuild()
Class113.model_rebuild()
Class114.model_rebuild()
Class115.model_rebuild()
Class116.model_rebuild()
Class117.model_rebuild()
Class118.model_rebuild()
Class119.model_rebuild()
Class120.model_rebuild()
Class121.model_rebuild()
