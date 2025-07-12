import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mydb =
MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

# Data
WORK_EXPERIENCES = [
    {
        "position": "Production Engineer Fellow",
        "company": "Major League Hacking",
        "years": "2025–2025",
        "description": "Deployed a personal flask web application",
    },
    {
        "position": "Manager",
        "company": "Epic Theatres",
        "years": "2019-2020",
        "description": "Managed theatre operations",
    },
]

EDUCATION = [
    {
        "school": "Western Governors University",
        "degree": "M.Sc. in SWE",
        "years": "2025–2026",
    },
    {
        "school": "Florida State University",
        "degree": "B.Sc. in CS",
        "years": "2021–2024",
    },
]

HOBBIES = [
    {
        "name": "Running",
        "image": "running.png",
        "description": "I love running outdoors and have completed several 5K races.",
    },
    {
        "name": "Weightlifting",
        "image": "weightlifting.png",
        "description": "Strength training has been a passion of mine for years.",
    },
    {
        "name": "Reading",
        "image": "reading.png",
        "description": "I enjoy reading both fiction and non-fiction books.",
    },
]

PLACES = [
    {"name": "London", "lat": 51.5072, "lon": -0.1276, "date": "Dec 2019"},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "date": "Dec 2019"},
    {"name": "Madrid", "lat": 40.4168, "lon": -3.7038, "date": "Dec 2024"},
    {"name": "Toronto", "lat": 43.6511, "lon": -79.3837, "date": "Dec 2023"},
    {"name": "Dublin", "lat": 53.3498, "lon": -6.2603, "date": "Dec 2024"},
]


@app.route("/")
def main():
    """Main route"""
    return render_template("main.html")


# HTMX Content Routes
@app.route("/content/home")
def content_home():
    """HTMX endpoint for home content"""
    return """
    <div class="text-center py-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">Welcome to My Portfolio</h2>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Hello! I'm Michael. When I'm not at the keyboard you can find me at the gym, at a cafe, or at a bar with friends.
        </p>
        <img src="/static/img/headshot.png" 
             alt="Michael" 
             class="w-32 h-32 rounded-full mx-auto mb-8 shadow-lg object-cover">
        
        <!-- Quick navigation cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
            <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow cursor-pointer"
                 hx-get="/content/about" 
                 hx-target="#main-content">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">About Me</h3>
                <p class="text-gray-600">Learn about my work experience and education</p>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow cursor-pointer"
                 hx-get="/content/hobbies" 
                 hx-target="#main-content">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">My Hobbies</h3>
                <p class="text-gray-600">Discover what I enjoy in my free time</p>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow cursor-pointer"
                 hx-get="/content/map" 
                 hx-target="#main-content">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Places I've Been</h3>
                <p class="text-gray-600">See the cool places I've visited</p>
            </div>
        </div>
    </div>
    """


@app.route("/content/about")
def content_about():
    """HTMX endpoint for about content"""
    work_html = ""
    for job in WORK_EXPERIENCES:
        work_html += f"""
        <div class="border-l-4 border-blue-500 pl-6 py-4">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-2">
                <h4 class="text-xl font-semibold text-gray-900">{job["position"]}</h4>
                <span class="text-sm text-gray-500 mt-1 md:mt-0">{job["years"]}</span>
            </div>
            <p class="text-blue-600 font-medium mb-2">{job["company"]}</p>
            <p class="text-gray-600">{job["description"]}</p>
        </div>
        """

    edu_html = ""
    for edu in EDUCATION:
        edu_html += f"""
        <div class="border-l-4 border-green-500 pl-6 py-4">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-2">
                <h4 class="text-xl font-semibold text-gray-900">{edu["degree"]}</h4>
                <span class="text-sm text-gray-500 mt-1 md:mt-0">{edu["years"]}</span>
            </div>
            <p class="text-green-600 font-medium">{edu["school"]}</p>
        </div>
        """

    return f"""
    <div class="max-w-4xl mx-auto">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">About Me</h2>
            <p class="text-lg text-gray-600 max-w-2xl mx-auto">
                Hello! I'm Michael. When I'm not at the keyboard you can find me at the gym, at a cafe, or at a bar with friends.
            </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
            <!-- Work Experience -->
            <div class="bg-white rounded-lg p-8 shadow-sm">
                <h3 class="text-2xl font-bold text-gray-900 mb-6">Work Experience</h3>
                <div class="space-y-6">
                    {work_html}
                </div>
            </div>

            <!-- Education -->
            <div class="bg-white rounded-lg p-8 shadow-sm">
                <h3 class="text-2xl font-bold text-gray-900 mb-6">Education</h3>
                <div class="space-y-6">
                    {edu_html}
                </div>
            </div>
        </div>
    </div>
    """


