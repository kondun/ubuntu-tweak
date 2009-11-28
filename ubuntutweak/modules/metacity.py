#!/usr/bin/python

# Ubuntu Tweak - PyGTK based desktop configure tool
#
# Copyright (C) 2007-2008 TualatriX <tualatrix@gmail.com>
#
# Ubuntu Tweak is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ubuntu Tweak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ubuntu Tweak; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from ubuntutweak.modules  import TweakModule
from ubuntutweak.widgets import ListPack, TablePack
from ubuntutweak.widgets.dialogs import InfoDialog

#TODO
from ubuntutweak.common.factory import WidgetFactory

class Metacity(TweakModule):
    __title__ = _('Window Manager Settings')
    __desc__ = _('Some options about Metacity Window Manager')
    __icon__ = 'preferences-system-windows'
    __url__ = 'http://ubuntu-tweak.com'
    __category__ = 'desktop'
    __desktop__ = 'gnome'

    def __init__(self):
        TweakModule.__init__(self)

        box = TablePack(_('Window Decorate Effect'), (
                    WidgetFactory.create('GconfCheckButton',
                                          label=_('Use Metacity window theme'),
                                          key='use_metacity_theme'),
                    WidgetFactory.create('GconfCheckButton',
                                          label=_('Enable active window transparency'),
                                          key='metacity_theme_active_shade_opacity'),
                    WidgetFactory.create('GconfScale',
                                          label=_('Active window transparency level'),
                                          key='metacity_theme_active_opacity',
                                          min=0, max=1, digits=2),
                    WidgetFactory.create('GconfCheckButton',
                                          label=_('Enable inactive window transparency'),
                                          key='metacity_theme_shade_opacity'),
                    WidgetFactory.create('GconfScale',
                                          label=_('Inactive window shade transparency level'),
                                          key='metacity_theme_opacity',
                                          min=0, max=1, digits=2),
            ))
        self.add_start(box, False, False, 0)

        table = TablePack(_('Window Titlebar Action'), (
                    WidgetFactory.create('GconfComboBox',
                                         label=_('Titlebar mouse wheel action'),
                                         key='mouse_wheel_action',
                                         texts=[_('None'), _('Roll up')],
                                         values=['none', 'shade']),
                    WidgetFactory.create('GconfComboBox', 
                                         label=_('Titlebar double-click action'),
                                         key='action_double_click_titlebar',
                                         texts=[_('None'), _('Maximize'), _('Minimize'), _('Roll up'), _('Lower'), _('Menu')],
                                         values=['none', 'toggle_maximize', 'minimize', 'toggle_shade', 'lower', 'menu']),
                    WidgetFactory.create('GconfComboBox',
                                         label=_('Titlebar middle-click action'),
                                         key='action_middle_click_titlebar',
                                         texts=[_('None'), _('Maximize'), _('Minimize'), _('Roll up'), _('Lower'), _('Menu')],
                                         values=['none', 'toggle_maximize', 'minimize', 'toggle_shade', 'lower', 'menu']),
                    WidgetFactory.create('GconfComboBox', 
                                         label=_('Titlebar right-click action'),
                                         key='action_right_click_titlebar',
                                         texts=[_('None'), _('Maximize'), _('Minimize'), _('Roll up'), _('Lower'), _('Menu')],
                                         values=['none', 'toggle_maximize', 'minimize', 'toggle_shade', 'lower', 'menu']),
                ))

        self.add_start(table, False, False, 0)

        button = WidgetFactory.create('GconfCheckButton', 
                                      label=_("Enable Metacity's Compositing feature"),
                                      key='compositing_manager')
        if button:
            box = ListPack(_('Compositing Manager'), (button,))
            button.connect('toggled', self.on_compositing_button_toggled)

            self.add_start(box, False, False, 0)

    def on_compositing_button_toggled(self, widget):
        if widget.get_active():
            InfoDialog(_('To enable the compositing feature of metacity, you should manually disable Visual Effects in "Appearance".')).launch()
