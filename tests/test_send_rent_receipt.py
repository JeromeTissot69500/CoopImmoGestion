from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Rental import Rental
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Rent import Rent
from coopimmogestion.smtp.smtp import mail


class TestSendRentRecept:
    def test_send_rent_receipt_status(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestSendRentRecept.create_test_entity(app)

        response = client.post("/finances/quittance-loyer", data={
            "rental_id": 1,
            "start_date": "2023-05-07",
            "end_date": "2023-05-09"
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_send_rent_receipt(self, client, app):
        with app.app_context():
            with mail.record_messages() as outbox:
                mail.send_message(subject='testing',
                                  sender='coopimmogestion@gmail.com',
                                  body='test',
                                  recipients=['test@test.fr'])

                assert len(outbox) == 1
                assert outbox[0].subject == "testing"

    def test_send_rent_receipt_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestSendRentRecept.create_test_entity(app)

        response = client.post("/finances/quittance-loyer", data={
            "rental_id": 1,
            "start_date": "2023-05-07",
            "end_date": "2023-05-09"
        }, follow_redirects=True)

        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

    @staticmethod
    def create_test_entity(app):
        with app.app_context():
            address_test: Address = Address(None, 'Test', 1, '', '00000', 'Test')
            db.session.add(address_test)
            db.session.commit()

            apartment_test: Apartment = Apartment(None, 'Apartement-test', 150, 5, address_test,
                                                  2, True, 400, 100, 700)
            tenant_test: Tenant = Tenant(None, 'Test', 'Test', dt.now(), '0000000102', 'test@test.fr',
                                         address_test, 'Test', 30000)
            db.session.add(apartment_test)
            db.session.add(tenant_test)
            db.session.commit()

            rental_test: Rental = Rental(None, dt.strptime('2023-01-01', '%Y-%m-%d'),
                                         dt.strptime('2023-04-01', '%Y-%m-%d'), 1, 1)
            db.session.add(rental_test)
            db.session.commit()

            rent_test = Rent(None, 500, dt.now(), 'Locataire', 1, 1)
            db.session.add(rent_test)
            db.session.commit()


