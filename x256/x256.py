#!/usr/bin/env python
from math import sqrt as _sqrt
from sys import stdout as _stdout


def __hex2rgb(hexa):
    r = int(hexa[0:2], 16)
    g = int(hexa[2:4], 16)
    b = int(hexa[4:6], 16)
    return [r, g, b]


def __rgb2hex(rgb):
    return "%.2X%.2X%.2X" % (rgb[0], rgb[1], rgb[2])


colors = list(map(__hex2rgb, [
    "000000", "800000", "008000", "808000", "000080", "800080", "008080", "c0c0c0",
    "808080", "ff0000", "00ff00", "ffff00", "0000ff", "ff00ff", "00ffff", "ffffff",
    "000000", "00005f", "000087", "0000af", "0000d7", "0000ff", "005f00", "005f5f",
    "005f87", "005faf", "005fd7", "005fff", "008700", "00875f", "008787", "0087af",
    "0087d7", "0087ff", "00af00", "00af5f", "00af87", "00afaf", "00afd7", "00afff",
    "00d700", "00d75f", "00d787", "00d7af", "00d7d7", "00d7ff", "00ff00", "00ff5f",
    "00ff87", "00ffaf", "00ffd7", "00ffff", "5f0000", "5f005f", "5f0087", "5f00af",
    "5f00d7", "5f00ff", "5f5f00", "5f5f5f", "5f5f87", "5f5faf", "5f5fd7", "5f5fff",
    "5f8700", "5f875f", "5f8787", "5f87af", "5f87d7", "5f87ff", "5faf00", "5faf5f",
    "5faf87", "5fafaf", "5fafd7", "5fafff", "5fd700", "5fd75f", "5fd787", "5fd7af",
    "5fd7d7", "5fd7ff", "5fff00", "5fff5f", "5fff87", "5fffaf", "5fffd7", "5fffff",
    "870000", "87005f", "870087", "8700af", "8700d7", "8700ff", "875f00", "875f5f",
    "875f87", "875faf", "875fd7", "875fff", "878700", "87875f", "878787", "8787af",
    "8787d7", "8787ff", "87af00", "87af5f", "87af87", "87afaf", "87afd7", "87afff",
    "87d700", "87d75f", "87d787", "87d7af", "87d7d7", "87d7ff", "87ff00", "87ff5f",
    "87ff87", "87ffaf", "87ffd7", "87ffff", "af0000", "af005f", "af0087", "af00af",
    "af00d7", "af00ff", "af5f00", "af5f5f", "af5f87", "af5faf", "af5fd7", "af5fff",
    "af8700", "af875f", "af8787", "af87af", "af87d7", "af87ff", "afaf00", "afaf5f",
    "afaf87", "afafaf", "afafd7", "afafff", "afd700", "afd75f", "afd787", "afd7af",
    "afd7d7", "afd7ff", "afff00", "afff5f", "afff87", "afffaf", "afffd7", "afffff",
    "d70000", "d7005f", "d70087", "d700af", "d700d7", "d700ff", "d75f00", "d75f5f",
    "d75f87", "d75faf", "d75fd7", "d75fff", "d78700", "d7875f", "d78787", "d787af",
    "d787d7", "d787ff", "d7af00", "d7af5f", "d7af87", "d7afaf", "d7afd7", "d7afff",
    "d7d700", "d7d75f", "d7d787", "d7d7af", "d7d7d7", "d7d7ff", "d7ff00", "d7ff5f",
    "d7ff87", "d7ffaf", "d7ffd7", "d7ffff", "ff0000", "ff005f", "ff0087", "ff00af",
    "ff00d7", "ff00ff", "ff5f00", "ff5f5f", "ff5f87", "ff5faf", "ff5fd7", "ff5fff",
    "ff8700", "ff875f", "ff8787", "ff87af", "ff87d7", "ff87ff", "ffaf00", "ffaf5f",
    "ffaf87", "ffafaf", "ffafd7", "ffafff", "ffd700", "ffd75f", "ffd787", "ffd7af",
    "ffd7d7", "ffd7ff", "ffff00", "ffff5f", "ffff87", "ffffaf", "ffffd7", "ffffff",
    "080808", "121212", "1c1c1c", "262626", "303030", "3a3a3a", "444444", "4e4e4e",
    "585858", "606060", "666666", "767676", "808080", "8a8a8a", "949494", "9e9e9e",
    "a8a8a8", "b2b2b2", "bcbcbc", "c6c6c6", "d0d0d0", "dadada", "e4e4e4", "eeeeee"
]))

