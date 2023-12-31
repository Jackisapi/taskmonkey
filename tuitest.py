import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
    ('banner', 'black', 'dark green'),
    ('streak', 'black', 'black'),
    ('bg', 'black', 'black'), ]

txt = urwid.Text(('banner', u" Hello World "), align='left')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()
