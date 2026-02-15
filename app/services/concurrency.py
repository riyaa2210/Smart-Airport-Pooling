# app/services/concurrency.py

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Cab


async def assign_cab_safe(session: AsyncSession, cab_id: int, seats_required: int):
    """
    Row-level locking using SELECT FOR UPDATE
    Prevents two users booking same seat simultaneously
    """

    result = await session.execute(
        select(Cab).where(Cab.id == cab_id).with_for_update()
    )

    cab = result.scalar_one_or_none()

    if not cab:
        return False

    if cab.available_seats >= seats_required:
        cab.available_seats -= seats_required
        await session.commit()
        return True

    return False