@app.route("/content/hobbies")
def content_hobbies():
    """HTMX endpoint for hobbies content"""
    hobbies_html = ""
    for hobby in HOBBIES:
        hobbies_html += f"""
        <div class="bg-white rounded-lg shadow-sm overflow-hidden hover:shadow-lg transition-shadow cursor-pointer"
             hx-get="/hobby/{hobby["name"].lower()}" 
             hx-target="#hobby-detail" 
             hx-swap="innerHTML">
            <img src="/static/img/{hobby["image"]}" 
                 alt="{hobby["name"]}" 
                 class="w-full h-48 object-cover">
            <div class="p-6">
                <h4 class="text-xl font-semibold text-gray-900 mb-2">{hobby["name"]}</h4>
                <p class="text-gray-600">{hobby["description"]}</p>
            </div>
        </div>
        """

    return f"""
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">My Hobbies</h2>
            <p class="text-lg text-gray-600 max-w-2xl mx-auto">
                Here are some of the activities I enjoy in my free time. Click on any hobby to learn more!
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-8">
            {hobbies_html}
        </div>

        <!-- Hobby Detail Area -->
        <div id="hobby-detail"></div>
    </div>
    """


@app.route("/hobby/<hobby_name>")
def hobby_detail(hobby_name):
    """HTMX endpoint for individual hobby details"""
    hobby_details = {
        "running": {"frequency": "4-5 times per week", "location": "Local park trails"},
        "weightlifting": {"frequency": "3-4 times per week", "location": "Local gym"},
        "reading": {"frequency": "Daily", "location": "Coffee shops and home"},
    }

    hobby = next((h for h in HOBBIES if h["name"].lower() == hobby_name), None)
    details = hobby_details.get(hobby_name, {})

    if not hobby:
        return "<p class='text-red-500 text-center'>Hobby not found</p>"

    return f"""
    <div class="bg-white rounded-lg shadow-sm p-8 mt-8">
        <div class="flex justify-between items-start mb-4">
            <h3 class="text-2xl font-bold text-gray-900">{hobby["name"]}</h3>
            <button class="text-gray-400 hover:text-gray-600" 
                    hx-get="/content/hobbies" 
                    hx-target="#main-content">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </div>
        <p class="text-gray-600 mb-6">{hobby["description"]}</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <span class="font-semibold text-gray-900">Frequency:</span>
                <span class="text-gray-600 ml-2">{details.get("frequency", "Regular")}</span>
            </div>
            <div>
                <span class="font-semibold text-gray-900">Favorite Location:</span>
                <span class="text-gray-600 ml-2">{details.get("location", "Various places")}</span>
            </div>
        </div>
    </div>
    """


