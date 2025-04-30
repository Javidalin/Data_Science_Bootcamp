import os
import pickle
from typing import Optional, Union

import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from sklearn.model_selection import train_test_split


app = FastAPI(title="Advertising Model API")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Landing page with API information and documentation links."""
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/api/v1/extra")
# def extra():
#     return "El Webhook funciona"


@app.get("/api/v1/predict")
def predict(
    tv: Optional[float] = Query(None, description="TV advertising budget"),
    radio: Optional[float] = Query(None, description="Radio advertising budget"),
    newspaper: Optional[float] = Query(None, description="Newspaper advertising budget")
):
    with open('ad_model.pkl', 'rb') as f:
        model = pickle.load(f)

    print(tv, radio, newspaper)
    
    if tv is None or radio is None or newspaper is None:
        raise HTTPException(status_code=400, detail="Args empty, not enough data to predict")
    else:
        input_data = pd.DataFrame({
            'TV': [tv],
            'radio': [radio],
            'newspaper': [newspaper]
        })
        prediction = model.predict(input_data)
    
    return {"predictions": float(prediction[0])}

# Retrain endpoint
@app.get("/api/v1/retrain")
def retrain():
    if os.path.exists("data/Advertising_new.csv"):
        data = pd.read_csv('data/Advertising_new.csv')

        X_train, X_test, y_train, y_test = train_test_split(
            data.drop(columns=['sales']),
            data['sales'],
            test_size=0.20,
            random_state=42
        )

        model = Lasso(alpha=6000)
        model.fit(X_train, y_train)
        rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
        mape = mean_absolute_percentage_error(y_test, model.predict(X_test))
        model.fit(data.drop(columns=['sales']), data['sales'])
        
        with open('ad_model.pkl', 'wb') as f:
            pickle.dump(model, f)
        return f"Model retrained. New evaluation metric RMSE: {str(round(rmse, 2))}, MAPE: {str(round(mape, 2))}%"
    else:
        raise HTTPException(status_code=404, detail="New data for retrain NOT FOUND. Nothing done!")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)