from werkzeug.security import generate_password_hash
from bson import ObjectId
from .models import get_user_collection, get_hotel_collection, get_review_collection

def initialize_database():
    # 检查并初始化用户集合
    if get_user_collection().count_documents({}) == 0:
        admin_password = generate_password_hash("adminpassword")
        get_user_collection().insert_one({
            "username": "admin",
            "password": admin_password,
            "role": "admin"
        })
        print("Admin user created.")

    # 检查并初始化酒店集合
    if get_hotel_collection().count_documents({}) == 0:
        hotels = [
            {
                "_id": ObjectId("677fc7b1a3aa514305ef0197"),
                "description": "Park Plaza London Westminster Bridge offers modern and comfortable rooms with beautiful views of the Houses of Parliament and Big Ben. It provides excellent service, amenities, and a fantastic location.",
                "images": [
                    "https://media-cdn.tripadvisor.com/media/photo-s/18/73/6b/6b/the-park-plaza-london.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/18/73/6b/68/park-plaza-london-westminster.jpg",
                    "https://www.parkplaza.com/london-hotel-gb-sw1v-3lf/gbwestmi/media/photos/1.jpg"
                ],
                "location": "Westminster Bridge Road, London, UK",
                "name": "Park Plaza London Westminster Bridge",
                "rating": 8.3
            },
            {
                "_id": ObjectId("677fc7e71d290596a40dacb1"),
                "description": "The London Marriott Hotel County Hall is situated on the banks of the River Thames, with stunning views of the London Eye and Big Ben. This hotel features spacious rooms and an exceptional level of service.",
                "images": [
                    "https://www.marriott.com/hotels/travel/lonmh-london-marriott-hotel-county-hall/",
                    "https://cdn.londonmarriott.co.uk/media/3a6b3b94-7174-4c12-bb25-71089c6bcad9",
                    "https://media-cdn.tripadvisor.com/media/photo-s/0f/a1/a5/8c/the-marriott-county-hall.jpg"
                ],
                "location": "County Hall, London, UK",
                "name": "London Marriott Hotel County Hall",
                "rating": 8.6
            },
            {
                "_id": ObjectId("677fc7e81d290596a40dacb2"),
                "description": "The Westminster London, Curio Collection by Hilton, provides a premium stay with contemporary rooms and views of Westminster Abbey and Big Ben. A perfect choice for luxury travelers.",
                "images": [
                    "https://www.hilton.com/en/hotels/lonwiqq-the-westminster-london-curio-collection-by-hilton/",
                    "https://www.hilton.com/im/en/hotels/UKLONWI/rooms",
                    "https://media-cdn.tripadvisor.com/media/photo-s/18/73/6b/7e/the-westminster-hilton-london.jpg"
                ],
                "location": "18-24 Westminster Bridge Road, London, UK",
                "name": "Westminster London, Curio Collection by Hilton",
                "rating": 9.0
            },
            {
                "_id": ObjectId("677fc7e91d290596a40dacb3"),
                "description": "The Park Plaza County Hall London offers fantastic modern amenities and comfortable rooms, located just a short walk from major London attractions, such as the London Eye and Houses of Parliament.",
                "images": [
                    "https://www.parkplaza.com/london-hotel-gb-sw1p-3qz/gbwestco/media/photos/1.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/18/73/6b/64/park-plaza-county-hall.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/1c/71/9f/68/park-plaza-county-hall.jpg"
                ],
                "location": "1 Addington Street, London, UK",
                "name": "Park Plaza County Hall London",
                "rating": 8.4
            },
            {
                "_id": ObjectId("677fc7fd1d290596a40dacb4"),
                "description": "The London Eye hotel provides a perfect blend of relaxation and luxury, located steps away from the famous London Eye and other cultural landmarks in the city.",
                "images": [
                    "https://www.londoneye.com/assets/img/standard-images/visitor_experience.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/0e/7a/52/f1/london-eye-views.jpg",
                    "https://cdn.londonandpartners.com/-/media/images/what-to-see-and-do/london-eye/visiting-london-eye.jpg?as=1&h=1600&la=en&hash=3A9A93E8C254A028370C0C57F8E8E0A4"
                ],
                "location": "London, UK",
                "name": "The London Eye Hotel",
                "rating": 8.7
            }
        ]
        get_hotel_collection().insert_many(hotels)
        print("Example hotels created.")

    # 检查并初始化评论集合
    if get_review_collection().count_documents({}) == 0:
        reviews = [
            {
                "hotel_id": ObjectId("677fc7b1a3aa514305ef0197"),
                "user_id": ObjectId("677fc7b1a3aa514305ef0198"),
                "username": "user1",
                "content": "Great hotel with excellent service.",
                "rating": 9.0
            },
            {
                "hotel_id": ObjectId("677fc7e71d290596a40dacb1"),
                "user_id": ObjectId("677fc7b1a3aa514305ef0199"),
                "username": "user2",
                "content": "Amazing location and views.",
                "rating": 8.5
            }
        ]
        get_review_collection().insert_many(reviews)
        print("Example reviews created.")
