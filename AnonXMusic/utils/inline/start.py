from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["✨️𝗢𝘄𝗻𝗲𝗿✨️"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["✨️𝗦𝘂𝗽𝗽𝗼𝗿𝘁✨️"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["𝗨𝗽𝗱𝗮𝘁𝗲"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["✨️𝗢𝘄𝗻𝗲𝗿✨️"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
