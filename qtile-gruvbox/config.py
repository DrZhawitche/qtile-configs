from __future__ import annotations
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
import re, os, subprocess
from libqtile.widget import base, Spacer 
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from libqtile.dgroups import simple_key_binder

#colors

red 	  =  "#cc241d"
green 	  =  "#98971a"
yellow    =  "#d79921"
blue 	  =  "#458588"
purple    =  "#b16286"
aqua      =  "#689d6a"
gray      =  "#a89984"

red_bright 	     =  "#fb4934"
green_bright	 =  "#b8bb26"
yellow_bright    =  "#fabd2f"
blue_bright      =  "#83a598"
purple_bright    =  "#d3869b"
aqua_bright      =  "#8ec07c"
gray_bright      =  "#928374"

fg    =  "#ebdbb2"
fg0   =  "#fbf1c7"
fg1   =  "#ebdbb2"
fg2   =  "#d5c4a1"   
fg3   =  "#bda393"
fg4   =  "#a89984"

bg      =  "#282828"
bg0_h   =  "#1d2021"
bg0     =  "#282828"
bg0_s   =  "#32301f"
bg1     =  "#3c3836"     
bg2     =  "#504945"
bg3     =  "#665c54"
bg4     =  "#7c6f64"

orange        =  "#d65d0e"
orange_bright =  "#fe9019"

mod = "mod4"
defaultfont = "Cantarell"
terminal = "alacritty"
browser2 = "brave"
browser1 = "librewolf"
ide = "emacs"
file_manager = "thunar"
dmenu = "dmenu_run" + " -sb " + yellow + " -nb " + bg3 + " -p Launch: " + " -fn " + defaultfont
editor_cmd = "alacritty -e vim"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"), # Toggle between split and unsplit sides of stack.  # Split = all windows displayed # Unsplit = 1 window displayed, like Max layout, but still with # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "q", lazy.spawn("archlinux-logout"), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),  
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Toggle minimize"),  
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),  
    # Application launchers
    Key([mod, "shift"], "Return", lazy.spawn(dmenu), desc="Run dmenu"),
    Key([mod, "shift"], "e", lazy.spawn(ide), desc="Open ide gui"),
    Key([mod, "shift"], "v", lazy.spawn(editor_cmd), desc="Open vim in a terminal"),
    Key([mod], "o", lazy.spawn("libreoffice"), desc="Open libreoffice"),
    Key([mod, "shift"], "f", lazy.spawn(file_manager), desc="Open thunar"),
    Key([mod], "w", lazy.spawn(browser1), desc="Open brave"),
    Key([mod, "shift"], "w", lazy.spawn(browser2), desc="Open librewolf"),
    Key([mod, "shift"], "m", lazy.spawn("deadbeef"), desc="Open deadbeef"),
    Key([mod, "shift"], "d", lazy.spawn("webcord"), desc="Open discord"),
    Key([mod], "t", lazy.spawn("sleep 0.1 && xdotool key thorn", shell=True), desc="Type minuscule thorn"),
    Key(["mod1"], "bracketleft", lazy.spawn("sleep 0.1 && xdotool key thorn", shell=True), desc="Type majuscule thorn"),
    Key([mod], "r", lazy.spawn('sleep 0.1 && xdotool type "ƿ"', shell=True), desc="Type majuscule thorn"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch flameshot"),
    #KeyChords
    KeyChord([mod], "e", [
        Key([], "e", lazy.spawn("element-desktop")),
        Key([], "g", lazy.spawn("gdlauncher")),
        Key([], "v", lazy.spawn("alacritty -e vim")),
        Key([], "t", lazy.spawn("transmission-gtk")),
        Key([], "s", lazy.spawn("surf")),

    ]),

    #Special Characters, W.I.P.
    KeyChord([mod], "c", [
        Key([], "t", lazy.spawn("xclip -selection clipboard .local/share/chars/thorn-small.txt")),
        Key([], "T", lazy.spawn("xclip -selection clipboard .local/share/chars/thorn-big.txt")),
    ])
]
groups = [Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns')]

dgroups_key_binder = simple_key_binder("mod4")

layout_defaults = {
        "margin": 5,
        "border_focus": blue_bright,
        "border_normal": bg2,
}

layouts = [
    layout.Columns(
        border_width= 2,
        **layout_defaults
        ),
    layout.Max(**layout_defaults),
     # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_defaults),
    layout.MonadWide(**layout_defaults),
    layout.RatioTile(**layout_defaults),
    layout.Tile(**layout_defaults),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font= defaultfont,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

defaut_font = "Cantarell"

powerline = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(
            path="arrow_right",
            #path=[(0, 0), (1, 0), (0.3, 0.5), (1, 1), (0, 1)], #Variation of the normal left pointing arrow
            padding_y=0,
        )
    ]
}

powerline_left = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(path="arrow_left", padding_y=0)
    ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                background = bg0_h,
                length = 6,   
                ),
                widget.CurrentLayout(
                    foreground = fg1,
                    background = bg0_h,
                    **powerline_left,

                ),
                widget.GroupBox(
                    background = bg0,
                    block_highlight_text_color = yellow_bright,
                    highlight_color = bg2,
                    foreground = fg,
                    inactive = yellow,
                    active = yellow_bright,
                    fontsize = 15,
                    highlight_method='line',
                    urgent_border = orange_bright,
                    this_current_screen_border = yellow_bright,
                    **powerline_left,
                ),
                widget.TaskList(
                    icon_size = 0,
                    background = bg3,
                    foreground = fg1,
                    border = gray,
                    fontsize = 12,
                    **powerline,
                ),
                widget.CPU(
                    font = defaut_font,
                    background = blue,
                    foreground = fg1,
                    padding = 5,
                    **powerline,
                ),
                widget.Memory(
                    background = yellow,
                    measure_mem ='M',
                    foreground = fg1,
                    **powerline,
                ),
                widget.Systray(
                    padding = 5,
                    background = green,
                    foreground = fg1,
                    icon_size = 20,
                ),
                #Spacer is to fix issue with the systray
                widget.Spacer(
                    background = green,
                    length = 1,
                    **powerline,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    padding = 4,
                    background = red,
                    foreground = fg2,
                ),
            ],
            28,
        opacity = 1.0,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = orange_bright,
    border_normal = bg3,
    margin = 5,
    border_width= 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="galculator"),  
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['sh','.config/qtile/autostart.sh'],
        ['swaybg', '-i', '/home/zhawitche/.config/qtile/wallpapers/forest-fog.jpg'],
    ]

    for p in processes:
        subprocess.Popen(p)

@hook.subscribe.startup_once
def _():
    top.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
