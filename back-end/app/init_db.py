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
                "_id": ObjectId("677fe194b3a568eac10235e2"),
                "name": "Park Plaza London Westminster Bridge",
                "description": "You may be eligible for Genius deals at Park Plaza London Westminster Bridge. To check if Genius offers are available on your selected dates, log in.\nThe Genius offer for this property varies based on booking date, stay date and other offers.\nPark Plaza London Westminster Bridge is located on the South Bank of the Thames, Located on the South Bank opposite the Houses of Parliament and Big Ben, the London Eye, aquariums, restaurants and theatres are all within a 5-minute walk.",
                "location": "Westminster Bridge Road",
                "rating": "8.3",
                "images": [
                    "https://cf.bstatic.com/xdata/images/hotel/max1024x768/493258329.jpg?k=22e4e7897775ddfaaaefcd873814c6769a53d1d7c85b8de2a18577ae87ca1659&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max500/493258214.jpg?k=d1f8b26ac23105c7e01f1eeb4ce645174023c561d576787c26cf0f7d8573a61a&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max300/493258219.jpg?k=29a90753ceea24f621068e440005c665ecd5b38c15c70815da9d825bbe514d54&o="
                ]
            },
            {
                "_id": ObjectId("6780433ef80ea1e2c8b652de"),
                "name": "The Ship Rooms",
                "description": "The Ship Rooms is located in London and offers free WiFi and express check-in and check-out services. It is a 19-minute walk from Big Ben. The accommodation is approximately 2.2 kilometers from the Churchill War Rooms, 2.4 kilometers from the Savoy Theatre, and 2.4 kilometers from the Banqueting House. It is a 16-minute walk from Waterloo Station and less than 2.2 kilometers from the city center.\nAll the guest rooms in this hotel are equipped with desks, flat-screen TVs, private bathrooms, bedding and towels.\nThe popular landmarks near The Ship Rooms include the Houses of Parliament, Westminster Abbey and the Embankment. London City Airport is 15 kilometers away from the accommodation. \nCouples especially like the location of this accommodation and have given it a score of 8.9 for a two-person stay experience.",
                "location": "171 Kennington Road",
                "rating": "8.4",
                "images": [
                    "https://cf.bstatic.com/xdata/images/hotel/max1024x768/237723896.jpg?k=14c81197477da07eb02852fe29d73ed572bb7965fea86a9212d260870f219546&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max300/237723911.jpg?k=591676f87ebe6aef19ba5db81d13d393c6f2bfcf34bf2eb82cb8f8a3e78e660f&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max300/232851650.jpg?k=b84cc13889523212bf6187a98995fe595fb49fd1102fde02fb6f7070f882f8de&o="
                ]
            },
            {
                "_id": ObjectId("6780440cf80ea1e2c8b652df"),
                "name": "Ruby Lucy Hotel London",
                "description": "Ruby Lucy Hotel London enjoys a prime location in the Lambeth area of London.\nIt is a 12-minute walk from Big Ben, 1.3 kilometers from the Houses of Parliament, and a 17-minute walk from Westminster Abbey.\nThis luxury hotel features a bar and offers air-conditioned rooms with free WiFi and private bathrooms.\nThe accommodation is 1.7 kilometers from the city center and a 7-minute walk from Waterloo Station.\n\nAll guest rooms at this hotel are equipped with flat-screen TVs with satellite channels and safes.\nEach room at Ruby Lucy Hotel London offers bed linens and towels.\n\nThis accommodation offers a daily buffet, continental or vegetarian breakfast.\n\nThe front desk staff of this accommodation can offer advice to guests at any time.\n\nPopular landmarks near Ruby Lucy Hotel London include the Savoy Theatre, Churchill War Rooms and the Embankment.\nLondon City Airport is 14 kilometers from the accommodation.\n\nCouples especially love the location of this accommodation and have given it a score of 9.4 for the two-person stay experience.",
                "location": "100 Lower Marsh, Lambeth, London, SE1 7AB",
                "rating": "10",
                "images": [
                    "https://cf.bstatic.com/xdata/images/hotel/max1024x768/240970544.jpg?k=3dcd11fe2a10c38477a51baa56e35e9bbb5b46cdf8071e4d07be726b7a92ec53&o=",
                    "https://assets.ruby-hotels.com/Ruby-Lucy/_sliderMood/Ruby_Lucy_London_Bar_09.jpg",
                    "https://assets.ruby-hotels.com/Ruby-Lucy/_sliderBig/Ruby_Lucy_London_Bar_10.jpg",
                    "https://assets.ruby-hotels.com/Ruby-Lucy/_teaserSingleImage/134238/Ruby_Lucy_London_Fruehstueck_04.webp"
                ]
            },
            {
                "_id": ObjectId("67804500f80ea1e2c8b652e0"),
                "name": "Hyatt Regency London Albert Embankment",
                "description": "London - Hyatt Regency London Albert Embankment is located in London, near the Houses of Parliament and Westminster Abbey.\nA 12-minute walk from Big Ben and a 15-minute walk from the London Eye, the hotel offers a fitness centre and a bar.\nPOTUS Bar and Restaurant serves American cuisine, while Mezemiso Sky terrace Restaurant offers a variety of Japanese and Lebanese cuisine.\n\nEach room at the hotel has a desk.\nEvery room at the London - Hyatt Regency London Albert Embankment features a private bathroom, free Wi-Fi and a wardrobe.\nSome rooms also have river views.\nAll rooms have wardrobes.\n\nStaff at the 24-hour front desk speak German, Greek, English and Spanish.\n\nBanqueting House is an 18-minute walk from London - Hyatt Regency London Albert Embankment.\nLondon City Airport is 12 km away.",
                "location": "10-11 Albert Embankment, Lambeth, London, SE1 7TP, United Kingdom",
                "rating": "9.9",
                "images": [
                    "https://cf.bstatic.com/xdata/images/hotel/max1024x768/422360326.jpg?k=8d12c9357c4a521c74dbca0de6bfa7a01714cb04443c5462fb4550ba0d0b4845&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max300/422360313.jpg?k=bcf5cb40f00adafb2fdf95969b60dd1490f85f985cbe09fd08ae41e9ac534e37&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max300/422360307.jpg?k=f7969937dbc21a1b93a7118d95e01bfdda8ead31b659ee9b46fb61e192f50a80&o="
                ]
            },
            {
                "_id": ObjectId("6780459df80ea1e2c8b652e1"),
                "name": "Marlin Waterloo",
                "description": "Marlin Waterloo is 600 metres from the London Eye, 800 metres from the Houses of Parliament and a 1-minute walk from Lambeth North Tube Station. Waterloo Tube Station is a 10-minute walk away and London City Airport is 11 km away.",
                "location": "111 Westminster Bridge Road, Lambeth, London, SE1 7HR, United Kingdom",
                "rating": "8.7",
                "images": [
                    "https://cf.bstatic.com/xdata/images/hotel/max1024x768/295247004.jpg?k=7176f4ee9fa5a994618fec888945c5e81ae001bf3666faf8b3b05202ac64aa6d&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max500/106865764.jpg?k=27febead2ea72550b4ac6a2d3c9bdd11096c927f70441e805987e9b06d2bc773&o=",
                    "https://cf.bstatic.com/xdata/images/hotel/max500/97829558.jpg?k=7ef34dbc1126e8e0f180d25d2f5c1162ca714b841200ac8e55241bc3ae163028&o="
                ]
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
