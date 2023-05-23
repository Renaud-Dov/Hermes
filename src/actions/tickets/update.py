#  Copyright (c) 2023.
#  Author: Dov Devers (https://bugbear.fr)
#  All right reserved
import asyncio

import discord

from src.client import HermesClient


async def update_ticket(client: HermesClient, before: discord.Thread, after: discord.Thread):
    config_forum = client.config.get_forum(after.parent_id)
    if not config_forum:
        return

    if "Moulinette" in [tag.name for tag in after.applied_tags] \
            and not "Moulinette" in [tag.name for tag in before.applied_tags]:
        await asyncio.sleep(0.5)
        await after.send("Merci de préciser votre login et le tag de votre trace ci dessous./Please specify your "
                         "login and the tag of your trace below.")
