from geopy.geocoders import Nominatim

# Tạo đối tượng địa chỉ
geolocator = Nominatim(user_agent="my_geocoder")
address = geolocator.geocode("VN")

# Lấy tọa độ
latitude = address.latitude
longitude = address.longitude

print(latitude, longitude)
