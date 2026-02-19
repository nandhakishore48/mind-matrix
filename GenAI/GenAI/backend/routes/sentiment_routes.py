from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
import models
import schemas
import mock_ai

router = APIRouter(prefix="/api", tags=["Sentiment"])


@router.post("/sentiment-analyze")
def analyze_sentiment(req: schemas.SentimentRequest, current_user: models.User = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    result = mock_ai.analyze_sentiment(req.text)

    # Save report to DB
    report = models.SentimentReport(
        project_id=req.project_id,
        input_text=req.text,
        positive_pct=result["positive"],
        neutral_pct=result["neutral"],
        negative_pct=result["negative"],
        brand_perception_score=result["brand_perception_score"],
        suggestions="; ".join(result["suggestions"])
    )
    db.add(report)
    db.commit()

    return result
