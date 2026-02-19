from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
import models
import schemas
import mock_ai

router = APIRouter(prefix="/api", tags=["Chat"])


@router.post("/chat")
def chat(req: schemas.ChatRequest, current_user: models.User = Depends(get_current_user),
         db: Session = Depends(get_db)):
    result = mock_ai.chat_response(req.message, req.context)

    # Save to chat history
    history = models.ChatHistory(
        user_id=current_user.id,
        message=req.message,
        response=result["response"]
    )
    db.add(history)
    db.commit()

    return result
