from fastapi import APIRouter

app_home = APIRouter()


@app_home.get('/', tags=["Intro"])
async def hello() -> dict:
    """
    A function that returns a dictionary with a greeting message.

    Returns
    -------
    dict
        A dictionary containing a greeting message.
    """
    return {"message": "Hello!"}


@app_home.get('/bye', tags=["Intro"])
async def bye() -> dict:
    """
    A function that returns a dictionary with a farewell message.

    Returns
    -------
    dict
        A dictionary containing a farewell message.
    """
    return {"message": "Bye!"}

@app_home.get("/health", status_code=200)
async def get_health() -> dict:
    """
    A function that returns a dictionary with a status message.

    Returns
    -------
    dict
        A dictionary containing a status message.
    """
    return {
        "status": "OK"
    }