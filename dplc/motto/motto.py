import argparse
from dplc.utils import md5_encoding


def verifyMotto(P: argparse.Namespace):
    name = P.name
    motto = P.motto
    is_verified = False
    if name == "DPTechnology":
        is_verified = verifyMottoDPTechnology(motto)
    elif name == "YuzhiZhang":
        is_verified = verifyMottoYuzhiZhang(motto)
    elif name == "MaohuaYang":
        is_verified = verifyMottoMaohuaYang(motto)
    elif name == "YannanYuan":
        is_verified = verifyMottoYannanYuan(motto)
    elif name == "YiboWang":
        is_verified = verifyMottoYiboWang(motto)
    elif name == "YuhangWang":
        is_verified = verifyMottoYuhangWang(motto)
    elif name == "QiangqiangGu":
        is_verified = verifyMottoQiangqiangGu(motto)
    else:
        assert RuntimeError("Your input name is not valid for this test!")

    if is_verified:
        print(f"Your input '{motto}' matches with {name}'s motto! ")
    else:
        print(f"Your input '{motto}' doesn't match with {name}'s motto! ")


def verifyMottoDPTechnology(public_string: str) -> bool:
    '''

    Verify if a public string is DP Technology's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    is_verified: bool, if the string matches with DP Technology's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "79538b12f0c2b23fb317141a6eb3e16d":
        is_verified = True
    return is_verified


def verifyMottoYuzhiZhang(public_string: str) -> bool:
    '''

    Verify if a public string is Yuzhi Zhang's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    is_verified: bool, if the string matches with Yuzhi Zhang's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "dbe7f4e7f8587bc7a538e2299142add7":
        is_verified = True
    return is_verified


def verifyMottoMaohuaYang(public_string: str) -> bool:
    '''

    Verify if a public string is Maohua Yang's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    is_verified: bool, if the string matches with Maohua Yang's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "c6d3560f21ddd7a4cca224ebcf7e6aa0":
        is_verified = True
    return is_verified


def verifyMottoYannanYuan(public_string: str) -> bool:
    '''

    Verify if a public string is Yannan Yuan's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    Verify if a public string is Yannan Yuan's motto.
    is_verified: bool, if the string matches with Yannan Yuan's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "a700cadc676620c759a11df2cd06b4c9":
        is_verified = True
    return is_verified


def verifyMottoYiboWang(public_string: str) -> bool:
    '''

    Verify if a public string is Yibo Wang's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    Verify if a public string is Yibo Wang's motto.
    is_verified: bool, if the string matches with Yibo Wang's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "805135ea1c11443d5b0837044ee8b732":
        is_verified = True
    return is_verified


def verifyMottoYuhangWang(public_string: str) -> bool:
    '''

    Verify if a public string is Yuhang Wang's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    True: if the string matches with Yuhang Wang's motto.
    False: otherwise.
    '''
    return md5_encoding(public_string) == "48c9598399fca3a74a1f73a641651a25"


def verifyMottoQiangqiangGu(public_string: str) -> bool:
    '''

    Verify if a public string is Qiangqiang Gu's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    Verify if a public string is Qiangqiang Gu's motto.
    is_verified: bool, if the string matches with Qiangqiang Gu's motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "48f3cb54333cbceda32156f4f2a7dd33":
        is_verified = True
    return is_verified

  
def verifyMottoZixiGan(public_string: str) -> bool:
    '''

    Verify if a public string is Zixi Gan's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    True: if the string matches with Zixi Gan's motto.
    False: otherwise.
    '''
    
    in_md5 = md5_encoding(public_string)
    if in_md5 == "083ecbdb5e5f1fc25aefb501f9b6c6e1":
        return True
    else:
        return False