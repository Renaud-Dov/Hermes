#  Copyright (c) 2023.
#  Author: Dov Devers (https://bugbear.fr)
#  All right reserved
import asyncio

import discord

from src import logs
from src.client import HermesClient
from src.other import Embed
from src.other.db import add_ticket, get_ticket_nb
from src.other.types import TypeStatusTicket


async def create_ticket(client: HermesClient, thread: discord.Thread):
    config = client.get_config(thread.guild.id)
    config_forum = config.get_forum(thread.parent_id)
    if not config_forum:
        return

    await thread.edit(auto_archive_duration=10080)  # 7 days to archive
    embed = Embed.newThreadEmbed(thread, TypeStatusTicket.Created)
    view = discord.ui.View()
    view.add_item(Embed.urlButton(thread.jump_url))
    view.add_item(Embed.statusButton(TypeStatusTicket.Created))
    channel_id = config_forum.webhook_channel
    channel = client.get_channel(channel_id)
    await channel.send(embed=embed, view=view)

    await thread.join()

    tag_id = config.get_week_practical_tag(thread)
    if tag_id:
        tag = thread.parent.get_tag(tag_id)
        if not tag:
            await thread.send(f"Error: tag {tag_id} not found")
        else:
            await thread.add_tags(tag)
            await thread.send(f"Auto added tag {thread.parent.get_tag(tag_id).name}")

    if "Solved" in [tag.name for tag in thread.applied_tags]:
        await asyncio.sleep(0.5)
        await thread.send("Merci de préciser votre login et le tag de votre trace ci dessous./Please specify your "
                          f"login and the tag of your trace below. {thread.owner.mention}")

    add_ticket(thread.id, thread.owner_id)
    id_ticket = get_ticket_nb(thread.id)
    await thread.edit(name=f"[{id_ticket}] {thread.name}")

    logs.new_ticket(thread.id, thread.name, thread.owner)
