from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
import models
import schemas
from datetime import datetime
import random

router = APIRouter(prefix="/api", tags=["Projects"])


@router.post("/projects", response_model=schemas.ProjectOut)
def create_project(req: schemas.ProjectCreate, current_user: models.User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    project = models.Project(
        name=req.name,
        description=req.description,
        user_id=current_user.id,
        brand_strength_score=round(random.uniform(60, 95), 1)
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/projects")
def list_projects(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    projects = db.query(models.Project).filter(models.Project.user_id == current_user.id).all()
    return [schemas.ProjectOut.from_orm(p) for p in projects]


@router.get("/projects/{project_id}")
def get_project(project_id: int, current_user: models.User = Depends(get_current_user),
                db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(
        models.Project.id == project_id, models.Project.user_id == current_user.id
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return schemas.ProjectOut.from_orm(project)


@router.put("/projects/{project_id}")
def update_project(project_id: int, req: schemas.ProjectCreate,
                   current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(
        models.Project.id == project_id, models.Project.user_id == current_user.id
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.name = req.name
    project.description = req.description
    project.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(project)
    return schemas.ProjectOut.from_orm(project)


@router.delete("/projects/{project_id}")
def delete_project(project_id: int, current_user: models.User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(
        models.Project.id == project_id, models.Project.user_id == current_user.id
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted"}


# ─── Brand Kit ───
@router.post("/brand-kit")
def save_brand_asset(req: schemas.BrandAssetCreate, current_user: models.User = Depends(get_current_user),
                     db: Session = Depends(get_db)):
    asset = models.BrandAsset(
        project_id=req.project_id,
        asset_type=req.asset_type,
        asset_value=req.asset_value
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return schemas.BrandAssetOut.from_orm(asset)


@router.get("/brand-kit/{project_id}")
def get_brand_kit(project_id: int, current_user: models.User = Depends(get_current_user),
                  db: Session = Depends(get_db)):
    assets = db.query(models.BrandAsset).filter(models.BrandAsset.project_id == project_id).all()
    return [schemas.BrandAssetOut.from_orm(a) for a in assets]


@router.delete("/brand-kit/{asset_id}")
def delete_brand_asset(asset_id: int, current_user: models.User = Depends(get_current_user),
                       db: Session = Depends(get_db)):
    asset = db.query(models.BrandAsset).filter(models.BrandAsset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(asset)
    db.commit()
    return {"message": "Asset deleted"}
