from app.core.tools import repeat_every
from app.dramatiq_worker.clear_message_xq import clear_message_in_XQ

@repeat_every(seconds=3600)
async def event_startup_clear_message_in_XQ():
    clear_message_in_XQ()



events = [v for k, v in locals().items() if k.startswith('event_startup_')]