from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
import models
import schemas
import mock_ai

router = APIRouter(prefix="/api", tags=["Content"])


@router.post("/content-generate")
def generate_content(req: schemas.ContentRequest, current_user: models.User = Depends(get_current_user),
                     db: Session = Depends(get_db)):
    content = mock_ai.generate_content(req.brand_name, req.content_type, req.tone, req.keywords, req.length)

    # Save to DB
    generated = models.GeneratedContent(
        project_id=None,
        content_type=req.content_type,
        content_text=content["content"],
        tone=req.tone
    )
    db.add(generated)
    db.commit()

    return content
