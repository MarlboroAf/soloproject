import xlrd
import os
from pathlib import Path
from django.core.management.base import BaseCommand
from shop.models import Product, Order

class Command(BaseCommand):
    help = 'Load data from xls'

    def handle(self, *args, **options):
        try:
            # Delete existing data before importing new data
            self.delete_existing_data()

            # Get the base directory of the project
            base_dir = self.get_base_directory()

            # Construct the file path of the Excel file to be imported
            file_path = os.path.join(base_dir, 'shop', 'data', 'products.xls')

            # Import data from the Excel file
            self.import_data_from_excel(file_path)

            # Print success message
            self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
        except Exception as e:
            # Print error message if an exception occurs
            self.stderr.write(self.style.ERROR(f"Error occurred: {e}"))

    def delete_existing_data(self):
        # Delete all existing data in Data models
        Product.objects.all().delete()
        Order.objects.all().delete()

        # Print success message
        self.stdout.write(self.style.SUCCESS("Tables dropped successfully"))

    def get_base_directory(self):
        # Get the base directory of the Django project
        return Path(__file__).resolve().parent.parent.parent.parent

    def import_data_from_excel(self, file_path):
        # Open the Excel workbook
        workbook = xlrd.open_workbook(file_path)

        # Import data from the first sheet (data sheet)
        self.import_data_sheet(workbook.sheet_by_index(0))

    def import_data_sheet(self, sheet):
        # Iterate through rows in the data sheet
        for row_idx in range(1, sheet.nrows):
            # Extract product name and price
            row = sheet.row_values(row_idx)
            sku = row[0]
            name = row[1]
            price = row[5]
            # Create Data objects and print information
            Products = Product.objects.create(sku=sku,name=name, price=price,)
            print(f" Product Name: {name}, price: {price}")
