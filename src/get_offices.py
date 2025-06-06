import os
import requests
import folium
import os
import json

try:
    with open('API_KEY.txt', 'r') as file:
        API_KEY = file.readline().strip()
        if not API_KEY:
            print("Warning: API_KEY.txt found but is empty.")
except FileNotFoundError:
    API_KEY = None
    print("Error: 'API_KEY.txt' not found in the current directory.")
except Exception as e:
    API_KEY = None
    print(f"Error reading API key: {e}")

PLACES_API = "https://places.googleapis.com/v1/places:searchText"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location"
}

CITY_COORDINATES = {
    "Madrid": {"latitude": 40.4165, "longitude": -3.70256, "filename": "offices_mapM.html", "json_filename": "offices_madrid.json"},
    "Barcelona": {"latitude": 41.3851, "longitude": 2.1734, "filename": "offices_mapB.html", "json_filename": "offices_barcelona.json"},
    "Valencia": {"latitude": 39.4699, "longitude": -0.3763, "filename": "offices_mapV.html", "json_filename": "offices_valencia.json"}
}

# Get offices from Google Places API


def get_offices(city_name, center_coords):
    if not API_KEY:
        print("API_KEY is not set. Cannot proceed with API call.")
        return {"error": "API_KEY not provided"}, 400

    payload = {
        "textQuery": "Oficina de extranjería",
        "locationBias": {
            "circle": {
                "center": center_coords,
                "radius": 10000
            }
        },
        "regionCode": "es"  # España (escalable si se necesita)
    }

    try:
        response = requests.post(PLACES_API, json=payload, headers=headers)
        response.raise_for_status()
        return response.json(), 200

    except requests.exceptions.HTTPError as e:
        print(
            f"HTTP Error from Google Places API for {city_name}: {e.response.status_code} - {e.response.text}")
        return {"error": f"Error de conexión con Google Places ({city_name}): {e.response.text}"}, e.response.status_code

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error for {city_name}: {e}")
        return {"error": f"Error de red ({city_name}): {e}"}, 500

    except requests.exceptions.RequestException as e:
        print(
            f"General Request Error at Google Places API for {city_name}: {e}")
        return {"error": f"Error de conexión con Google Places ({city_name}): {e}"}, 500

    except Exception as e:
        print(
            f"Unexpected error when processing Google Places response for {city_name}: {e}")
        return {"error": f"Error interno del servidor ({city_name}): {e}"}, 500

# Create a folium map with offices data


def create_offices_map(offices_data, map_center, json_output_path):
    m = folium.Map(location=map_center, zoom_start=13)
    offices_list = []  # List to store office data in JSON file

    if "places" in offices_data and offices_data["places"]:
        print(f"Found {len(offices_data['places'])} places")

        for place in offices_data["places"]:
            if "location" in place and "latitude" in place["location"] and "longitude" in place["location"]:
                latitude = place["location"]["latitude"]
                longitude = place["location"]["longitude"]
                address = place.get("formattedAddress",
                                    "Dirección no disponible")
                display_name = place.get("displayName", {}).get(
                    "text", "Oficina de extranjería")

                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"<b>{display_name}</b><br>{address}",
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)

                # Add office data to the list
                offices_list.append({
                    "name": display_name,
                    "address": address,
                    "latitude": latitude,
                    "longitude": longitude
                })
            else:
                print(f"Place without location data: {place}")
    else:
        print("No places found in the API response or 'places' list is empty.")
        if "error" in offices_data:
            print(f"API Error: {offices_data['error']}")

    # Write the JSON file
    if offices_list:
        with open(json_output_path, 'w', encoding='utf-8') as json_file:
            json.dump(offices_list, json_file, ensure_ascii=False, indent=4)
    else:
        print("No offices data to write to JSON file.")

    return m



if __name__ == "__main__":
    for city_name, city_info in CITY_COORDINATES.items():
        # Generate map for {city_name}
        center_coords = {
            "latitude": city_info["latitude"],
            "longitude": city_info["longitude"]
        }

        offices_response, status_code = get_offices(city_name, center_coords)

        # Check if the response is valid and contains offices
        if status_code == 200 and "places" in offices_response:
            map_file_path = os.path.join("public", city_info["filename"])
            json_file_path = os.path.join("public", city_info["json_filename"])

            # Create the map and save it
            offices_map = create_offices_map(
                offices_response, [city_info["latitude"], city_info["longitude"]], json_file_path)
            offices_map.save(map_file_path)
            print(f"Map saved to {map_file_path}")

        elif "error" in offices_response:
            print(f"Error for {city_name}: {offices_response['error']}")
        else:
            print(
                f"Failed to retrieve office data or no offices found for {city_name}.")
