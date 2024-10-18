from fastapi import APIRouter
from sqlmodel import Session

from app.modules.organization import Organization

router = APIRouter(prefix="/organizations")
@router.post("/")
def create_organization(organization: Organization):
    from app.main import db
    with Session(db.engine) as session:
        session.add(organization)
        session.commit()
        session.refresh(organization)
        return organization


@router.get('/')
def get_organizations():
    from app.main import db
    with Session(db.engine) as session:
        return session.query(Organization).all()


@router.put('/<organization_id>')
def update_organization(organization_id: int, updated_organization: Organization):
    from app.main import db
    with Session(db.engine) as session:
        organization = session.query(Organization).filter(Organization.id == organization_id).first()
        if organization:
            organization.name = updated_organization.name
            organization.owner = updated_organization.owner
            session.commit()
            return organization
        else:
            return {"error": "Organization not found"}


@router.delete('/<organization_id>')
def delete_organization(organization_id: int):
    from app.main import db
    with Session(db.engine) as session:
        organization = session.query(Organization).filter(Organization.id == organization_id).first()
        if organization:
            session.delete(organization)
            session.commit()
            return {"message": "Organization deleted"}
        else:
            return {"error": "Organization not found"}