html_color_table = {
    'indigo': '4B0082',
	'gold': 'FFD700',
	'firebrick': 'B22222',
	'indianred': 'CD5C5C',
	'yellow': 'FFFF00',
	'darkolivegreen': '556B2F',
	'darkseagreen': '8FBC8F',
	'mediumvioletred': 'C71585',
	'mediumorchid': 'BA55D3',
	'chartreuse': '7FFF00',
	'mediumslateblue': '7B68EE',
	'black': '000000',
	'springgreen': '00FF7F',
	'crimson': 'DC143C',
	'lightsalmon': 'FFA07A',
	'brown': 'A52A2A',
	'turquoise': '40E0D0',
	'olivedrab': '6B8E23',
	'cyan': '00FFFF',
	'silver': 'C0C0C0',
	'skyblue': '87CEEB',
	'gray': '808080',
	'darkturquoise': '00CED1',
	'goldenrod': 'DAA520',
	'darkgreen': '006400',
	'darkviolet': '9400D3',
	'darkgray': 'A9A9A9',
	'lightpink': 'FFB6C1',
	'teal': '008080',
	'darkmagenta': '8B008B',
	'lightgoldenrodyellow': 'FAFAD2',
	'lavender': 'E6E6FA',
	'yellowgreen': '9ACD32',
	'thistle': 'D8BFD8',
	'violet': 'EE82EE',
	'navy': '000080',
	'orchid': 'DA70D6',
	'blue': '0000FF',
	'ghostwhite': 'F8F8FF',
	'honeydew': 'F0FFF0',
	'cornflowerblue': '6495ED',
	'darkblue': '00008B',
	'darkkhaki': 'BDB76B',
	'mediumpurple': '9370DB',
	'cornsilk': 'FFF8DC',
	'red': 'FF0000',
	'bisque': 'FFE4C4',
	'slategray': '708090',
	'darkcyan': '008B8B',
	'khaki': 'F0E68C',
	'wheat': 'F5DEB3',
	'deepskyblue': '00BFFF',
	'darkred': '8B0000',
	'steelblue': '4682B4',
	'aliceblue': 'F0F8FF',
	'gainsboro': 'DCDCDC',
	'mediumturquoise': '48D1CC',
	'floralwhite': 'FFFAF0',
	'coral': 'FF7F50',
	'purple': '800080',
	'aqua': '00FFFF',
	'lightcyan': 'E0FFFF',
	'darksalmon': 'E9967A',
	'beige': 'F5F5DC',
	'azure': 'F0FFFF',
	'lightsteelblue': 'B0C4DE',
	'oldlace': 'FDF5E6',
	'greenyellow': 'ADFF2F',
	'royalblue': '4169E1',
	'lightseagreen': '20B2AA',
	'mistyrose': 'FFE4E1',
	'sienna': 'A0522D',
	'lightcoral': 'F08080',
	'orangered': 'FF4500',
	'navajowhite': 'FFDEAD',
	'lime': '00FF00',
	'palegreen': '98FB98',
	'burlywood': 'DEB887',
	'seashell': 'FFF5EE',
	'mediumspringgreen': '00FA9A',
	'fuchsia': 'FF00FF',
	'papayawhip': 'FFEFD5',
	'blanchedalmond': 'FFEBCD',
	'peru': 'CD853F',
	'aquamarine': '7FFFD4',
	'white': 'FFFFFF',
	'darkslategray': '2F4F4F',
	'tomato': 'FF6347',
	'ivory': 'FFFFF0',
	'dodgerblue': '1E90FF',
	'lemonchiffon': 'FFFACD',
	'chocolate': 'D2691E',
	'orange': 'FFA500',
	'forestgreen': '228B22',
	'slateblue': '6A5ACD',
	'olive': '808000',
	'mintcream': 'F5FFFA',
	'antiquewhite': 'FAEBD7',
	'darkorange': 'FF8C00',
	'cadetblue': '5F9EA0',
	'moccasin': 'FFE4B5',
	'limegreen': '32CD32',
	'saddlebrown': '8B4513',
	'darkslateblue': '483D8B',
	'lightskyblue': '87CEFA',
	'deeppink': 'FF1493',
	'plum': 'DDA0DD',
	'darkgoldenrod': 'B8860B',
	'maroon': '800000',
	'sandybrown': 'F4A460',
	'magenta': 'FF00FF',
	'tan': 'D2B48C',
	'rosybrown': 'BC8F8F',
	'pink': 'FFC0CB',
	'lightblue': 'ADD8E6',
	'palevioletred': 'DB7093',
	'mediumseagreen': '3CB371',
	'dimgray': '696969',
	'powderblue': 'B0E0E6',
	'seagreen': '2E8B57',
	'snow': 'FFFAFA',
	'mediumblue': '0000CD',
	'midnightblue': '191970',
	'paleturquoise': 'AFEEEE',
	'palegoldenrod': 'EEE8AA',
	'whitesmoke': 'F5F5F5',
	'darkorchid': '9932CC',
	'salmon': 'FA8072',
	'lightslategray': '778899',
	'lawngreen': '7CFC00',
	'lightgreen': '90EE90',
	'lightgray': 'D3D3D3',
	'hotpink': 'FF69B4',
	'lightyellow': 'FFFFE0',
	'lavenderblush': 'FFF0F5',
	'linen': 'FAF0E6',
	'mediumaquamarine': '66CDAA',
	'green': '008000',
	'blueviolet': '8A2BE2',
	'peachpuff': 'FFDAB9'}

