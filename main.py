from fastapi import FastAPI, HTTPException
from typing import Optional
from recommended_from_description import recommend_books_based_on_description
from recommend_by_title import recommend_books

app = FastAPI()


@app.get("/recommend_by_description/")
def recommend_by_description(description: str, num_recommendations: Optional[int] = 5):
    try:
        recommendations = recommend_books_based_on_description(description, num_recommendations)
        recommendations_filled = recommendations.fillna("N/A")  # or 0, or any other appropriate default value

        return recommendations_filled.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/recommend_by_title/")
def recommend_by_title(title: str, num_recommendations: Optional[int] = 5):
    try:
        recommendations = recommend_books(title, num_recommendations)
        recommendations_filled = recommendations.fillna("N/A")  # or 0, or any other appropriate default value

        return recommendations_filled.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
