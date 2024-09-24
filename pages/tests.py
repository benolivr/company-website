from django.test import SimpleTestCase
from django.urls import reverse 

class HomepageTests(SimpleTestCase):
    def testUrlExistsAtCorrectLocation(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def testUrlAvailibleByName(self):
        response =  self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def testTemplateNameCorrect(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def testTemplateContent(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Company Homepage</h1>")

class AboutpageTests(SimpleTestCase):
    def testUrlExistsAtCorrectLocation(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def testUrlAvailibleByName(self):
        response =self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def testTemplateNameCorrect(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def testTemplateContent(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Company About Page</h1>")

class ProductspageTests(SimpleTestCase):
    def testUrlExistsAtCorrectLocation(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def testUrlAvailibleByName(self):
        response =self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
    
    def testTemplateNameCorrect(self):
        response = self.client.get(reverse("products"))
        self.assertTemplateUsed(response, "products.html")

    def testTemplateContent(self):
        response = self.client.get(reverse("products"))
        self.assertContains(response, "<h1>Company Products Page</h1>")
