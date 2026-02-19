from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
import models
import schemas
import mock_ai

router = APIRouter(prefix="/api", tags=["Brand"])


@router.post("/brand-names")
def generate_brand_names(req: schemas.BrandNameRequest, current_user: models.User = Depends(get_current_user)):
    names = mock_ai.generate_brand_names(req.industry, req.keywords, req.target_audience, req.tone)
    return {"brand_names": names, "industry": req.industry, "tone": req.tone}


@router.post("/logo-generate")
def generate_logo(req: schemas.LogoRequest, current_user: models.User = Depends(get_current_user)):
    logos = mock_ai.generate_logo_urls(req.brand_name, req.style, req.primary_color, req.secondary_color)
    return {"logos": logos, "brand_name": req.brand_name, "style": req.style}


@router.post("/brand-identity")
def generate_brand_identity(req: schemas.BrandIdentityRequest, current_user: models.User = Depends(get_current_user)):
    identity = mock_ai.generate_brand_identity(req.brand_name, req.industry, req.target_audience)
    return identity
