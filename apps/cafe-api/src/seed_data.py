from main import app, db, Cafe

def seed_database():
    """Seed the database with sample cafe data."""
    with app.app_context():
        # Check if data already exists
        if Cafe.query.first():
            print("Database already contains data. Skipping seed.")
            return
        
        sample_cafes = [
            Cafe(
                name="Science Gallery Cafe",
                map_url="https://goo.gl/maps/RhkutvkRE1p",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Pearse St, Dublin 2",
                seats="50-100",
                has_toilet=True,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=True,
                coffee_price="€3.50"
            ),
            Cafe(
                name="The Fumbally",
                map_url="https://goo.gl/maps/XkjZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Fumbally Lane, Dublin 8",
                seats="20-30",
                has_toilet=True,
                has_wifi=True,
                has_sockets=False,
                can_take_calls=False,
                coffee_price="€3.00"
            ),
            Cafe(
                name="Brother Hubbard",
                map_url="https://goo.gl/maps/YqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Capel St, Dublin 1",
                seats="30-50",
                has_toilet=True,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=False,
                coffee_price="€3.20"
            ),
            Cafe(
                name="3FE Coffee",
                map_url="https://goo.gl/maps/ZqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Grand Canal St, Dublin 2",
                seats="10-20",
                has_toilet=False,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=True,
                coffee_price="€3.80"
            ),
            Cafe(
                name="Clement & Pekoe",
                map_url="https://goo.gl/maps/AqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="South William St, Dublin 2",
                seats="20-30",
                has_toilet=True,
                has_wifi=True,
                has_sockets=False,
                can_take_calls=False,
                coffee_price="€3.30"
            ),
            Cafe(
                name="Kaph",
                map_url="https://goo.gl/maps/BqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Drury St, Dublin 2",
                seats="15-25",
                has_toilet=True,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=True,
                coffee_price="€3.40"
            ),
            Cafe(
                name="Two Pups Coffee",
                map_url="https://goo.gl/maps/CqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Francis St, Dublin 8",
                seats="10-15",
                has_toilet=False,
                has_wifi=True,
                has_sockets=False,
                can_take_calls=False,
                coffee_price="€3.10"
            ),
            Cafe(
                name="Network Cafe",
                map_url="https://goo.gl/maps/DqZ9QqZ9Qq",
                img_url="https://lh3.googleusercontent.com/p/AF1QipPP_YQqVpK8xYvN_GqZqKcVqKqVqKqVqKqVqKqV",
                location="Aungier St, Dublin 2",
                seats="40-60",
                has_toilet=True,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=True,
                coffee_price="€3.00"
            )
        ]
        
        db.session.add_all(sample_cafes)
        db.session.commit()
        print(f"Successfully seeded {len(sample_cafes)} cafes to the database.")

if __name__ == '__main__':
    seed_database()
