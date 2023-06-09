from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Tenant import Tenant
from ..models.Address import Address


tenant = Blueprint('tenant', __name__, template_folder='templates')


@tenant.get('/locataires')
@login_required
def tenant_read_all():
    page_title = 'CoopImmoGestion-Locataires'
    tenants = Tenant.read()
    # If connection database error
    if not isinstance(tenants, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('tenant.html', page_title=page_title,
                           tenants=tenants)


@tenant.post('/locataires/creer')
@login_required
def tenant_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Apartment and associate Address
    tenant_address: Address = Address.create(user_input)
    tenant: Tenant = Tenant.create(user_input, tenant_address)

    if tenant:
        flash("Succès de la création du locataire", "success")
    else:
        flash("Erreur lors de la création du locataire", "error")

    return redirect(url_for('tenant.tenant_read_all'))


@tenant.post('/locataires/modifier/<int:person_id>')
@login_required
def tenant_update(person_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Update Apartment
    tenant_address: Address = Address.create(user_input)
    tenant: Tenant = Tenant.update(person_id, user_input, tenant_address)

    if tenant:
        flash("Succès de la mise à jour du locataire", "success")
    else:
        flash("Erreur lors de la mise à jour du locataire", "error")

    return redirect(url_for('tenant.tenant_read_all'))


@tenant.get('/locataires/supprimer/<int:person_id>')
@login_required
def tenant_delete(person_id):
    # Delete Apartment concerned by property_id
    if Tenant.delete(person_id):
        flash("Succès de la suppression du locataire", "success")
    else:
        flash("Erreur lors de la suppression du locataire", "error")

    return redirect(url_for('tenant.tenant_read_all'))
