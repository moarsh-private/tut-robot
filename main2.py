from telethon import TelegramClient,events,sessions

API_ID = "7932417"
API_HASH = "c250664d2d69e7b59c1b010f55066935"
client = TelegramClient(sessions.StringSession("1AZWarzkBu4fPWaaaNRnDZwflx-0RoMcWwlyfGiWOrQTXj-NFsWMJIkhhcgk9sGd4E6UXVcLwucfDPzN_v5QAVGHNIwXMRCOvBP807Y3-luQYYKd-rciTfErKyQDSjlAEoEx-RfNCAKut9WeXB6kc7XovXPmSITjfogSbbo-QAkx3JSy23dten3kGAXtgyyE_EcG9K3M16Ni51CKcZ3uUsKdvFNlLsJcgqFqAmhN2NJQSRNcJ-JSwRLZV94iXqyNHBQbTRqiqujemBw7xyr0UzXQeZ7jTk_7RU2JNevdeFkyu0wBSymbJZXbRVnxoRWIV17A4IoNNlGMBPlkdcxjmYccuH4gbQNk="), API_ID, API_HASH)
@client.on(events.NewMessage)
async def handler(m):
    await m.reply(m.raw_text+" From Telethon")


client.start(bot_token="5257174102:AAEJNKw7IH0ef70GTlzhi07ieUyL8cbVUQs")
print("R    U   N")
client.run_until_disconnected()