import pandas as pd
from . import assets
from .models.PlaystationGame import PlaystationGame

try:
    import importlib.resources as ir
except ImportError:
    import importlib_resources as ir

"""
Gets a Playstation Game with the given ID
"""
def find_by_id(game_id) -> PlaystationGame:
    id = str(game_id).upper()
    result = __search_title(id)
    return result


def __check_type_for_known_platforms(id) -> list:
    type = id[0:4]
    result = []
    if __psp_codes(type): result.append("PSP")
    if __psv_codes(type): result.append("PSV")
    if __ps3_codes(type): result.append("PS3")
    if __psx_codes(type): result.append("PSX")
    if __psm_codes(type): result.append("PSM")
    return result


def __search_title(id) -> PlaystationGame:
    platforms_known = __check_type_for_known_platforms(id)
    if len(platforms_known) == 0:
        return None
    for platform in platforms_known:
        result = __find_in_platform(id, platform)
        if result is not None:
            return result


def __find_in_platform(id, platform) -> PlaystationGame:
    file_loc = ir.open_text(assets, f"{platform}_GAMES.tsv")
    df = pd.read_table(file_loc)
    for _, row in df.iterrows():
        if row["Title ID"] == id:
            return PlaystationGame(row["Name"], id, platform)
    return None


def __psv_codes(type) -> bool:
    if(
        type == "PCSG" or
        type == "PCSA" or
        type == "PCSE" or
        type == "PCSC" or
        type == "PCSI" or
        type == "PCSB" or
        type == "PCSF" or
        type == "PCSD" or
        type == "PCSH" or
        type == "NPEA" or
        type == "NPJJ" or
        type == "NPUF"
    ):
        return True


def __psp_codes(type) -> bool:
    if (
        type == "NPUF" or
        type == "NPUG" or
        type == "NPUH" or
        type == "NPUX" or
        type == "NPUZ" or
        type == "UCUS" or
        type == "ULUS" or
        type == "NPJG" or
        type == "NPJH" or
        type == "NPJJ" or
        type == "NPJQ" or
        type == "NPEG" or
        type == "NPEH" or
        type == "NPEX" or
        type == "NPEZ" or
        type == "UCES" or
        type == "ULES" or
        type == "NPHG" or
        type == "NPHH" or
        type == "NPHZ" or
        type == "UCAS" or
        type == "NPEF" or
        type == "PCSB" or
        type == "NPUJ" or
        type == "NPJI"
    ):
        return True


def __ps3_codes(type) -> bool:
    if (
        type == "BCUS" or   
        type == "NPEB" or
        type == "NPJJ" or
        type == "NPUA" or
        type == "NPUB" or
        type == "NPUC" or
        type == "NPUD" or
        type == "NPUF" or
        type == "NPUI" or
        type == "NPUJ" or
        type == "NPUO" or
        type == "NPUP" or
        type == "NPUX" or
        type == "NPUZ" or
        type == "BCJS" or
        type == "BLJM" or
        type == "BLJS" or
        type == "NPJA" or
        type == "NPJB" or
        type == "NPJC" or
        type == "NPJD" or
        type == "NPJQ" or 
        type == "NPJR" or 
        type == "BCES" or 
        type == "BLES" or
        type == "NPEA" or
        type == "NPEC" or 
        type == "NPED" or
        type == "NPEF" or
        type == "NPEJ" or
        type == "NPEL" or 
        type == "NPEP" or 
        type == "BCAS" or
        type == "BLAS" or
        type == "BLUS" or
        type == "NPHA" or
        type == "NPHB" or
        type == "NPHL" or 
        type == "NPHO" or 
        type == "NPHP" or 
        type == "BLET" or
        type == "BCET" or
        type == "NPIA" or 
        type == "NPJI" or
        type == "NPEE" or
        type == "NPKA" or 
        type == "NPHC" or 
        type == "BCJB" or 
        type == "ULUS" or 
        type == "NPJN"
    ):
        return True


def __psx_codes(type) -> bool:
    if(
        type == "NPUH" or
        type == "NPUF" or
        type == "NPUI" or
        type == "NPUJ" or
        type == "NPJI" or
        type == "NPJJ" or
        type == "NPEE" or
        type == "NPEF" or
        type == "NPHB" or
        type == "NPHI" or
        type == "NPHJ"
    ):
        return True


def __psm_codes(type) -> bool:
    if(
        type =="NPNA" or
        type =="NPPA" or
        type =="NPOA" or
        type =="NPQA"
    ):
        return True
