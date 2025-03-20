from fastapi import FastAPI,Depends




app =FastAPI()


@app.get("/")
async def get_api():
    return {
        "message": "welcome to the backend api"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)
