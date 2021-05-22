from hata import Color, Embed, Emoji
from random import choice
import os, re


OwO_COLOR = Color.from_html('#FF69B4')
NEKOGIRL_PEEK = Emoji.precreate(os.environ.get('NEKOGIRL_PEEK'))

_str_emojis = [
    "꒰◍ᐡᐤᐡ◍꒱",
    "{ @❛ꈊ❛@ }",
    "6(◦･ω･◦)9",
    "UwU",
    "OwO",
    "@w@",
    "◕w◕"
]

def owo(*, txt: str, ending_emoji: bool = False) -> str:
    """
    `txt`: The text you wish to 'owoify'
    `ending_emoji`: Whether you wish to add an
    emoji at the end of your text to make it 
    especially stand out 
    """

    replacements = {
        r"(?:l|r)": "w",
        r'(?:L|R)': "W",
        r'n([aeiou])': "ny",
        r'N([aeiou])|N(AEIOU)': "Ny",
        r"ove": "uv",
        r'nd(?= |$)': "ndo"
    }

    for pattern, replacement in list(replacements.items()):
        txt = re.sub(pattern=pattern, repl=replacement, string=txt)

    if ending_emoji:
        txt += " " + choice(_str_emojis)

    return txt


@Pichu.interactions(is_global=True)
async def owoify(client, event, text: ('str', 'Please, enter the message OwO')):
    """owoified text"""
    
    return Embed( color=OwO_COLOR).\
        add_field(f"OwOified Text {NEKOGIRL_PEEK:e}", owo(txt=text, ending_emoji=True)).\
        add_footer("purrr!!!")


@Pichu.commands
async def owoify(client, message, text):
    return Embed( color=OwO_COLOR).\
        add_field(f"OwOified Text {NEKOGIRL_PEEK:e}", owo(txt=text, ending_emoji=True)).\
        add_footer("purrr!!!")

