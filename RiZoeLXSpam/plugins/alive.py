from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/572a9c973dc1965a6b46c.png"
  

          
rizoel = " DIVINE SPAMโค๏ธโ๐ฅ โง\n\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโโ\n"

rizoel += f"โฃโฃ **แดสแดสแดษด แด แดสsษชแดษด** : `3.9.6`\n"
 
rizoel += f"โฃโฃ **sแดแดแดแดสแด** : [JOIN](https://t.me/centraI_community)\n"

rizoel += f"โฃโฃ **แดสแดษดษดแดส** : [JOIN](https://t.me/avalivefru)\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโโ\n\n"

rizoel += f"๐ค [๐๐๐๐](https://t.me/parvcodes) ๐ค"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
