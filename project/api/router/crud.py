from api.models.pydantic import SummaryPayloadSchema
from api.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url, 
        summary='dummy summary'
    )
    await summary.save()
    return summary.id

