from coopimmogestion.models.Rental import Rental


class TestUpdateRental:
    def test_send_data_update_rental(self, client):
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

        client.post("/locataires/creer", data={
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        response = client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_update_rental(self, client, app):
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

        client.post("/locataires/creer", data={
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        with app.app_context():
            with app.app_context():
                try:
                    rental_test = Rental.query.filter_by(text_start_date="2023-04-09").first()
                except Exception:
                    rental_test = None
            assert rental_test is not None

    def test_update_rental_redirect(self, client):
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

        client.post("/locataires/creer", data={
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        response = client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')