x256
====
*This is a python version from [node-x256](https://github.com/substack/node-x256)*

Return the nearest
[xterm 256 color code](http://www.frexx.de/xterm-256-notes/)
for rgb inputs.


Example
=======

You can just print the index:

    >>> from x256 import x256
    >>> ix = x256.from_rgb(220, 40, 150)
    >>> print ix

output:

    162


or you can use raw ansi escape codes:

	from x256 import x256
    fore = from_rgb(220, 40, 90)
    back = from_rgb(120, 180, 210)
    set_fore_color(fore)
    set_back_color(back)
    _stdout.write('Colorful Text!!')
    reset_color()
    _stdout.write('  And the normal one....')

output:

![x256 test](https://github.com/inndy/python-x256/raw/master/screenshots/x256_test.png)


Methods
=======

    from x256 import x256

x256.from_rgb(red, green, blue)
-------------------------------

Return the nearest xterm 256 color code for the 24-bit `[red, green, blue]`
values.

`red`, `green`, and `blue` should each be integers from 0 through 255,
inclusive.


x256.from_hex(hex)
------------------

Return the nearest xterm 256 color code for the hexadecimal color
values.

`hex` should be string without 0x.


x256.from_html_color_name(name)
-------------------------------

Return the nearset xterm 256 color code form html color name.
It returns `False` when the specific color name was not found.

`name` should be string.


x256.to_rgb(ix)
---------------

Return 24-bit `[red, green, blue]` values from xterm 256 color code.

`ix` should be integer.


x256.to_hex(ix)
---------------

Return hexadecimal color from xterm 256 color code.

`ix` should be integer.


x256.set_fore_color(color[, stream])
----------------------------------

Set fore color for specific stream.

default stream is `sys.stdout`
`color` should be integer


x256.set_back_color(color[, stream])
------------------------------------

Set background color for specific stream.

default stream is `sys.stdout`
`color` should be integer


x256.reset_color([stream])
--------------------------

Reset colors to normal.

default stream is `sys.stdout`


Install
=======

    python setup.py install


License
=======

Copyright (c) 2012 Martin Garcia (newluxfero@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
