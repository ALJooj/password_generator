import molotov

@molotov.scenario(50)
async def scenario_get(session):
    async with session.get("http://127.0.0.1:8000/api") as resp:
        assert resp.status == 200


@molotov.scenario(50)
async def scenario_get(session):
    resp = await session.post("http://localhost:8000/api", params={'q': 'devops'})
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    assert redirect_status == 302, error

