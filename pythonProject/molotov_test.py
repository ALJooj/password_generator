import molotov

@molotov.scenario(100)
async def scenario_get(session):
    async with session.get("http://127.0.0.1:8000/api") as resp:
        assert resp.status == 200


