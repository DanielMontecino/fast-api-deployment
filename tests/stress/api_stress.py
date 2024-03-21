from locust import HttpUser, task

class StressUser(HttpUser):
    
    @task
    def predict_argentinas(self):
        self.client.post(
            "/predict", 
            json={
                "flights": [
                    {
                        "SIGLADES": "Miami",
                        "DIANOM": "Domingo",
                        "fecha_i": "2024-01-01 23:30:00",
                        "OPERA": "Aerolineas Argentinas", 
                        "TIPOVUELO": "N", 
                        "MES": 3
                    }
                ]
            }
        )


    @task
    def predict_latam(self):
        self.client.post(
            "/predict", 
            json={
                "flights": [
                    {
                        "SIGLADES": "Miami",
                        "DIANOM": "Domingo",
                        "fecha_i": "2024-01-01 23:30:00",
                        "OPERA": "Grupo LATAM", 
                        "TIPOVUELO": "N", 
                        "MES": 3
                    }
                ]
            }
        )