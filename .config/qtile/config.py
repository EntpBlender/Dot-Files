# ________  ________  ________  ________      ___    ___ ________ ___   ___  _________   
#|\   ____\|\   __  \|\   __  \|\_____  \    |\  \  /  /|\   ____\\  \ |\  \|\___   ___\ 
#\ \  \___|\ \  \|\  \ \  \|\  \\|___/  /|   \ \  \/  / | \  \___\ \  \\_\  \|___ \  \_| 
# \ \  \    \ \   _  _\ \   __  \   /  / /    \ \    / / \ \  \   \ \______  \   \ \  \  
#  \ \  \____\ \  \\  \\ \  \ \  \ /  /_/__    \/  /  /   \ \  \___\|_____|\  \   \ \  \ 
#   \ \_______\ \__\\ _\\ \__\ \__\\________\__/  / /      \ \_______\    \ \__\   \ \__\
#    \|_______|\|__|\|__|\|__|\|__|\|_______|\___/ /        \|_______|     \|__|    \|__|
#                                           \|___|/                                      
#--------------------------------https://saidneder.tech/--------------------------------                                                                                                                                                                           
# --------------- Qtile Conf ----------------#
# https://docs.qtile.org/en/latest/index.html#

from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"  # Supr key

# Colors
# Purple Theme

focus = "7300e6"  # Purple
dark = "0f101a"
light = "f1ffff"
inactive = "404040"




    # ---------------------------- Startup Apps ----------------------------- #

    #lazy.spawn("dunst"),

    # ----------------------------------------------------------------------- #

keys = [
    # ----------------------- QTILE WINDOW MANAGMENT ------------------------ #

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # ------------------ APPS HOTKEYS --------------------- #

    # Launch Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show run")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -10%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +10%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    #PLAY
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),

    #Next
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

    #Previous
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),

    #Stop
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Screenshot
    Key([], "Print", lazy.spawn("grim")),

    # Web browser
    Key([mod], "f", lazy.spawn("firefox")),

    # Keyboard Layouts
    #    Key([mod], "z", lazy.spawn("setxkbmap ar")),
    Key([mod], "x", lazy.spawn("setxkbmap us")),

    # Toggle Floating
    Key([mod, "shift"], "a", lazy.window.toggle_floating()),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 4000k")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Discord
    Key([mod], "d", lazy.spawn("discord")),

    # Spotify
    Key([mod], "s", lazy.spawn("spotify")),

    # Pavucontrol
    Key([mod], "p", lazy.spawn("pavucontrol")),

    # Nemo
    Key([mod], "n", lazy.spawn("nemo")),

    # VSCode
    Key([mod], "a", lazy.spawn("code /Documents/Programming")),

    # Lock Screen
    Key([mod, "control"], "l", lazy.spawn("betterlockscreen -l")),

    # BoostNote
    Key([mod], "b", lazy.spawn("boostnote")),

]

# 1 = Firefox | 2 = Terminal | 3 = Programming | 4 = File Explorer | 5 = Discord | 6 = Spotify | 7 = School #

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", " ﭮ ", " 阮 ", "  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# Preferred Layouts = MonadTall | Matrix | Max (In order of usage)


layout_conf = {
    "border_focus": focus,
    "margin": 5,
    "border_width": 2
}

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.MonadTall(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(**layout_conf),
    layout.Max(),
    # layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Font
font = "Hack Nerd Font"

widget_defaults = dict(
    font=font,
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Widgets

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font=font,
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=light,
                    inactive=inactive,
                    rounded=False,
                    highlight_method="block",
                    urgent_alert_method="block",
                    urgent_border=dark,
                    this_current_screen_border=focus,
                    this_screen_border=dark,
                    other_current_screen_border=dark,
                    other_screen_border=dark,
                    disable_drag=True
                ),
                widget.WindowName(fontsize=14, foreground=focus),
                widget.Systray(),
                # widget.KeyboardLayout(
                #    configured_keyboards=["us", "es olpc"],
                #    display_map={"us": "us", "es olpc": "es"}
                #),
                widget.Battery(format='{char} {percent:2.0%}', padding=5),
                widget.Volume(padding=5),        
                widget.Spacer(length=5),
                widget.CurrentLayout(),
                widget.Clock(
                    format="%m-%d %I:%M %p",
                    padding=5
                ),
            ],
            24,
            opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    # gitk
    Match(
        wm_class='confirmreset'),
    # gitk
    Match(
        wm_class='makebranch'),
    # gitk
    Match(
        wm_class='maketag'),
    # ssh-askpass
    Match(
        wm_class='ssh-askpass'),
    # gitk
    Match(
        title='branchdialog'),
    # GPG key password entry
    Match(
        title='pinentry'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

