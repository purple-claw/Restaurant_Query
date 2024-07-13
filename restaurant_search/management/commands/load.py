import csv
import json
from django.core.management.base import BaseCommand
from restaurant_search.models import dish_search

class Command(BaseCommand):
    help = 'Load data from CSV into Restaurant model'

    def handle(self, *args, **kwargs):
        file_path = '/home/dev/Desktop/Restaurant_Query/restaurants_small.csv'
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                try:
                    print(f"Processing row: {row}")
                    items = json.loads(row['items'].strip()) if row['items'].strip() else {}
                    full_details = json.loads(row['full_details'].strip()) if row['full_details'].strip() else {}
                    restaurant = dish_search(
                        id=row['id'],
                        name=row['name'],
                        location=row['location'],
                        items=items,
                        cordinates=row['lat_long'],
                        detailDump=full_details
                    )
                    restaurant.save()
                #handling errors due to empty rows for some fields
                except json.JSONDecodeError as e:
                    data.append(f"JSONDecodeError: {e} for row: {row}")
                except Exception as e:
                    data.append(f"Error: {e} for row: {row}")

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
