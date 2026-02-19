from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import require_admin
from typing import List
from models import User, Project, BrandAsset, GeneratedContent, SentimentReport, ChatHistory, AdminLog
import schemas

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.get("/users")
def list_users(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "role": u.role,
        "is_active": u.is_active,
        "created_at": u.created_at.isoformat() if u.created_at else None
    } for u in users]


@router.get("/stats")
def get_stats(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_projects = db.query(Project).count()
    total_content = db.query(GeneratedContent).count()
    total_sentiments = db.query(SentimentReport).count()
    total_chats = db.query(ChatHistory).count()
    total_assets = db.query(BrandAsset).count()

    return {
        "total_users": total_users,
        "total_projects": total_projects,
        "total_generated_content": total_content,
        "total_sentiment_reports": total_sentiments,
        "total_chat_messages": total_chats,
        "total_brand_assets": total_assets,
        "api_calls_today": total_content + total_sentiments + total_chats + 42  # mock
    }


@router.get("/logs")
def get_logs(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    logs = db.query(AdminLog).order_by(AdminLog.created_at.desc()).limit(50).all()
    return [{
        "id": l.id,
        "action": l.action,
        "details": l.details,
        "admin_id": l.admin_id,
        "created_at": l.created_at.isoformat() if l.created_at else None
    } for l in logs]


@router.put("/users/{user_id}/suspend")
def suspend_user(user_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = not user.is_active
    db.commit()

    log = AdminLog(action="user_toggled", details=f"User {user.username} active={user.is_active}", admin_id=admin.id)
    db.add(log)
    db.commit()

    return {"message": f"User {'activated' if user.is_active else 'suspended'}", "is_active": user.is_active}


@router.delete("/users/{user_id}")
def delete_user(user_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role == "admin":
        raise HTTPException(status_code=400, detail="Cannot delete admin user")

    log = AdminLog(action="user_deleted", details=f"User {user.username} deleted", admin_id=admin.id)
    db.add(log)

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
