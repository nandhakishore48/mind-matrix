from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ─── Auth Schemas ───
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


# ─── Project Schemas ───
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = ""


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    brand_strength_score: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ─── Brand Name Generator ───
class BrandNameRequest(BaseModel):
    industry: str
    keywords: str
    target_audience: str
    tone: str  # professional, playful, modern, bold


# ─── Logo Generator ───
class LogoRequest(BaseModel):
    brand_name: str
    style: str  # minimal, modern, vintage, tech
    primary_color: str
    secondary_color: str


# ─── Brand Identity ───
class BrandIdentityRequest(BaseModel):
    brand_name: str
    industry: str
    target_audience: str


# ─── Content Generator ───
class ContentRequest(BaseModel):
    brand_name: str
    content_type: str  # social_post, ad_copy, blog, email
    tone: str
    keywords: Optional[str] = ""
    length: Optional[str] = "medium"


# ─── Sentiment Analysis ───
class SentimentRequest(BaseModel):
    text: str
    project_id: Optional[int] = None


# ─── Chatbot ───
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = ""


class ChatResponse(BaseModel):
    response: str
    suggestions: List[str] = []


# ─── Brand Asset ───
class BrandAssetCreate(BaseModel):
    project_id: int
    asset_type: str
    asset_value: str


class BrandAssetOut(BaseModel):
    id: int
    project_id: int
    asset_type: str
    asset_value: str
    created_at: datetime

    class Config:
        from_attributes = True
