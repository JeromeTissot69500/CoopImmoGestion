from coopimmogestion.models.Apartment import Apartment


class TestCreateApartment:
    def test_send_data_apartment(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        with app.app_context():
            try:
                apartment_test = Apartment.query.filter_by(reference="test").first()
            except Exception:
                apartment_test = None
        assert apartment_test is not None

    def test_create_apartment_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-appartements</title>' in response.data.decode('utf-8')