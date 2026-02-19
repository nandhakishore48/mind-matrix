from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default="user")  # user / admin
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    projects = relationship("Project", back_populates="owner")
    chat_history = relationship("ChatHistory", back_populates="user")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, default="")
    user_id = Column(Integer, ForeignKey("users.id"))
    brand_strength_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="projects")
    brand_assets = relationship("BrandAsset", back_populates="project")
    generated_content = relationship("GeneratedContent", back_populates="project")
    sentiment_reports = relationship("SentimentReport", back_populates="project")


class BrandAsset(Base):
    __tablename__ = "brand_assets"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    asset_type = Column(String(50))  # logo, color, name, tagline, mission, vision, values, story
    asset_value = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="brand_assets")


class GeneratedContent(Base):
    __tablename__ = "generated_content"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    content_type = Column(String(50))  # social_post, ad_copy, blog, email
    content_text = Column(Text)
    tone = Column(String(30))
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="generated_content")


class SentimentReport(Base):
    __tablename__ = "sentiment_reports"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    input_text = Column(Text)
    positive_pct = Column(Float, default=0.0)
    neutral_pct = Column(Float, default=0.0)
    negative_pct = Column(Float, default=0.0)
    brand_perception_score = Column(Float, default=0.0)
    suggestions = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="sentiment_reports")


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="chat_history")


class AdminLog(Base):
    __tablename__ = "admin_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String(100))
    details = Column(Text)
    admin_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
