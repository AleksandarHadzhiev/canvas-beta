"""Organization CRUD operations endpoints."""
from fastapi import APIRouter
from sqlmodel import Session
from app.db_conn import db
from app.modules.organization import Organization

router = APIRouter(prefix="/organizations")
@router.post("/")
def create_organization(organization: Organization):
    """Create organization

    Args:
        organization (Organization): contains the data needed to create the organization.

    Returns:
        Organization: the  newly created organization.
    """
    with Session(db.engine) as session:
        session.add(organization)
        session.commit()
        session.refresh(organization)
        return organization


@router.get('/')
def get_organizations():
    """Get a list of organizations.

    Returns:
        List<Organization>: A list of organizations.
    """
    with Session(db.engine) as session:
        return session.query(Organization).all()


@router.put('/<organization_id>')
def update_organization(organization_id: int, updated_organization: Organization):
    """Update organization.

    Args:
        organization_id (int): id of the organization to update.
        updated_organization (Organization): the new data.

    Returns:
        dict: Contains either error message or organization
    """
    with Session(db.engine) as session:
        organization = session.query(Organization).filter(
            Organization.id == organization_id).first()
        if organization:
            organization.name = updated_organization.name
            organization.owner = updated_organization.owner
            session.commit()
            return {"organization": organization}

        return {"error": "Organization not found"}


@router.delete('/<organization_id>')
def delete_organization(organization_id: int):
    """Delete a organization.

    Args:
        organization_id (int): id of the organization to delete.

    Returns:
        dict: message for success of failure.
    """
    with Session(db.engine) as session:
        organization = session.query(Organization).filter(
            Organization.id == organization_id).first()
        if organization:
            session.delete(organization)
            session.commit()
            return {"message": "Organization deleted"}

        return {"error": "Organization not found"}