def __distance(a, b):
    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2
    z = (a[2] - b[2]) ** 2
    return _sqrt(x + y + z)


def from_rgb(r, g=None, b=None):
    """
    Return the nearest xterm 256 color code from rgb input.
    """
    c = r if isinstance(r, list) else [r, g, b]
    best = {}

    for index, item in enumerate(colors):
        d = __distance(item, c)
        if(not best or d <= best['distance']):
            best = {'distance': d, 'index': index}

    if 'index' in best:
        return best['index']
    else:
        return 1


def from_hex(h):
    """
    Return the nearest xterm 256 color code from hex input.
    """
    return from_rgb(__hex2rgb(h))


def from_html_color_name(h):
    """
    Return the nearset xterm 256 color code form html color name.

    It returns False when the specific color name was not found.
    """
    if h.lower() not in html_color_table:
        return False
    return from_hex(html_color_table[h.lower()])


def to_rgb(i):
    """
    Return rgb from xterm 256 color code.
    """
    return colors[i]


def to_hex(i):
    """
    Return hex color from xterm 256 color code.
    """
    return __rgb2hex(colors[i])

def _set_color(opt, color, stream):
    if stream == None:
        stream = _stdout
    stream.write('\x1b[%d;5;%dm' % (opt, color))


def set_fore_color(color, stream = None):
    """
    Set fore color for specific stream
    """
    _set_color(38, color, stream)


def set_back_color(color, stream = None):
    """
    Set background color for specific stream
    """
    _set_color(48, color, stream)

def reset_color(stream = None):
    """
    Reset colors to normal
    """
    _set_color(39, 0, stream)
    _set_color(49, 0, stream)

def _hi_contrast(r, g = None, b = None):
    r = r if isinstance(r, list) else [r, g, b]
    return [0, 0, 0] if sum(r) > 128 * 3 else [255, 255, 255]

if __name__ == "__main__":
    fore = from_rgb(220, 40, 90)
    back = from_rgb(120, 180, 210)
    set_fore_color(fore)
    set_back_color(back)
    _stdout.write("Colorful Text!!")
    reset_color()
    _stdout.write("  And the normal one....\n")

    i = 0
    for c in colors:
        set_back_color(from_rgb(c))
        set_fore_color(from_rgb(_hi_contrast(c)))
        _stdout.write(" %.2X " % i)
        i += 1
        if i == 16:
            reset_color()
            _stdout.write("\n")
        elif i > 16:
            k = i - 16
            if k % 12 == 0:
                reset_color()
                _stdout.write("\n")
    reset_color()
