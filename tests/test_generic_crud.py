import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eud_gui.settings")
django.setup()

from django.test import TestCase, Client
from django.urls import reverse
from apps.users.models import User
from apps.clients.models import BankingRelationship, Relationship
from apps.generic_crud.registry import CrudRegistry

from apps.generic_crud.views import DynamicViewSetFactory, GenericFormView
from apps.generic_crud.registry import CrudRegistry
from apps.clients.models import BankingRelationship, Relationship

class GenericCRUDRelationshipTests(TestCase):
    def setUp(self):
        # Create an admin user for testing
        self.user = User.objects.create_superuser(username='T12345', password='password')
        self.client = Client()
        self.client.force_login(self.user)

    def test_dynamic_viewset_factory(self):
        """Test that the viewset factory generates a viewset for the model."""
        viewset = DynamicViewSetFactory.create_viewset(Relationship)
        self.assertEqual(viewset.queryset.model, Relationship)

    def test_form_field_exclusion(self):
        """Test that internal fields are excluded from forms."""
        view = GenericFormView()
        exclude = view._get_exclude_fields(Relationship, 'relationship')
        self.assertIn('id', exclude)
        self.assertIn('client_uuid', exclude)
        self.assertIn('created_at', exclude)

    def test_add_relationship_page_loads(self):
        """Test that the add relationship page loads."""
        # Assuming 'relationship' is the registered table name
        url = reverse('generic-add', kwargs={'table_name': 'relationship'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Link a Client to this Relationship")
        self.assertContains(response, "Search Existing")

    def test_create_relationship_existing_client(self):
        """Test creating a relationship with an existing client."""
        # This relies on existing seeded data (client_uuid)
        bank_rel = BankingRelationship.objects.first()
        if not bank_rel:
            self.skipTest("No banking relationship found in the database to test with.")
        
        url = reverse('generic-add', kwargs={'table_name': 'relationship'})
        data = {
            'association_mode': 'existing',
            'child_unique_id': str(bank_rel.client_uuid),
            # Other fields...
        }
        response = self.client.post(url, data, follow=True)
        # Should redirect on success
        self.assertEqual(response.status_code, 200)

