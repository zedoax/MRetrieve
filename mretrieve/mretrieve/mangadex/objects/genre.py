from enum import Enum, unique


@unique
class Genre(Enum):
    ACTION = 2
    ADVENTURE = 3
    AWARD_WINNING = 4
    COMEDY = 5
    COOKING = 6
    DOUJINSHI = 7
    DRAMA = 8
    ECCHI = 9
    FANTASY = 10
    GENDER_BENDER = 11
    HAREM = 12
    HISTORICAL = 13
    HORROR = 14
    JOSEI = 15
    MARTIAL_ARTS = 16
    MECHA = 17
    MEDICAL = 18
    MUSIC = 19
    MYSTERY = 20
    ONESHOT = 21
    PSYCHOLOGICAL = 22
    ROMANCE = 23
    SCHOOL_LIFE = 24
    SCI_FI = 25
    SEINEN = 26
    SHOUJO = 27
    SHOUJO_AI = 28
    SHOUNEN = 29
    SHOUNEN_AI = 30
    SLICE_OF_LIFE = 31
    SMUT = 32
    SPORTS = 33
    SUPERNATURAL = 34
    TRAGEDY = 35
    WEBTOON = 36
    YAOI = 37
    YURI = 38
    GAME = 40
    ISEKAI = 41
