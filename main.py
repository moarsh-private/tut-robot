import asyncio
from pyrogram import Client

SESSION = "AQB35a_RqdQa11LulQ41JoclkuX5wvNIDYe0W-DVtw8lp0I4iR6jFfsdUxjq1CRdDocPdBP6gOw3L5ci2_kOStYFvGa8zpQeemR_N0Ui6TAadAqY0FF8jUtlSU21F57KeB9hq21U7xXUYNafOglOVeYfyXKIjRO2nszRjucijzT7OZ19dwM0Tuy5pxTJh7-5Rq0tCqtM6T5K4p-yb95nK5Saa2QhhOkdom-udYXENWTOrSnznAmrQYqVfMK6vw-xVXSXbJr19yVYsm84gHTgb20xZ5iVQIkTO4PJe08DQStC9hc5QbYuN0WwR1qQ25Hu0nAkpHAsK6jZUApRzoXtcgv5AAAAATlaHFYB"
API_ID = "7932417"
API_HASH = "c250664d2d69e7b59c1b010f55066935"

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)

@app.on_message()
async def handler(_,m):
    await m.reply(m.text)

print("R    U   N")
app.run()