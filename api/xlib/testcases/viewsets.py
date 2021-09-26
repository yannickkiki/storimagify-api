from rest_framework import status


class ModelViewSetTestCaseMixin:

    @classmethod
    def setUpTestData(cls):
        cls.model.objects.create(**cls.data_create)

    def setUp(self) -> None:
        response = self.client.get(path=self.base_url)
        self.instance_data = response.json()[0]
        self.detail_url = f"{self.base_url}{self.instance_data['id']}/"

    def test_create(self):
        response = self.client.post(path=self.base_url, data=self.instance_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        instance_created = response.json()
        self.assertCountEqual(instance_created.keys(), self.fields)

    def test_retrieve(self):
        response = self.client.get(path=self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        instance_retrieved = response.json()
        self.assertCountEqual(instance_retrieved.keys(), self.fields)

    def test_update(self):
        response = self.client.put(path=self.detail_url, data=self.instance_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        instance_updated = response.json()
        self.assertCountEqual(instance_updated.keys(), self.fields)

    def test_delete(self):
        response = self.client.delete(path=self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list(self):
        response = self.client.get(path=self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        instance_list = response.json()
        self.assertIsInstance(instance_list, list)
        self.assertCountEqual(instance_list[0].keys(), self.fields)
