import logging
from uuid import UUID

import discord

from src.types import TypeClose

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


def close_ticket(manager: discord.Member, type: TypeClose, ticket_id: int, reason: str):
    logger.info(
        f'action=close_ticket user_id={manager.id} user={manager.name}#{manager.discriminator} type={type.name} ticket_id={ticket_id} reason=\"{reason}\"')


def new_ticket(ticket_id: int, name: str, student: discord.Member):
    logger.info(
        f"action=new_ticket name=\"{name}\" user_id={student.id} user={student.name}#{student.discriminator} ticket_id={ticket_id}")


def renamed_ticket(user: discord.Member, ticket_id: int, old_name: str, name: str):
    logger.info(
        f"action=renamed_ticket user_id={user.id} user={user.name}#{user.discriminator} ticket_id={ticket_id} old_name=\"{old_name}\" name=\"{name}\"")


def deleted_ticket(ticket_id: int, name: str, user: discord.Member):
    logger.info(
        f"action=deleted_ticket ticket_id={ticket_id} name=\"{name}\" user_id={user.id} user={user.name}#{user.discriminator}")


def joined_ticket(manager: discord.Member, ticket_id: int):
    logger.info(
        f"action=joined_ticket user_id={manager.id} user={manager.name}#{manager.discriminator} ticket_id={ticket_id}")


def error(user: discord.Member, err: Exception, id_err: UUID):
    logger.error(f"action=error user_id={user.id} user={user.name}#{user.discriminator} error={err} err_id={id_err}")


def reopen_ticket(user: discord.Member, ticket_id: int, name: str, owner: discord.Member):
    logger.info(
        f"action=reopen_ticket user_id={user.id} user={user.name}#{user.discriminator} ticket_id={ticket_id} name=\"{name}\" owner_id={owner.id} owner={owner.name}#{owner.discriminator}")
