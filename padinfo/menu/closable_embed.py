from typing import Optional

from discord import Message
from discordmenu.embed.control import EmbedControl
from discordmenu.embed.menu import EmbedMenu

from tsutils.menu.panes import MenuPanes
from padinfo.view.awakening_help import AwakeningHelpView
from padinfo.view.closable_embed import ClosableEmbedViewState
from padinfo.view.id_traceback import IdTracebackView

view_types = {
    AwakeningHelpView.VIEW_TYPE: AwakeningHelpView,
    IdTracebackView.VIEW_TYPE: IdTracebackView,
}


class ClosableEmbedEmoji:
    home = '\N{HOUSE BUILDING}'


class ClosableEmbedMenu:
    MENU_TYPE = 'ClosableEmbedMenu'
    message = None

    @staticmethod
    def menu():
        embed = EmbedMenu({}, ClosableEmbedMenu.message_control)
        return embed

    @staticmethod
    async def respond_with_home(messagge: Optional[Message], ims, **data):
        dgcog = data['dgcog']
        user_config = data['user_config']

        view_state = await ClosableEmbedViewState.deserialize(dgcog, user_config, ims)
        control = ClosableEmbedMenu.message_control(view_state)
        return control

    @staticmethod
    def message_control(state: ClosableEmbedViewState):
        view = view_types[state.view_type]
        return EmbedControl(
            [view.embed(state, state.props)],
            []
        )


class ClosableEmbedMenuPanes(MenuPanes):
    DATA = {
        ClosableEmbedEmoji.home: (ClosableEmbedMenu.respond_with_home, None)
    }

    HIDDEN_EMOJIS = [
        ClosableEmbedEmoji.home
    ]