@app.route("/content/map")
def content_map():
    """HTMX endpoint for map content"""
    places_html = ""
    for place in PLACES:
        places_html += f"""
        <div class="border border-gray-200 rounded-lg p-6 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer"
             onclick="focusOnPlace({place['lat']}, {place['lon']}, '{place['name']}')">
            <h4 class="text-xl font-semibold text-gray-900 mb-2">{place["name"]}</h4>
            <p class="text-blue-600 font-medium mb-1">{place["date"]}</p>
            <p class="text-sm text-gray-500">Click to view on map</p>
        </div>
        """

    # Convert places to JavaScript format
    places_js = str(PLACES).replace("'", '"')
    
    # Get Google Maps API key from environment
    google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY_HERE')

    return f"""
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-8">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Places I've Visited</h2>
            <p class="text-lg text-gray-600 max-w-2xl mx-auto">
                Here are some of the cool locations and countries I've had the chance to explore. Click on a location to focus on it on the map!
            </p>
        </div>

        <!-- Google Map Container -->
        <div class="bg-white rounded-lg shadow-sm mb-8 overflow-hidden">
            <div id="map" style="height: 500px; width: 100%;"></div>
        </div>

        <!-- Places Grid -->
        <div class="bg-white rounded-lg p-8 shadow-sm">
            <h3 class="text-2xl font-bold text-gray-900 mb-6">My Travel Timeline</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {places_html}
            </div>
        </div>
    </div>

    <script>
        let map;
        let markers = [];
        const places = {places_js};

        function initMap() {{
            // Initialize map centered on Europe (rough center of your travels)
            map = new google.maps.Map(document.getElementById("map"), {{
                zoom: 3,
                center: {{ lat: 45.0, lng: 10.0 }},
                styles: [
                    {{
                        "featureType": "water",
                        "elementType": "geometry",
                        "stylers": [{{ "color": "#e9e9e9" }}, {{ "lightness": 17 }}]
                    }},
                    {{
                        "featureType": "landscape",
                        "elementType": "geometry",
                        "stylers": [{{ "color": "#f5f5f5" }}, {{ "lightness": 20 }}]
                    }}
                ]
            }});

            // Add markers for each place
            places.forEach((place, index) => {{
                const marker = new google.maps.Marker({{
                    position: {{ lat: place.lat, lng: place.lon }},
                    map: map,
                    title: place.name,
                    animation: google.maps.Animation.DROP,
                    icon: {{
                        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(`
                            <svg width="30" height="40" viewBox="0 0 30 40" xmlns="http://www.w3.org/2000/svg">
                                <path d="M15 0C6.716 0 0 6.716 0 15c0 8.284 15 25 15 25s15-16.716 15-25C30 6.716 23.284 0 15 0z" fill="#3b82f6"/>
                                <circle cx="15" cy="15" r="8" fill="white"/>
                                <text x="15" y="19" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#3b82f6">${{index + 1}}</text>
                            </svg>
                        `),
                        scaledSize: new google.maps.Size(30, 40),
                        anchor: new google.maps.Point(15, 40)
                    }}
                }});

                // Add info window
                const infoWindow = new google.maps.InfoWindow({{
                    content: `
                        <div class="p-2">
                            <h3 class="font-bold text-lg text-gray-900">${{place.name}}</h3>
                            <p class="text-blue-600 font-medium">${{place.date}}</p>
                        </div>
                    `
                }});

                marker.addListener("click", () => {{
                    // Close all other info windows
                    markers.forEach(m => m.infoWindow.close());
                    infoWindow.open(map, marker);
                }});

                markers.push({{ marker, infoWindow }});
            }});

            // Create a path connecting all the places
            const flightPath = new google.maps.Polyline({{
                path: places.map(place => ({{ lat: place.lat, lng: place.lon }})),
                geodesic: true,
                strokeColor: "#3b82f6",
                strokeOpacity: 0.6,
                strokeWeight: 2,
            }});

            flightPath.setMap(map);
        }}

        function focusOnPlace(lat, lng, name) {{
            map.setCenter({{ lat: lat, lng: lng }});
            map.setZoom(10);
            
            // Find and open the corresponding marker's info window
            const markerIndex = places.findIndex(place => place.lat === lat && place.lon === lng);
            if (markerIndex !== -1) {{
                // Close all info windows first
                markers.forEach(m => m.infoWindow.close());
                // Open the selected one
                markers[markerIndex].infoWindow.open(map, markers[markerIndex].marker);
            }}
        }}

        // Initialize map when the content loads
        if (typeof google !== 'undefined' && google.maps) {{
            initMap();
        }} else {{
            // Load Google Maps API if not already loaded
            const script = document.createElement('script');
            script.src = 'https://maps.googleapis.com/maps/api/js?key={google_maps_api_key}&callback=initMap';
            script.async = true;
            script.defer = true;
            document.head.appendChild(script);
        }}
    </script>
    """
